#!/bin/bash

for file in *.csv.pdf; do
    mv "$file" "$(basename "$file" .csv.pdf).pdf"
done
