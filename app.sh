#!/bin/bash

# Usage: $ ./app.sh frameworks.txt frameworks

while IFS='' read -r line || [[ -n "$line" ]]; do
    echo "$line"
    lighthouse $line --quiet --output json --output html
    sleep 10s
done < "$1"

DATE=$(date +"%Y-%m-%d")
SUB_FOLDER=$2

mkdir -p reports/$SUB_FOLDER/$DATE
mv ./*.html ./reports/$SUB_FOLDER/$DATE/
mv ./*.json ./reports/$SUB_FOLDER/$DATE/
