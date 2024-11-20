# About Directory-Visualizer

**Directory-Visualizer** is a tool designed to help users visualize their directory structure in a clean and easy-to-understand flowchart. It takes a directory path as input, traverses the directory structure, and generates a diagram of the folder and file hierarchy, making it simple to explore large and complex file systems.

## Features

- **Recursive Directory Traversal**: Automatically explores all subdirectories within the provided directory.
- **Mermaid Diagram Generation**: Converts the directory structure into a **Mermaid.js** flowchart syntax.
- **SVG Image Export**: Converts the Mermaid diagram into an SVG image, which can be used for documentation or visual analysis.
- **Customizable**: Easily extendable to support different file formats and output types.

## How It Works

1. **Input**: Provide the path to a directory on your local machine.
2. **Traversal**: The tool recursively scans the directory and all its subdirectories.
3. **Mermaid Syntax**: Generates a Mermaid flowchart code representing the directory structure.
4. **Output**: The Mermaid diagram can be saved as:
    - A **Markdown** file.
    - An **SVG image** for easy viewing and sharing.

## Installation

### Prerequisites
Ensure you have the following installed:
- **Python 3.6+** (for running the script)
- **Mermaid** (for rendering flowcharts)

### Steps to Install

1. Clone the repository:
```bash
git clone https://github.com/yourusername/directory-visualizer.git
```
###Navigate into the directory:

```bash

cd directory-visualizer
```

### Install the required dependencies by running:

```bash
pip install -r requirements.txt
```
After installation, navigate to the src folder:

```bash
cd src
```
Now, run the tool using the following command:

```bash
python directory_visualizer.py
```
## Usage
### Step-by-Step Usage
#### Input: After running the directory_visualizer.py script, it will prompt you for the following inputs:

#### Directory Path: Enter the path to the directory you want to visualize.
#### Output Format: Choose between markdown or mermaid as the output format.
#### Generate the Diagram: The script will generate the directory structure in the chosen format and save it to a file.

Example:
Run the script in the src folder:

```bash
python directory_visualizer.py
```
Enter the directory path when prompted:

```bash
Enter the directory path: /path/to/your/directory
```
Choose the format for the output file:

```bash
Enter the format (markdown/mermaid): markdown
```
The tool will generate a directory structure in the desired format and save it to a file.
