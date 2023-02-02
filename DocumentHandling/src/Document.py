import io
from DocumentLine import DocumentLine


"""
A Document is a collection of Document Lines
"""
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

    def get_title(self)        :
        return self.get_line(0).replace('\n', '')

    """
    Get the header level for the current line.
    If the index is zero, this is the Title: return 'T'
    If the current line is body text, return empty string, as this is not a header
    If the current line is a header, and the next line is also a header, return 'H1'
    If the current line is a header, and the next line is not a header, return 'H2'
    
    Context:
    The "header level" is one of 'H1', 'H2' or none ('').
    This is pre-pended to the text of the header. For example, 'The Heading' => 
    'H1. The Heading'.
    The document manager (class Document) processes the lines in a document 
    front to back (there is some argument for doing back to front, but I won't for now).,
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
    def get_header_level(self, current_line: DocumentLine, next_line: DocumentLine, index: int = None):
        if index == 0:
            return 'T' # title
        if current_line.is_header():
            if next_line.is_header():
                return 'H1'
            return 'H2'
        return ''
        
    
    """
    Set the header levels for the set of document lines.
    It is done at the level of Document not DocumentLine, because only
    Document knows the context.
    This results in header lines getting H1 or H2, Title getting T,
    and no change for text lines.
    """
    def set_header_levels(self):
        for i in self.documentline_set:
            current = self.documentline_set[i]
            if i+1 < len(self.documentline_set):
                next = self.documentline_set[i+1]
            current.set_header_level(self.get_header_level(current, next, i))

    """
    The source document is updated so that every header is numbered, based on the Rules.
    The first non-blank line is the Title. It does not get numbered.
    The non-header lines are unchanged, and the document returned with the updates.
    
    """
    def number_all_headers(self):
        self.set_header_levels()
        h1_ctr = 0
        h2_ctr = 0
        line_ctr = 0
        out_doc = {}
        first = True

        for key, value in self.documentline_set.items():
            current_line = f"{value.get_line()}"

            # ignore blank lines
            if current_line == '':
                continue

            if first: # first non-blank line must be Title
                first = False
                out_doc[line_ctr] = current_line
            elif value.get_header_level() == 'H1':
                h1_ctr += 1
                out_doc[line_ctr] = f"{h1_ctr}. {current_line}"
                h2_ctr = 0 # reset h2 counter
            elif value.get_header_level() == 'H2':
                h2_ctr += 1
                out_doc[line_ctr] = f"{h1_ctr}.{h2_ctr} {current_line}"
            else:
                out_doc[line_ctr] = current_line
            line_ctr += 1
        return out_doc

    """
    The document is transformed in a copy to the output_root.
    Title (first non-blank line in the source file) is used as the name of the file,
    and Title is returned to the caller.
    """    
    def save_number_headings_to_file(self, output_root):
        numbered_lines = self.number_all_headers()
        self.dict_values_to_file(numbered_lines, output_root)
        return self.get_title()


    """
    utility: read file into dictionary of Document Lines
    """
    def file_to_DocumentLineDict(source_file):
        line_ctr = 0
        dl_dict = {}
        with io.open(source_file, 'r') as f:
            for line in f:
                dl_dict[line_ctr] = DocumentLine(line, line_ctr)
                line_ctr += 1
        return dl_dict

    """
    Save the numbered headings and all other lines to file.
    Take the first line of the line dictionary
    , that is, the title, and make that the file name, with .txt appended.
    """
    def dict_values_to_file(self, source_dict, output_root):
        t = source_dict[0].replace('\n', '')
        target_file = f"{output_root}/{t}.txt"
        with open(target_file, 'w') as f:
            for i in source_dict:
                f.writelines(source_dict[i])

    """
    utility: If files are the same, return true, else return false.
    """
    def files_are_same(self, file1, file2):
        # return filecmp.cmp(file1, file2) - does not work for both Dos and Linux 
        # credit: https://stackoverflow.com/questions/23036576/python-compare-two-files-with-different-line-endings
        # https://www.aleksandrhovhannisyan.com/blog/crlf-vs-lf-normalizing-line-endings-in-git/
        
        l1 = l2 = True
        with open(file1, 'r') as f1, open(file2, 'r') as f2:
            while l1 and l2:
                l1 = f1.readline()
                l2 = f2.readline()
                if l1 != l2:
                    return False
        return True

