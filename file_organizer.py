import os
from shutil import move
from collections import defaultdict

def organize_downloads(source_path: str, target_path: str) -> None:
    """
    Organize files from the source directory by their file extensions 
    and move them into categorized folders in the target directory.

    Parameters:
    - source_path (str): The path to the source directory where files are located.
    - target_path (str): The path to the target directory where files will be moved.

    The function creates subdirectories in the target directory based on the file extensions.
    Files without extensions will be placed in a folder named 'other'.
    """
    
    # List all files in the source directory
    files = [f for f in os.listdir(source_path) if os.path.isfile(os.path.join(source_path, f))]
    
    # Dictionary to store files categorized by their extensions
    file_dict = defaultdict(list)

    # Categorize files by their extensions
    for file in files:
        # Extract the file extension and convert it to lowercase
        extension = os.path.splitext(file)[1].lower()
        if extension:
            # If a file has an extension, add it to the corresponding category
            file_dict[extension].append(file)
        else:
            # If a file doesn't have an extension, categorize it as 'other'
            file_dict['other'].append(file)

    # Ensure the target directory exists; if not, create it
    if not os.path.exists(target_path):
        os.mkdir(target_path)
        print(f"Created directory: {target_path}")

    # Move files into folders based on their extension
    for ext, files in file_dict.items():
        # Create a directory for each file extension (e.g., .txt -> txt folder)
        directory = os.path.join(target_path, ext.strip('.'))
        if not os.path.exists(directory):
            os.mkdir(directory)
            print(f"Created directory for {ext}: {directory}")
        
        # Sort files alphabetically before moving (optional)
        files.sort()
        
        # Move each file to its respective folder
        for file in files:
            dest = os.path.join(directory, file)
            move(os.path.join(source_path, file), dest)
            print(f"Moved {file} to {dest}")

# Define source and target paths
# Example of how the path most be defined
source_path = "C:\\Users\\ericg\\Downloads"  # Path where the files are located
target_path = "C:\\Users\\ericg\\Desktop\\Files"  # Path where files will be moved and organized

# Call the function to organize files
organize_downloads(source_path, target_path)
