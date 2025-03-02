from __future__ import annotations
import enum
import copy
import typing
import functools
from itertools import groupby

def consume(iterable: typing.Iterator):
  for _ in iterable:
    pass

def all_equal(iterable: typing.Iterable):
  g = groupby(iterable)
  return next(g, True) and not next(g, False)
assert not all_equal([1, 2, 2, 2])
assert not all_equal([2, 1, 2, 2])
assert not all_equal([2, 2, 1, 2])
assert not all_equal([2, 2, 2, 1])
assert all_equal([2, 2, 2, 2])

def find_min(iterable: typing.Iterable):
  iterable = iter(iterable)
  cur_idx = -1
  obj_idx = None
  obj = None
  while True:
    try:
      next_obj = next(iterable)
      cur_idx += 1
      if next_obj is not None:
        if obj is None or next_obj < obj:
          obj = next_obj
          obj_idx = cur_idx
    except StopIteration:
      break
  return obj_idx, obj
assert find_min([1, 2, 2, 2]) == (0, 1)
assert find_min([2, 1, 2, 2]) == (1, 1)
assert find_min([2, 2, 1, 2]) == (2, 1)
assert find_min([2, 2, 2, 1]) == (3, 1)
assert find_min([2, 2, 2, 2]) == (0, 2)
assert find_min([None, 2, 1, 3]) == (2, 1)

TermID=int
DocID=int

InvertedIndex=dict[TermID, list[DocID]]

class Expr:
  class Op(enum.Enum):
    TERM = 0
    AND = 1
    OR = 2

    def __repr__(self) -> str:
      match self:
        case Expr.Op.TERM:
          return "TERM"
        case Expr.Op.AND:
          return "AND"
        case Expr.Op.OR:
          return "OR"
      return "<>"

  def __init__(self, op: Expr.Op, operands: list[Expr] = [], term: TermID|None = None) -> None:
    self.op: Expr.Op = op
    self.operands: list[Expr] = operands
    self.term: TermID|None = term
    self.docs: typing.Iterator[DocID] = iter([])
    self.doc: DocID|None = None

  @staticmethod
  def And(x: Expr, y: Expr) -> Expr:
    return Expr(Expr.Op.AND, operands=[x, y])

  @staticmethod
  def Or(x: Expr, y: Expr) -> Expr:
    return Expr(Expr.Op.OR, operands=[x, y])
  
  @staticmethod
  def Term(x: TermID) -> Expr:
    return Expr(Expr.Op.TERM, term=x)

  def __repr__(self) -> str:
    return str((self.op, self.operands, self.doc))

class Resolver:
  @staticmethod
  def initialize_expression(index: InvertedIndex, expr: Expr) -> Expr:
    expr = copy.copy(expr)
    if expr.op == Expr.Op.TERM:
      assert expr.term is not None
      expr.docs = iter(index[expr.term])
      expr.doc = next(expr.docs, None)
    expr.operands = list(map(lambda operand: Resolver.initialize_expression(index, operand), expr.operands))
    return expr

  @staticmethod
  def not_finished_yet(expr: Expr) -> bool:
    return expr.doc is not None or sum(map(Resolver.not_finished_yet, expr.operands)) > 0

  @staticmethod
  def consume_all(expr: Expr) -> None:
    if expr.op == Expr.Op.TERM:
      while next(expr.docs, None) is not None:
        pass
      expr.doc = None
    else:
      consume(map(Resolver.consume_all, expr.operands))
      expr.doc = None

  @staticmethod
  def consume_if(expr: Expr, by_doc: DocID|None = None) -> None:
    if by_doc is None or expr.doc == by_doc:
      expr.doc = None
      Resolver.apply_iteration(expr)

  @staticmethod
  def apply_iteration(expr: Expr) -> None:
    if expr.doc is None:
      consume(map(Resolver.apply_iteration, expr.operands))
      match expr.op:
        case Expr.Op.TERM:
          expr.doc = next(expr.docs, None)
        case Expr.Op.AND:
          operand_docs = list(map(lambda operand: operand.doc, expr.operands))
          while True:
            if None in operand_docs:
              Resolver.consume_all(expr)
              break
            if all_equal(operand_docs):
              expr.doc = operand_docs[0]
              consume(map(Resolver.consume_if, expr.operands))
              break
            min_idx, min_doc = find_min(operand_docs)
            expr.operands[min_idx].doc = None
            Resolver.apply_iteration(expr.operands[min_idx])
            operand_docs[min_idx] = expr.operands[min_idx].doc
        case Expr.Op.OR:
          operand_docs = list(map(lambda operand: operand.doc, expr.operands))
          _, min_doc = find_min(operand_docs)
          expr.doc = min_doc
          if min_doc is not None:
            consume(map(lambda operand: Resolver.consume_if(operand, by_doc=min_doc), expr.operands))

  @staticmethod
  def resolve(index: InvertedIndex, expr: Expr) -> list[DocID]:
    expr = Resolver.initialize_expression(index, expr)
    docs: list[DocID] = []
    while Resolver.not_finished_yet(expr):
      Resolver.apply_iteration(expr)
      if expr.doc is not None:
        docs.append(expr.doc)
        expr.doc = None
    return docs

if __name__ == "__main__":
  index: InvertedIndex = {
    0: [1, 4, 6],
    1: [2, 4, 6],
    2: [2, 3, 7]
  }
  expr: Expr = Expr.And(Expr.Term(0), Expr.Or(Expr.Term(1), Expr.Term(2)))
  docs: list[DocID] = Resolver.resolve(index, expr)

  print("docs =", docs)
  assert (docs == [4, 6, 7])
