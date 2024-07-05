#!/bin/bash
# comment
curl -s -o /dev/null -w '%{http_code}' "$1"
