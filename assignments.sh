#!/bin/bash

for folder in $(find -mindepth 1 -type d); do
    cd $folder
    echo -e "entering $folder"
    pdflatex appunti.tex
    cd ..
done
