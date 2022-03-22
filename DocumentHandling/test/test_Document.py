from src.DocumentLine import DocumentLine
from src.Document import Document

class TestDocument:
    def get_testset_1(self):
        dl = {}
        line = [
            'First Header', 
            'Header Two', 
            'Some body and then some repeat all that until more than max for header'
        ]
        
        dl[0] = DocumentLine(line[0],0)
        dl[1] = DocumentLine(line[1],1)
        dl[2] = DocumentLine(line[2],2)
        return dl

    def test_lines_are_in_ok_order(self):
        # arrange
        documentLineSet = self.get_testset_1()

        # act
        doc = Document(documentLineSet)

        # assert
        assert doc.get_line_count() == 3
        assert doc.get_line(0) == 'First Header'
        assert doc.get_line(1) == 'Header Two'
        assert doc.get_line(2) == 'Some body and then some repeat all that until more than max for header'
        
    def test_prefix_is_applied_to_header(self):
        documentLineSet = self.get_testset_1()
        
        for i in documentLineSet:
            documentLineSet[i].set_prefix()

        assert documentLineSet[0].get_line() == "1. First Header"
        assert documentLineSet[1].get_line() == "1. Header Two"
        assert documentLineSet[2].get_line() == 'Some body and then some repeat all that until more than max for header'
        
  
    def test_set_header_levels(self):

        # arrange
        documentLineSet = self.get_testset_1()
        doc = Document(documentLineSet)

        # act
        doc.set_header_levels()        

        # assert
        assert documentLineSet[0].get_header_level() == 'H1'
        assert documentLineSet[1].get_header_level() == 'H2'
        assert documentLineSet[2].get_header_level() == ''  
