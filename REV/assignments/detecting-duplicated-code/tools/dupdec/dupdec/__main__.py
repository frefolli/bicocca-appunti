import argparse
import sys
import os
import enum
import re
import Levenshtein
import scipy.sparse # type: ignore
import matplotlib.pyplot # type: ignore
import numpy
import json
import yaml
import hashlib
import typing

IOTA_COUNTER=0

def reset_iota():
  global IOTA_COUNTER
  IOTA_COUNTER = 0

def iota() -> int:
  global IOTA_COUNTER
  value = IOTA_COUNTER
  IOTA_COUNTER += 1
  return value

FileRange = tuple[str, int|None, int|None]
FixedFileRange = tuple[str, int, int]
Line = str
File = tuple[FixedFileRange, list[Line]]
NormalizedFile = tuple[FixedFileRange, list[tuple[int, Line]]]
MechanicalReport=tuple[FixedFileRange, FixedFileRange, list[tuple[tuple[int, Line], tuple[int, Line]]]]

def file_range_repr(file_range: FileRange) -> str:
  repr: str = file_range[0]
  if file_range[1] is not None:
    assert file_range[1] is not None
    repr += ":%d" % file_range[1]
    repr += ":%d" % file_range[2]
  return repr

def fixed_file_range_repr(file_range: FixedFileRange) -> str:
  return "%s:%d:%d" % file_range

def fixed_file_range_with_line_repr(file_range: FixedFileRange, line_index: int):
  return "%s:%d" % (file_range[0], line_index)

reset_iota()
class Language(enum.Enum):
  PYTHON=iota()
  JAVA=iota()
  C=iota()
  CPP=iota()
  PERL=iota()

LANGUAGES={
  Language.PYTHON: ['py'],
  Language.JAVA: ['java'],
  Language.C: ['h', 'c'],
  Language.CPP: ['hh', 'cc', 'cxx', 'hpp', 'cpp', 'c++'],
  Language.PERL: ['pl']
}
def parse_language(inp: str) -> Language:
  inp = inp.strip()
  for (lang, patterns) in LANGUAGES.items():
    if inp in patterns:
      return lang
  raise ValueError(inp)

def infer_language(file_ranges: list[FileRange]) -> Language:
  lang: Language|None = None
  for file_range in file_ranges:
    ext = file_range[0].split('.')[-1]
    try:
      current_lang = parse_language(ext)
      if lang is None:
        lang = current_lang
      else:
        if lang != current_lang:
          raise ValueError("conflicting language %s suggests %s but %s was previosly captured" % (file_range, current_lang, lang))
    except ValueError:
      pass
  if lang is None:
    raise ValueError("unable to infer language from extensions of files: %s" % file_ranges)
  return lang

def parse_file_range(inp: str) -> FileRange:
  splitted_inp: list[str] = inp.strip().split(':')
  if len(splitted_inp) == 1:
    path = splitted_inp[0]
    path = os.path.normpath(os.path.expanduser(path))
    if not os.path.exists(path):
      raise ValueError(inp)
    return (path, None, None)
  elif len(splitted_inp) == 3:
    path = splitted_inp[0]
    path = os.path.normpath(os.path.expanduser(path))
    if not os.path.exists(path):
      raise ValueError(inp)
    return (path, int(splitted_inp[1]), int(splitted_inp[2]))
  raise ValueError(inp)

def load_file(file_range: FileRange) -> File:
  path, start_line, end_line = file_range
  fd = open(path, "r")
  lines: list[Line] = fd.readlines()
  fd.close()
  if start_line is None:
    start_line = 0
  if end_line is None:
    end_line = len(lines)
  if start_line < 0 or end_line > len(lines) or start_line > end_line:
    raise ValueError("invalid range (%d, %d) for file '%s'" % (start_line, end_line, path))
  return ((path, start_line, end_line), lines[start_line:end_line])

LINE_COMMENTS={
  Language.PYTHON: re.compile("#"),
  Language.JAVA: re.compile("//"),
  Language.C: re.compile("//"),
  Language.CPP: re.compile("//"),
  Language.PERL: re.compile("#"),
}
def identify_line_comment(line: Line, lang: Language) -> int|None:
  regex = LINE_COMMENTS[lang]
  match = regex.search(line)
  if match is None:
    return None
  return match.span()[0]

STARTING_COMMENTS={
  Language.PYTHON: re.compile('"""'),
  Language.JAVA: re.compile("/\\*"),
  Language.C: re.compile("/\\*"),
  Language.CPP: re.compile("/\\*"),
  Language.PERL: re.compile("=(pod|begin)"),
}
def identify_starting_comment(line: Line, lang: Language) -> int|None:
  regex = STARTING_COMMENTS[lang]
  match = regex.search(line)
  if match is None:
    return None
  return match.span()[0]

ENDING_COMMENTS={
  Language.PYTHON: re.compile('"""'),
  Language.JAVA: re.compile("\\*/"),
  Language.C: re.compile("\\*/"),
  Language.CPP: re.compile("\\*/"),
  Language.PERL: re.compile("=(cut)"),
}
def identify_closing_comment(line: Line, lang: Language) -> int|None:
  regex = ENDING_COMMENTS[lang]
  match = regex.search(line)
  if match is None:
    return None
  return match.span()[1]

OPENED_COMMENT = False
def remove_comments(line: Line, lang: Language) -> Line:
  global OPENED_COMMENT
  if OPENED_COMMENT:
    end = identify_closing_comment(line, lang)
    if end is not None:
      line = line[end:]
      OPENED_COMMENT = False
      return remove_comments(line, lang)
    return ''
  else:
    start = identify_starting_comment(line, lang)
    if start is not None:
      line = line[:start]
      OPENED_COMMENT = True
      return remove_comments(line, lang)
    inline = identify_line_comment(line, lang)
    if inline is not None:
      return line[:inline]
  return line

def remove_spaces(line: Line) -> Line:
  return line.replace(" ", "").replace("\t", "").replace("\n", "")

NOISE_SMELLS=re.compile("^[{}()\\[\\];]|(pass|end|else)([:;])?$")
def remove_noise(line: Line) -> Line:
  if NOISE_SMELLS.match(line):
    return ''
  return line

def normalize_file(file: File, lang: Language) -> NormalizedFile:
  global OPENED_COMMENT
  OPENED_COMMENT = False

  lines = []
  file_start = file[0][1]
  for (idx, line) in enumerate(file[1]):
    line = remove_comments(line, lang)
    line = remove_spaces(line)
    line = remove_noise(line)
    if len(line) > 0:
      lines.append((idx + file_start, line))
  return (file[0], lines)


def check_if_match(s1: str, s2: str, tol: float) -> bool:
  edit_distance = Levenshtein.distance(s1, s2)
  return edit_distance <= min(len(s1), len(s2)) * tol

def compare_files(f1: NormalizedFile, f2: NormalizedFile, tol: float) -> scipy.sparse.spmatrix:
  f1_length, f2_length = f1[0][2], f2[0][2]
  result: scipy.sparse.dok_matrix = scipy.sparse.eye(f1_length, f2_length, dtype=numpy.bool).todok()
  for (i, line1) in enumerate(f1[1]):
    for (j, line2) in enumerate(f2[1]):
      if check_if_match(line1[1], line2[1], tol):
        result[line1[0], line2[0]] = 1
  return result.tocoo()

def make_mechanical_report(f1: File, f2: File, comparison_result: scipy.sparse.spmatrix) -> MechanicalReport:
  not_same_file: bool = (f1[0][0] != f2[0][0])
  matches: list[tuple[tuple[int, Line], tuple[int, Line]]] = []
  for (i, j, equals) in zip(comparison_result.row, comparison_result.col, comparison_result.data):
    if equals and (i != j or not_same_file):
      matches.append(((i + 1, f1[1][i].strip()), (j + 1, f2[1][j].strip())))
  return (f1[0], f2[0], matches)

def make_mechanical_reports(files: list[File], normalized_files: list[File], tol: float) -> list[MechanicalReport]:
  reports: list[MechanicalReport] = []
  n_of_files = len(files)
  for i in range(n_of_files):
    for j in range(i + 1, n_of_files):
      reports.append(make_mechanical_report(files[i], files[j], compare_files(normalized_files[i], normalized_files[j], tol)))
  return reports

SERIALIZATION_FORMATS={
  'json': json.dumps,
  'yaml': yaml.dump
}
def serialize_mechanical_reports(reports: list[MechanicalReport], output: str|None, format: str):
  if output is None:
    pass
    for report in reports:
      f1, f2, matches = report
      print("## %s | %s" % (fixed_file_range_repr(f1), fixed_file_range_repr(f2)))
      print("")
      print("| LFile | LLine | <> | RLine | RFile |")
      print("| ----- | ----- | ----- | ----- | ----- |")
      for match in matches:
        print("| %s | `%s` | <> | `%s` | %s |" % (fixed_file_range_with_line_repr(f1, match[0][0]),
                                        match[0][1],
                                        match[1][1],
                                        fixed_file_range_with_line_repr(f2, match[1][0])))
  else:
    file: typing.IO[typing.Any]
    with open(output, "w") as file:
      file.write(SERIALIZATION_FORMATS[format](reports))

def compute_rank(comparison_result: scipy.sparse.spmatrix) -> float:
  nnz = comparison_result.getnnz()
  shape = comparison_result.shape
  return nnz / (shape[0]*shape[1])

def make_dotplot_report(f1: NormalizedFile, f2: NormalizedFile, comparison_result: scipy.sparse.spmatrix, output: str):
  f1_repr: str = fixed_file_range_repr(f1[0])
  f2_repr: str = fixed_file_range_repr(f2[0])
  title = "%s-%s" % (f1_repr, f2_repr)
  filename = "%s.png" % hashlib.sha1(title.encode()).hexdigest()
  path = os.path.join(output, filename)
  rank = compute_rank(comparison_result)
  matplotlib.pyplot.ylabel(f1_repr)
  matplotlib.pyplot.xlabel(f2_repr)
  matplotlib.pyplot.spy(comparison_result, marker='.', markersize=5)
  matplotlib.pyplot.savefig(path)
  return (filename, rank)

def make_dotplot_reports(files: list[NormalizedFile], tol: float, output: str, format: str):
  if os.path.exists(output):
    os.system("rm -r %s" % output)
  os.makedirs(output)
  n_of_files = len(files)
  ranking: list[tuple[str, float]] = []
  for i in range(n_of_files):
    for j in range(i + 1, n_of_files):
      f1 = files[i]
      f2 = files[j]
      filename, rank = make_dotplot_report(f1, f2, compare_files(f1, f2, tol), output)
      ranking.append((filename, rank))
  ranking = sorted(ranking, key = lambda item: item[1])
  file: typing.IO[typing.Any]
  with open(os.path.join(output, "ranking.%s" % format), "w") as file:
    file.write(SERIALIZATION_FORMATS[format](ranking))

def parse_args() -> argparse.Namespace:
  argument_parser = argparse.ArgumentParser(description="detect duplicates code via Mechanical Code Comparison")
  argument_parser.add_argument('-l', '--lang', type=parse_language, default=None, help="specifies the programming languages used in files, if not issued it's automatically inferred from input names")
  argument_parser.add_argument('FILE', type=parse_file_range, nargs='+', help="files to analyze, in <PATH>[:STARTLINE:ENDLINE] format")
  argument_parser.add_argument('-M', '--mechanical', action='store_true', default=False, help='mechanical comparison')
  argument_parser.add_argument('-D', '--dotplot', action='store_true', default=False, help='dotplot production')
  argument_parser.add_argument('-o', '--output', type=str, default=None, help='where to store output (file for mechanical | dir for dotplot)')
  argument_parser.add_argument('-f', '--format', type=str, choices=['json', 'yaml'], default='json', help='how to store mechanical output')
  argument_parser.add_argument('-t', '--tol', type=float, default=0.05, help='edit distance tolerance for line matching')
  return argument_parser.parse_args(sys.argv[1:])

def main():
  cli_args: argparse.Namespace = parse_args()
 
  if len(cli_args.FILE) < 2:
    file_range = cli_args.FILE[0]
    print("Warning: implicit re-inclusion of '%s'" % file_range_repr(file_range))
    print("         I suggest to always explicitly declare included files")
    cli_args.FILE.append(file_range)

  if (not cli_args.mechanical) and (not cli_args.dotplot):
    raise ValueError("should specify either -M/-D")

  if cli_args.lang is None:
    cli_args.lang = infer_language(cli_args.FILE)

  files: list[File] = [load_file(file_range) for file_range in cli_args.FILE]
  normalized_files: list[NormalizedFile] = [normalize_file(file, cli_args.lang) for file in files]

  if cli_args.mechanical:
    serialize_mechanical_reports(make_mechanical_reports(files, normalized_files, cli_args.tol), cli_args.output, cli_args.format)
  elif cli_args.dotplot:
    if cli_args.output is None:
      cli_args.output = 'out'
    make_dotplot_reports(normalized_files, cli_args.tol, cli_args.output, cli_args.format)
  else:
    pass

if __name__ == "__main__":
  main()
