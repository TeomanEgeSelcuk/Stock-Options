import sys
import os

# Get the current directory of the main script
current_directory = os.path.dirname(os.path.abspath(__file__))

# Add the project's root directory to the Python path
project_root = os.path.abspath(os.path.join(current_directory, ".."))
sys.path.insert(0, project_root)
