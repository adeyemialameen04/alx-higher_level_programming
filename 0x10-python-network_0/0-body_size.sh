#!/bin/bash

# Check if the URL is provided as an argument
if [ $# -eq 0 ]; then
	echo "Usage: $0 <URL>"
	exit 1
fi

URL=$1

# Send a request to the URL and store the response body size in bytes
size=$(curl -s -o /dev/null -w '%{size_download}' "$URL")

# Display the size
echo $size
