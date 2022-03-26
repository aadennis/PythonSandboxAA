import os
from Document import Document
"""
    Instantiate and run Document for its
    only purpose right now: add headings to text file.
"""

def NumberHeadings():
    default_folder = "c:/temp"
    default_source_file = "source.txt"
    default_target_file = "target.txt"
    
    in_folder = input(f"Enter the folder for both source and target files (default [{default_folder}]): ")
    in_sourceDoc = input(f"Enter the name of the source text file (default [{default_source_file}]): ")
    in_targetDoc = input(f"Enter the full path of the target text file( default [{default_target_file}]): ")

    folder = default_folder if in_folder == '' else in_folder
    sourceDoc = default_source_file if in_sourceDoc == '' else in_sourceDoc
    targetDoc = default_target_file if in_targetDoc == '' else in_targetDoc
    
    source_path = os.path.join(folder, sourceDoc)
    target_path = os.path.join(folder, targetDoc)
    print(f"Source file location: [{source_path}]")
    print(f"Target file location: [{target_path}]")

    if not os.path.exists(source_path):
        print("*****************************************************************")
        print(f"Error: source file [{source_path}] does not exist, or cannot be reached. Exiting...")
        print("*****************************************************************")
        exit(1)
    
    documentLineSet = Document.file_to_DocumentLineDict(source_path)
    doc = Document(documentLineSet)
    docWithHeadings = doc.number_all_headers()
    doc.dict_values_to_file(docWithHeadings, target_path)
    print(f"File with numbered headings is at [{target_path}]")


if __name__ == '__main__':
    NumberHeadings()

