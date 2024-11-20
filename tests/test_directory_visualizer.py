import os
import unittest
from src.directory_visualizer import generate_markdown

class TestDirectoryVisualizer(unittest.TestCase):
    def test_generate_markdown(self):
        # Create a sample directory structure for testing
        test_dir = 'test_dir'
        os.mkdir(test_dir)
        os.mkdir(os.path.join(test_dir, 'subfolder'))
        with open(os.path.join(test_dir, 'file.txt'), 'w') as f:
            f.write("Test file")

        output_file = 'test_output.md'
        generate_markdown(test_dir, output_file)

        # Check if the markdown file is generated and contains the expected content
        with open(output_file, 'r') as f:
            content = f.read()
            self.assertIn('## subfolder', content)
            self.assertIn('- file.txt', content)

        # Clean up
        os.remove(os.path.join(test_dir, 'file.txt'))
        os.rmdir(os.path.join(test_dir, 'subfolder'))
        os.rmdir(test_dir)
        os.remove(output_file)

if __name__ == "__main__":
    unittest.main()
