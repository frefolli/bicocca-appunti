#!/bin/bash
source clean.sh "no-homo"

function handler() {
    cleanFolder $1
}

handler $1
