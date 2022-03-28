import os
from Document import Document
"""
    Instantiate and run Document for its
    only purpose right now: add headings to text file.
"""

def NumberHeadings():
    default_folder = "c:/temp"
    default_source_file = "source.txt"
    
    in_folder = input(f"Enter the folder for both source and target files (default [{default_folder}]): ")
    in_sourceDoc = input(f"Enter the name of the source text file (default [{default_source_file}]): ")

    folder = default_folder if in_folder == '' else in_folder
    sourceDoc = default_source_file if in_sourceDoc == '' else in_sourceDoc
    
    source_path = os.path.join(folder, sourceDoc)
    print(f"Source file location: [{source_path}]")

    if not os.path.exists(source_path):
        print("*****************************************************************")
        print(f"Error: source file [{source_path}] does not exist, or cannot be reached. Exiting...")
        print("*****************************************************************")
        exit(1)
    
    lines = Document.file_to_DocumentLineDict(source_path)
    doc = Document(lines)
    title = doc.save_number_headings_to_file(folder)
    target_path = f"{folder}/{title}.txt"
    print(f"target file location: [{target_path}]")

if __name__ == '__main__':
    NumberHeadings()

