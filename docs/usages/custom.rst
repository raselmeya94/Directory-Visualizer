.. custom section
Usage: Custom
==============

To generate a Mermaid diagram (embedded in Markdown):

.. code-block:: bash

    directory-visualizer -p <path_to_directory> -f mermaid

This will create a `directory_structure.md` file with the Mermaid diagram.

To generate a raw `.mmd` file, use the `--raw-mermaid` flag:

.. code-block:: bash

    directory-visualizer -p <path_to_directory> -f mermaid --raw-mermaid

This will create a `directory_structure.mmd` file.
