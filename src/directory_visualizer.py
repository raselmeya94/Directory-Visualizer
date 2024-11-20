
import os

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
            name = name.replace(char, '' + char)
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
            name = name.replace(char, '' + char)
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
    
def main():
    """
    Main function to handle user input and invoke the directory structure generation.
    """
    directory_path = input("Enter the directory path: ")
    format = input("Enter the format (markdown/mermaid): ").lower()
    if not os.path.isdir(directory_path):
        print("The specified path is not a valid directory.")
        return
    
    if format=="markdown":
    # Specify the output markdown file
        output_markdown = "output/directory_structure_md.md"
        generate_markdown(directory_path, output_markdown)
        print(f"Directory structure has been saved to {output_markdown}")
    else:
        output_mermaid = "output/directory_structure_mmd.md"
        generate_mermaid(directory_path, output_mermaid)
        print(f"Directory structure has been saved in Mermaid format to {output_mermaid}")


if __name__ == "__main__":
    main()
