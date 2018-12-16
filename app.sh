#!/bin/bash

while IFS='' read -r line || [[ -n "$line" ]]; do
    echo "$line"
    lighthouse $line --quiet --output json --output html
    sleep 10s
done < "$1"

DATE=$(date +"%Y-%m-%d")

mkdir reports/$DATE
mv *.html reports/$DATE/
mv *.json reports/$DATE/
