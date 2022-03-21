"""
A Document is a collection of Document Lines
"""

class Document():
    """
    A Document is instantiated by passing it an array of Document Lines (cf).
    """   
    def __init__(self, documentline_set):
        self.documentline_set = documentline_set
        
    def get_line(self, index):
        return self.documentline_set[index].get_line()

    def get_line_count(self):
        return len(self.documentline_set)