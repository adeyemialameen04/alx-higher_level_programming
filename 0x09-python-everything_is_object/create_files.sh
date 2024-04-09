#!/bin/bash

for ((i=0; i<=28; i++))
do
    touch "${i}-answer.txt"
done

echo "Text files created successfully."