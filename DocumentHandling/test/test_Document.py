from src.DocumentLine import DocumentLine
from src.Document import Document

class TestDocument:


    def test_lines_are_in_ok_order(self):

        documentLineSet = {}
        line = ['First Header', 'Header Two', 'Some body and then some repeat all that until more than max for header']
        
        documentLineSet[0] = DocumentLine(line[0],0)
        documentLineSet[1] = DocumentLine(line[1],1)
        documentLineSet[2] = DocumentLine(line[2],2)

        a = Document(documentLineSet)
        assert a.get_line_count() == 3
        assert a.get_line(0) == line[0]
        assert a.get_line(1) == line[1]
        assert a.get_line(2) == line[2]
        

