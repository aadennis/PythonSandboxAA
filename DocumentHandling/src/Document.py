"""
A Document is a collection of Document Lines
"""

from src.DocumentLine import DocumentLine


class Document():
    """
    A Document manages Document Lines (cf). It is instantiated by passing it an array of Document Lines.
    """   
    def __init__(self, documentline_set: dict):
        self.documentline_set = documentline_set
        
    def get_line(self, index):
        return self.documentline_set[index].get_line()

    def get_line_count(self):
        return len(self.documentline_set)

    """
    If the line is a header then set the header type, which will be 'H1.' or 'H2.',
    to be pre-pended to the text of the header. For example, 'The Heading' => 
    'H1. The Heading'.
    For context, the document manager (class Document) processes the lines in a document 
    front to back (there is some argument for doing back to front, but I won't for now), and
    thus: 
    If the current line is a header
        if current line+1 is a header (assumption that no body text comes between an H1 and and H2), 
            then the current line is H1.
        else the current line is H2
    Look at this example:
        Line - header characteristics - 1
        Line - body characteristics - 2
        Line - header characteristics - 3
    In fact if this is the top of a file, this combination is not allowed, because the rule says no
    body between a H1 and H2.
    However, if the middle of a file, it would be allowed, because 
    a) line 1 and line 3 could be both be H2 or
    b)  line 1 could be H2 and line 3 H1 (but then a line 4 would have to be H2, due to the rule).
    This method cannot be part of the DocumentLine class because it needs to know about another line to
    answer the question. Hence it is part of the Document class.
    """
    def get_header_level(self, current_line: DocumentLine, next_line: DocumentLine):
        if current_line.is_header():
            if next_line.is_header():
                return 'H1'
            return 'H2'
        return ''
        
    
    def set_header_levels(self):
        doc = Document(self.documentline_set)

        for i in self.documentline_set:
            current = self.documentline_set[i]
            if i+1 < len(self.documentline_set):
                next = self.documentline_set[i+1]
            current.set_header_level(doc.get_header_level(current, next))

    """
    Return the document, numbering every header, and leaving the non-header
    lines as-is
    """
    def number_all_headers(self):
        self.set_header_levels()
        h1_ctr = 0
        h2_ctr = 0
        line_ctr = 0
        out_doc = {}

        for key, value in self.documentline_set.items():
            if value.get_header_level() == 'H1':
                h1_ctr += 1
                out_doc[line_ctr] = {line_ctr: f"{h1_ctr}. {value.get_line()}\n"}
                h2_ctr = 0 # reset h2 counter
            elif value.get_header_level() == 'H2':
                h2_ctr += 1
                out_doc[line_ctr] = {line_ctr: f"{h1_ctr}.{h2_ctr} {value.get_line()}\n"}
            else:
                out_doc[line_ctr] = {line_ctr: f"{value.get_line()}\n"}
            line_ctr += 1
        return out_doc
