#!/bin/bash

function cleanFolder() {
    find $1 -name "*.aux" -type f -delete
	find $1 -name "*.dvi" -type f -delete
	find $1 -name "*.idx" -type f -delete
	find $1 -name "*.out" -type f -delete
	find $1 -name "*.log" -type f -delete
	find $1 -name "*.ind" -type f -delete
	find $1 -name "*.ilg" -type f -delete
}

cleanFolder APAL
cleanFolder BIOINF
cleanFolder ROPR
