#!/bin/bash

function cleanTypeFolder() {
    DIRPATH=$1
    TYPE=$2
    echo -e "deleting $TYPE from $DIRPATH"
    find $DIRPATH -name $TYPE -type f -delete
}

function cleanFolder() {
    DIRPATH=$1
    echo -e "deleting $BLACKLIST from $DIRPATH"
    for TYPE in $BLACKLIST; do
        cleanTypeFolder $DIRPATH "$TYPE"
    done
}

BLACKLIST=$BLACKLIST" *.aux *.dvi *.idx *.out *.log *.ind *.ilg"
export BLACKLIST

function job() {
    cleanFolder APAL
    cleanFolder BIOINF
    cleanFolder ROPR
    cleanFolder APS
    cleanFolder SAF
    cleanFolder MCOR
    cleanFolder TCOM
}

function handler() {
    COMMAND=$1
    if [ -z "$COMMAND" ]; then
        job
    else
        echo -e "imported $0 as bash library"
    fi
}

handler $1
