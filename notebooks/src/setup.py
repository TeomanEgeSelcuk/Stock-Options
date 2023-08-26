import os
from setuptools import setup
from Cython.Build import cythonize
import numpy as np

def build_extension():
    # Define the name of the original .pyx file
    source_filename = "cython_numpy_test.pyx"
    
    # Extract the base name without extension
    base_name = os.path.splitext(source_filename)[0]

    # Configuration for building Cython extension
    setup(
        name=base_name,  # Extracted base name without extension
        ext_modules=cythonize(source_filename),  # Compile the original .pyx file
        include_dirs=[np.get_include()],  # Include NumPy headers
        language="c"
    )
    
    # Destination directory name
    destination_directory_name = "PYX Archives"
    
    # Get the current directory
    current_directory = os.getcwd()
    
    # Path to the source file
    source_path = os.path.join(current_directory, source_filename)
    
    # Path to the destination directory
    destination_directory_path = os.path.join(current_directory, destination_directory_name)
    
    # Create the destination directory if it doesn't exist
    if not os.path.exists(destination_directory_path):
        os.makedirs(destination_directory_path)
    
    # New file name with "PYX_" prefix
    new_filename = f"PYX_{source_filename}"
    
    # Path to the new file in the destination directory
    new_filepath = os.path.join(destination_directory_path, new_filename)
    
    # Rename and move the file
    os.rename(source_path, new_filepath)


if __name__ == "__main__":
    build_extension()
