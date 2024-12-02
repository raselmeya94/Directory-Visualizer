.. inside_code section
Python Code Setup
==================

If you want to use Directory Visualizer programmatically, you can import the functions into your Python code. Here's an example:

.. code-block:: python
   :linenos:

   from directory_visualizer.core.functions import generate_markdown, generate_mermaid

   # Example usage:
   directory = "/path/to/your/directory"
   format = "markdown"  # or "mermaid"
   depth = 2  # Optional depth argument

   # Generate content programmatically
   if format == "markdown":
       content = generate_markdown(directory, depth)
   else:
       content = generate_mermaid(directory, depth)

   print(content)
