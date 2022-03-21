import io


"""
  Simple Document class
"""
class DocumentLine():
    """
    Categorises a line in a document - Heading1, Heading2, etc
    """
    MAX_WORDS_FOR_HEADER = 10 # any more, and it is body text

    def __init__(self, line, line_index):
        """
        Ctor: 
        line - the current line - mandatory
        line_index - position of current line in file - mandatory
        """
        self.line = line 
        self.line_index = line_index 

    def is_valid_line(self):
        """
        First strip out white-space.
        If the line then has >= 1 characters, true, else false
        
        """
        if self.get_char_count() == 0:
            return False
        return True

    def is_header(self):
        wc = self.get_word_count()
        if wc == 0:
            return False
        if wc > self.MAX_WORDS_FOR_HEADER:
            return False
        return True

    def get_paragraph_type(self):
        if not self.is_valid_line():
            return None
        if self.is_header():
            return "Header"
        return "Body"

    def get_word_count(self):
        if self.get_char_count() == 0:
            return 0
        return len(self.line.strip().split(' '))

    def get_char_count(self):
        """
        Strip out white-space.
        Return the character count after that
        """
        line_no_ws = self.line.translate(str.maketrans('', '', ' \n\t\r'))
        return len(line_no_ws)



    

