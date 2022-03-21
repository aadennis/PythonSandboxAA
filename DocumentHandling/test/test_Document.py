from src.DocumentLine import DocumentLine
from src.Document import Document

class TestDocument:


    def test_get_line(self):

        documentLineSet = {}
        documentLineSet[0] = DocumentLine('First Header',0)
        documentLineSet[1] = DocumentLine('Header Two',1)
        documentLineSet[2] = DocumentLine('Some body and then some repeat all that until more than max for header',2)

        a = Document(documentLineSet)
        assert a.get_line_count() == 3
        assert a.get_line(0) == "First Header"

