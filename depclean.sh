#!/bin/bash
source clean.sh "no-homo"

BLACKLIST=$BLACKLIST" *.pdf Makefile"
export BLACKLIST

function handler() {
    COMMAND=$1
    if [ -z "$COMMAND" ]; then
        job
    fi
}

handler $1