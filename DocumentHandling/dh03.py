import io


"""
  Simple Document class
"""
class DocumentLine():
    """
    Categorises a line in a document - Heading1, Heading2, etc
    """
    def __init__(self, line, line_index):
        """
        Todo
        """
        self.line = line # the current line
        self.line_index = line_index # position of current line in file
        self.valid = self.is_valid_line() # e.g. zero content, when w-space excluded
        self.header = self.is_header() # default
        self.paragraph_type = self.set_paragraph_type() # default
        self.word_count = self.set_word_count()

    def is_valid_line(self):
        return False

    def is_header(self):
        return False

    def set_paragraph_type(self):
        return "Body"

    def set_word_count(self):
        return 42



    

