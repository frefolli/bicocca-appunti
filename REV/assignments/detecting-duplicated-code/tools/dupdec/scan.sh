#!/bin/bash

INDIR=$1
FLAG=$2

if [ "$INDIR" == "-h" ] || [ "$INDIR" == "--help" ] || [ "$FLAG" == "-h" ] || [ "$FLAG" == "--help" ]; then
  echo "usage: ./scan.sh <indir> <-D|-M>"
  exit 0
fi

if [ ! -d "$INDIR" ]; then
  echo "usage: ./scan.sh <indir> <-D|-M>"
  exit 0
fi

if [ "$FLAG" != "-D" ] && [ "$FLAG" != "-M" ]; then
  echo "usage: ./scan.sh <indir> <-D|-M>"
  exit 0
fi

if [ ! -z "$TOL" ]; then
  TOL="-t $TOL"
fi

FILES=$(find $INDIR -type f -regex ".*\\.\\(py\\|c\\|cc\\|cxx\\|cpp\\|h\\|hh\\|hxx\\|hpp\\|inc\\|java\\|pl\\)")
cmd="python -m dupdec $FLAG $FILES"
echo -e "> $cmd"
$cmd
