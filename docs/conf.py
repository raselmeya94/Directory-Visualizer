# conf.py for Directory Visualizer documentation

import os
import sys
sys.path.insert(0, os.path.abspath('.'))

project = 'Directory Visualizer'
author = 'Md. Rasel Meya'
release = '0.1.0'

extensions = []

templates_path = ['_templates']
exclude_patterns = []

html_static_path = ['_static']
# Add a custom footer
html_context = {
    'footer': '© 2024 Rasel Meya. All rights reserved.',
}

# Optional: Modify the theme settings to ensure footer appears on every page
html_theme_options = {
    'footer': '© 2024 Rasel Meya. All rights reserved.',
}