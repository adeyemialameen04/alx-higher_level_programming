#!/bin/bash
# comment
curl -s "$1" -X POST -H "Content-Type: application/json" -d "$(cat "$2")"
