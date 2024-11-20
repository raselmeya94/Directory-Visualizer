import os

def validate_directory(directory):
    """
    Validates if the given path is a valid directory.
    
    :param directory: Path to the directory to validate.
    :return: Boolean indicating if the path is a valid directory.
    """
    return os.path.isdir(directory)
