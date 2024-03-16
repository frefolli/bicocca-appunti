#!/bin/bash

for discipline in "$@"; do
  mkdir -p ./static/$discipline
  cp ./$discipline/appunti.pdf ./static/$discipline/appunti.pdf
done
cp ./index.html ./static/index.html
