#!/bin/bash

#Checking for argument
if [ $# -eq 0 ]; then
    echo "Usage: $0 <folder_name>"
    exit 1
fi

# Assign the first argument to a variable
FOLDER_NAME=$1

# Create the directory
mkdir -p "$FOLDER_NAME"

# Navigate to the directory
cd "$FOLDER_NAME"

# Create a text file and a Python file inside the directory
touch question.txt solution.py

echo "Folder '$FOLDER_NAME' created BOOYAKASHA"

