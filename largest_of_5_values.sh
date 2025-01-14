#!/bin/bash -eu
# Write your code here
# You must ONLY print the result to STDOUT

# Read input from STDIN, filter for "DATA" lines, and extract the second field
res=$(grep '^DATA' | awk -F',' '{print $2}' | tail -n 5 | sort -nr | head -n 1)

# Print the largest value
echo "$res"
