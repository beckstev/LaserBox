#!/bin/bash
for f in *.root;
do  
filename="${f%.*}"
height="${filename%_mm*}"
echo $filename
root -q 'testfit.c("'$filename'",'$height')'
done
