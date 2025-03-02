#!/bin/bash
source files.sh

for discipline in $PDF_DIRS; do
  echo $discipline
  mkdir -p ./static/$discipline
  if [ -f ./$discipline/appunti.pdf ]; then
    cp ./$discipline/appunti.pdf ./static/$discipline/appunti.pdf
  fi
  if [ -f ./$discipline/report.pdf ]; then
    cp ./$discipline/report.pdf ./static/$discipline/report.pdf
  fi
  if [ -f ./$discipline/slides.pdf ]; then
    cp ./$discipline/slides.pdf ./static/$discipline/slides.pdf
  fi
  if [ -f ./$discipline/main.pdf ]; then
    cp ./$discipline/main.pdf ./static/$discipline/main.pdf
  fi
done
cp ./index.html ./static/index.html
