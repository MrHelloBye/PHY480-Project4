#!/bin/bash

counter=0

for file in *.pdf; do
    convert -density 400 "$file" "../images/${file}.png"
done
