#!/bin/bash

# Function to check if the shebang line exists
check_shebang() {
    file="$1"
    shebang="#!/usr/bin/python3"
    head -n 1 "$file" | grep -q "$shebang"
}

# Function to add the shebang line
add_shebang() {
    file="$1"
    shebang="#!/usr/bin/python3"
    if ! check_shebang "$file"; then
        printf "%s\n" "$shebang" | cat - "$file" > temp && mv temp "$file"
    else
        echo "Shebang line already exists in $file"
    fi
}

# Check if a file is provided as an argument
if [ "$#" -eq 0 ]; then
    echo "Usage: $0 <filename>"
    exit 1
fi

# Loop through each file provided as an argument
for file in "$@"; do
    if [ -f "$file" ]; then
        add_shebang "$file"
    else
        echo "File $file does not exist"
    fi
done