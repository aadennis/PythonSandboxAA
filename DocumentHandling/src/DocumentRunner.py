from Document import Document
"""
    Instantiate and run Document for its
    only purpose right now: add headings to text file.
"""

def NumberHeadings():
    sourceDoc = input("Enter the full path of the source text file: ")
    targetDoc = input("Enter the full path of the target text file: ")
    
    documentLineSet = Document.file_to_DocumentLineDict(sourceDoc)
    doc = Document(documentLineSet)
    docWithHeadings = doc.number_all_headers()
    doc.dict_values_to_file(docWithHeadings, targetDoc)


if __name__ == '__main__':
    NumberHeadings()

