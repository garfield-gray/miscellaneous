#!/bin/bash

# Go to the directory containing the .kml files
cd kmlfiles/

# Loop over each .kml file
for file in *.kml; do
  # Use regex to extract the base 10-digit number at the start
  if [[ "$file" =~ ^([0-9]{10}) ]]; then
    base="${BASH_REMATCH[1]}"
    echo "${BASH_REMATCH[1]}"

    # Make directory named after the base if it doesn't exist
    mkdir -p "$base"
    
    # Move the file into the correct folder
    # mv "$file" "$base/"
  fi
done

echo "Organized all .kml files correctly."

