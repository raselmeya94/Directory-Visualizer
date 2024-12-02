#!/bin/bash

# Define base directory
BASE_DIR="docs"

# Define structure as folder and files array
FOLDERS=("getting_started" "usages" "python_code_setup" "command_line_interface" "contributings" "notes")
FILES=(
    "getting_started:welcome.rst installing.rst"
    "usages:default.rst custom.rst"
    "python_code_setup:inside_code.rst"
    "command_line_interface:cli.rst"
    "contributings:contributors.rst"
    "notes:changelog.rst"
)

# Create base directory
if [ ! -d "$BASE_DIR" ]; then
    mkdir -p "$BASE_DIR"
    echo "Created base directory: $BASE_DIR"
else
    echo "Base directory already exists: $BASE_DIR"
fi

# Create index.rst
INDEX_FILE="$BASE_DIR/index.rst"
if [ ! -f "$INDEX_FILE" ]; then
    echo ".. Directory Visualizer documentation index" > "$INDEX_FILE"
    echo "Created: $INDEX_FILE"
else
    echo "Index file already exists: $INDEX_FILE"
fi

# Loop through folders and files
for entry in "${FILES[@]}"; do
    FOLDER="${entry%%:*}"
    FILES_LIST="${entry#*:}"

    FOLDER_PATH="$BASE_DIR/$FOLDER"
    mkdir -p "$FOLDER_PATH"
    echo "Created directory: $FOLDER_PATH"
    
    for file in $FILES_LIST; do
        FILE_PATH="$FOLDER_PATH/$file"
        if [ ! -f "$FILE_PATH" ]; then
            echo ".. ${file%.rst} section" > "$FILE_PATH"
            echo "Created: $FILE_PATH"
        else
            echo "File already exists: $FILE_PATH"
        fi
    done
done

echo "Documentation structure generated successfully."
