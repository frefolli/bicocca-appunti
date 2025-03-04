#!/bin/bash
DIR=$PWD
PUBDIR=/tmp/bicocca-appunti-web

if [ -d $PUBDIR ]; then
  rm -rf $PUBDIR
fi

#git clone git@github.com:frefolli/bicocca-appunti --branch deployment --depth 1 ../bicocca-appunti-web

make
./static.sh

mkdir -p $PUBDIR
cp -r ./static/* $PUBDIR
cd $PUBDIR
git init -b deployment
git status
git add .
git remote add origin git@github.com:frefolli/bicocca-appunti
git commit -m "publish $(date)"
git push origin deployment -f -u
cd $DIR
