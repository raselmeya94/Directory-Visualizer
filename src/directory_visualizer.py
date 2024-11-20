
# import os
# import argparse
# def generate_markdown(directory, markdown_file):
#     """
#     Traverses the given directory and generates a markdown file listing its structure.
    
#     :param directory: Path to the directory to visualize.
#     :param markdown_file: The file object to write the generated markdown content.
#     """
#     def escape_markdown(name):
#         """
#         Escapes special markdown characters to prevent them from being interpreted as markdown.
        
#         :param name: The directory or file name.
#         :return: The escaped name as a string.
#         """
#         special_chars = ['#', '*', '!', '[', ']', '(', ')', '{', '}', '<', '>', '`']
#         for char in special_chars:
#             name = name.replace(char, '' + char)
#         return name

#     def traverse_directory(path, level=1, markdown_file=None):
#         """
#         Recursively traverses the directory and appends its structure to the markdown file.
        
#         :param path: Path of the directory or file.
#         :param level: Indentation level for directory nesting.
#         :param markdown_file: The file object to write the generated markdown content.
#         """
#         indent = "  " * (level - 1)  # Indentation for directories and files
#         if os.path.isdir(path):
#             # Use a dynamic number of `#` based on the level of the directory
#             markdown_file.write(f"{indent}- {'#' * min(level, 5)} {escape_markdown(os.path.basename(path))}\n")
#             # Traverse the directory and its contents
#             for item in os.listdir(path):
#                 traverse_directory(os.path.join(path, item), level + 1, markdown_file)
#         else:
#             # Only files should be listed with a bullet point
#             markdown_file.write(f"{indent}- {escape_markdown(os.path.basename(path))}\n")

#     # Open the markdown file for writing
#     with open(markdown_file, 'w') as md_file:
#         md_file.write(f"# Directory Structure of {directory}\n\n")
#         traverse_directory(directory, 1, md_file)


# def generate_mermaid(directory, mermaid_file):
#     """
#     Traverses the given directory and generates a Mermaid flowchart for the directory structure.
    
#     :param directory: Path to the directory to visualize.
#     :param mermaid_file: The file object to write the generated Mermaid content.
#     """
#     def escape_mermaid(name):
#         """
#         Escapes special characters for Mermaid syntax to prevent rendering issues.
        
#         :param name: The directory or file name.
#         :return: The escaped name as a string.
#         """
#         special_chars = ['(', ')', '{', '}', '[', ']', '#', '.', ',', ';']
#         for char in special_chars:
#             name = name.replace(char, '' + char)
#         return name
    
#     def regenerate_filename(name):
#         """
#         Regenerates the filename by replacing spaces with underscores and ensuring compatibility
#         with Mermaid syntax.

#         :param name: The original file name.
#         :return: The regenerated file name.
#         """
#         return name.replace(" ", "_").replace(".", "_").replace("-", "_")
    
#     def traverse_directory(path, level=1, mermaid_file=None, parent_dir=None):
#         """
#         Recursively traverses the directory and appends its structure to the Mermaid file.
        
#         :param path: Path of the directory or file.
#         :param level: Indentation level for directory nesting.
#         :param mermaid_file: The file object to write the generated Mermaid content.
#         :param parent_dir: The parent directory node (used for linking).
#         """
#         indent = "  " * level  # Indentation for directories and files
#         node_name = escape_mermaid(os.path.basename(path))

#         if os.path.isdir(path):
#             # For directories, we add a node
#             dir_name = regenerate_filename(node_name)
#             if parent_dir:  # If there's a parent directory, link it
#                 mermaid_file.write(f"{indent}{parent_dir} --> {dir_name}[( {node_name} )]\n")
#             else:
#                 mermaid_file.write(f"{indent}{dir_name}[( {node_name} )]\n")
            
#             # Traverse the directory and its contents
#             for item in os.listdir(path):
#                 item_path = os.path.join(path, item)
#                 traverse_directory(item_path, level + 1, mermaid_file, dir_name)
#         else:
#             # For files, we add a link to the parent directory node
#             file_name = regenerate_filename(node_name)
#             mermaid_file.write(f"{indent}{parent_dir} --> {file_name}[( {node_name} )]\n")

#     # Start the Mermaid diagram
#     with open(mermaid_file, 'w') as mermaid:
#         mermaid.write("```mermaid\n")
#         mermaid.write("graph TD\n")  # Top-down flowchart
#         traverse_directory(directory, 1, mermaid)
#         mermaid.write("```")
    


# def run_interactively():
#     """
#     Function to handle interactive input for running the script.
#     """
#     directory_path = input("Enter the directory path: ")
#     while not os.path.isdir(directory_path):
#         print(f"The specified path '{directory_path}' is not a valid directory.")
#         directory_path = input("Please enter a valid directory path: ")

#     output_format = input("Enter the format (markdown/mermaid): ").lower()
#     while output_format not in ['markdown', 'mermaid']:
#         print("Invalid format. Please choose 'markdown' or 'mermaid'.")
#         output_format = input("Enter the format (markdown/mermaid): ").lower()

#     output_file = input("Enter the output file path to save the visualization: ")

#     if output_format == 'markdown':
#         generate_markdown(directory_path, output_file)
#         print(f"Directory structure has been saved in markdown format to {output_file}")
#     else:
#         generate_mermaid(directory_path, output_file)
#         print(f"Directory structure has been saved in Mermaid format to {output_file}")

# def main():
#      """
#     Main function to handle user input via command line arguments or interactive input.
#     """
#     parser = argparse.ArgumentParser(description="Directory Visualizer CLI")
#     parser.add_argument('-p', '--path', help="Path to the directory you want to visualize")
#     parser.add_argument('-f', '--format', choices=['markdown', 'mermaid'], help="The format for the output (markdown or mermaid)")
#     parser.add_argument('-o', '--output', help="The output file path to save the visualization")

#     args = parser.parse_args()

#     # If command line arguments are provided, use them
#     if args.path and args.format and args.output:
#         directory_path = args.path
#         output_format = args.format
#         output_file = args.output

#         if not os.path.isdir(directory_path):
#             print(f"The specified path '{directory_path}' is not a valid directory.")
#             return

#         if output_format == 'markdown':
#             generate_markdown(directory_path, output_file)
#             print(f"Directory structure has been saved in markdown format to {output_file}")
#         else:
#             generate_mermaid(directory_path, output_file)
#             print(f"Directory structure has been saved in Mermaid format to {output_file}")
#     else:
#         # Otherwise, run interactively
#         run_interactively()

# if __name__ == "__main__":
#     main()


import os
import argparse

def generate_markdown(directory, markdown_file):
    """
    Traverses the given directory and generates a markdown file listing its structure.
    
    :param directory: Path to the directory to visualize.
    :param markdown_file: The file object to write the generated markdown content.
    """
    def escape_markdown(name):
        """
        Escapes special markdown characters to prevent them from being interpreted as markdown.
        
        :param name: The directory or file name.
        :return: The escaped name as a string.
        """
        special_chars = ['#', '*', '!', '[', ']', '(', ')', '{', '}', '<', '>', '`']
        for char in special_chars:
            name = name.replace(char, f"\\{char}")
        return name

    def traverse_directory(path, level=1, markdown_file=None):
        """
        Recursively traverses the directory and appends its structure to the markdown file.
        
        :param path: Path of the directory or file.
        :param level: Indentation level for directory nesting.
        :param markdown_file: The file object to write the generated markdown content.
        """
        indent = "  " * (level - 1)  # Indentation for directories and files
        if os.path.isdir(path):
            # Use a dynamic number of `#` based on the level of the directory
            markdown_file.write(f"{indent}- {'#' * min(level, 5)} {escape_markdown(os.path.basename(path))}\n")
            # Traverse the directory and its contents
            for item in os.listdir(path):
                traverse_directory(os.path.join(path, item), level + 1, markdown_file)
        else:
            # Only files should be listed with a bullet point
            markdown_file.write(f"{indent}- {escape_markdown(os.path.basename(path))}\n")

    # Open the markdown file for writing
    with open(markdown_file, 'w') as md_file:
        md_file.write(f"# Directory Structure of {directory}\n\n")
        traverse_directory(directory, 1, md_file)


def generate_mermaid(directory, mermaid_file):
    """
    Traverses the given directory and generates a Mermaid flowchart for the directory structure.
    
    :param directory: Path to the directory to visualize.
    :param mermaid_file: The file object to write the generated Mermaid content.
    """
    def escape_mermaid(name):
        """
        Escapes special characters for Mermaid syntax to prevent rendering issues.
        
        :param name: The directory or file name.
        :return: The escaped name as a string.
        """
        special_chars = ['(', ')', '{', '}', '[', ']', '#', '.', ',', ';']
        for char in special_chars:
            name = name.replace(char, f"\\{char}")
        return name
    
    def regenerate_filename(name):
        """
        Regenerates the filename by replacing spaces with underscores and ensuring compatibility
        with Mermaid syntax.

        :param name: The original file name.
        :return: The regenerated file name.
        """
        return name.replace(" ", "_").replace(".", "_").replace("-", "_")
    
    def traverse_directory(path, level=1, mermaid_file=None, parent_dir=None):
        """
        Recursively traverses the directory and appends its structure to the Mermaid file.
        
        :param path: Path of the directory or file.
        :param level: Indentation level for directory nesting.
        :param mermaid_file: The file object to write the generated Mermaid content.
        :param parent_dir: The parent directory node (used for linking).
        """
        indent = "  " * level  # Indentation for directories and files
        node_name = escape_mermaid(os.path.basename(path))

        if os.path.isdir(path):
            # For directories, we add a node
            dir_name = regenerate_filename(node_name)
            if parent_dir:  # If there's a parent directory, link it
                mermaid_file.write(f"{indent}{parent_dir} --> {dir_name}[( {node_name} )]\n")
            else:
                mermaid_file.write(f"{indent}{dir_name}[( {node_name} )]\n")
            
            # Traverse the directory and its contents
            for item in os.listdir(path):
                item_path = os.path.join(path, item)
                traverse_directory(item_path, level + 1, mermaid_file, dir_name)
        else:
            # For files, we add a link to the parent directory node
            file_name = regenerate_filename(node_name)
            mermaid_file.write(f"{indent}{parent_dir} --> {file_name}[( {node_name} )]\n")

    # Start the Mermaid diagram
    with open(mermaid_file, 'w') as mermaid:
        mermaid.write("```mermaid\n")
        mermaid.write("graph TD\n")  # Top-down flowchart
        traverse_directory(directory, 1, mermaid)
        mermaid.write("```")
    


def run_interactively():
    """
    Function to handle interactive input for running the script.
    """
    directory_path = input("Enter the directory path: ")
    while not os.path.isdir(directory_path):
        print(f"The specified path '{directory_path}' is not a valid directory.")
        directory_path = input("Please enter a valid directory path: ")

    output_format = input("Enter the format (markdown/mermaid): ").lower()
    while output_format not in ['markdown', 'mermaid']:
        print("Invalid format. Please choose 'markdown' or 'mermaid'.")
        output_format = input("Enter the format (markdown/mermaid): ").lower()

    output_file = input("Enter the output file path to save the visualization: ")

    if output_format == 'markdown':
        generate_markdown(directory_path, output_file)
        print(f"Directory structure has been saved in markdown format to {output_file}")
    else:
        generate_mermaid(directory_path, output_file)
        print(f"Directory structure has been saved in Mermaid format to {output_file}")

def main():
    """
    Main function to handle user input via command line arguments or interactive input.
    """
    parser = argparse.ArgumentParser(description="Directory Visualizer CLI")
    parser.add_argument('-p', '--path', help="Path to the directory you want to visualize")
    parser.add_argument('-f', '--format', choices=['markdown', 'mermaid'], help="The format for the output (markdown or mermaid)")
    parser.add_argument('-o', '--output', help="The output file path to save the visualization")

    args = parser.parse_args()

    # If command line arguments are provided, use them
    if args.path and args.format and args.output:
        directory_path = args.path
        output_format = args.format
        output_file = args.output

        if not os.path.isdir(directory_path):
            print(f"The specified path '{directory_path}' is not a valid directory.")
            return

        if output_format == 'markdown':
            generate_markdown(directory_path, output_file)
            print(f"Directory structure has been saved in markdown format to {output_file}")
        else:
            generate_mermaid(directory_path, output_file)
            print(f"Directory structure has been saved in Mermaid format to {output_file}")
    else:
        # Otherwise, run interactively
        run_interactively()

if __name__ == "__main__":
    main()
