from setuptools import setup, find_packages

setup(
    name='directory_visualizer',
    version='0.1',
    packages=find_packages(where='src'),
    install_requires=[],  # Add any third-party libraries here
    entry_points={
        'console_scripts': [
            'directory-visualizer=src.directory_visualizer:main',  # Command to run the main function
        ],
    },
    # Additional metadata
    author="Rasel Meya",
    description="A tool to visualize directory structures as markdown and mermaid formats",
)
