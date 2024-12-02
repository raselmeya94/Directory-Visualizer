.. cli section
Command Line Interface (CLI)
=============================

Directory Visualizer provides a simple command-line interface to visualize directory structures.

Basic Command
--------------

To generate a directory structure in Markdown format:

.. code-block:: bash

    directory-visualizer -p <path_to_directory> -f markdown

Generate Mermaid Diagram
-------------------------

To generate a Mermaid diagram (embedded in Markdown):

.. code-block:: bash

    directory-visualizer -p <path_to_directory> -f mermaid

Set Directory Traversal Depth
------------------------------

You can limit the depth of directory traversal using the `--depth` option.

.. code-block:: bash

    directory-visualizer -p <path_to_directory> -f markdown --depth 2

Output to Specific File
------------------------

Use the `-o` option to specify a custom output file name:

.. code-block:: bash

    directory-visualizer -p <path_to_directory> -f markdown -o custom_output.md