#!/bin/bash
DIR=$PWD

if [ ! -d ../bicocca-appunti-web ]; then
  git clone git@github.com:frefolli/bicocca-appunti --branch deployment --depth 1 ../bicocca-appunti-web
fi

make
./static.sh
rm ../bicocca-appunti-web/*
cp -r ./static/* ../bicocca-appunti-web/
cd ../bicocca-appunti-web
git status
git add .
git commit -m "publish $(date)"
git push origin deployment
cd $DIR
