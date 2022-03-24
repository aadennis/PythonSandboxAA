

import io
import tempfile
from src.DocumentLine import DocumentLine
from src.Document import Document

class TestDocument:
    def get_testset_1(self):
        dl = {}
        line = [
            'First Header', 
            'Header Two', 
            '',
            'Some body and then some repeat all that until more than max for header'
        ]
        
        dl[0] = DocumentLine(line[0],0)
        dl[1] = DocumentLine(line[1],1)
        dl[2] = DocumentLine(line[2],2)
        dl[3] = DocumentLine(line[3],3)
        return dl

    def get_testset_2(self):
        dl = {}
        line = [
            'setting the scene', # h1 => 1
            'the cow in the field',  # h2 => 1.1 
            'When I got to the other side of the gate, the bull had gone, but some cows were looking ' + 
                'scarily protective of their young. I edged along the corner of the sodden field, ' +
                'regretting the loss of a single wellington, both on grounds of comfort and safety. ' +
                ' Injury was very nearly added to insult when the pilot of the autogyro cocked his maxim ' +
                ' as he flew towards me. Happily, the machine gun failed after a single round, and the ' +
                ' tiny helicopter, pilot, gun and all, smashed into a sorry oak. It hadn\'t previously ' +
                ' been sorry, but now it sure was. The advantage to me was that bull, cows and calves were ' +
                ' thoroughly startled, and galumphed to the next field, leaving me to make a soggy exit ' +
                ' to relative safety as a pedestrian now limping, now stumbling along the A34.', #body 
            'A trip up the road', # h2 => 1.2
            ' I chose Launceston as my destination, trying and mostly failing to keep to a 30cm strip of ' +
            'pavement between an unending series of brick walls, and an unending stream of wing mirrors ' +
            ' on lorries, whistling past my ears at 5 second intervals.', #body
            'Jam today', #h1 => 2 (because next line is h2)
            'mouldy', #h2 => 2.1
            'The arse-end of a number of jars loosely fitting the description of "jam" sat unloved on the ' +
            'communal table of the B&B. Eat? A hint of green at the bottom of at least two of those made the ' +
            'decision for me. ', #body
            'Get out', #h2 => 2.2
            'I closed the front door quietly, and headed for The Shops, hopeful that I would find somewhere ' + 
            'to eat, which could boast at least 3, ok, 2 hygiene stars.', #body
            'Close encounters', #h1 => 3 (because next line is h2)
            'aliens', #h2 => 3.1
            'I have always felt it unwise to broadcast that we are here. Why would aliens show any less greed ' +
            'for resources protected by feeble competitors then we have, if that is a mark of "intelligence"? ' +
            'And so it proved. With the technology to kill, at will, the bulk of the human population, while ' +
            'preserving more useful resources, no-one escaped. Well, almost no-one. But romantic and ignorant ' +
            'hopes that a computer virus devised by Earth could somehow spike the guns of the invasion? ' +
            'I blame Independence Day. ', #body
            'Limited time', #h2 => 3.2
            'So like our own individual lives, which are over before we have had time to properly consider ' +
            'their meaning and value, Humanity will soon be gone, with no legacy worth preserving.' #body
        ]
        
        for i in range(0,len(line)):
            dl[i] = DocumentLine(line[i],i)
        
        return dl

    def test_lines_are_in_ok_order(self):
        # arrange
        documentLineSet = self.get_testset_1()

        # act
        doc = Document(documentLineSet)

        # assert
        assert doc.get_line_count() == 4
        assert doc.get_line(0) == 'First Header'
        assert doc.get_line(1) == 'Header Two'
        assert doc.get_line(2) == ''        
        assert doc.get_line(3) == 'Some body and then some repeat all that until more than max for header'
        
    def test_prefix_is_applied_to_header(self):
        documentLineSet = self.get_testset_1()
        
        for i in documentLineSet:
            documentLineSet[i].set_prefix()

        assert documentLineSet[0].get_line() == "1. First Header"
        assert documentLineSet[1].get_line() == "1. Header Two"
        assert documentLineSet[3].get_line() == 'Some body and then some repeat all that until more than max for header'
        
  
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

    """
    Checks that all headers are correctly numbered, and that body text is unchanged.
    """
    def test_number_all_headers(self):
        expected_formatted_doc = {0: '1. First Header', 1: '1.1 Header Two', 2: 'Some body and then some repeat all that until more than max for header'}
        documentLineSet = self.get_testset_1()
        doc = Document(documentLineSet)
        actual_formatted_doc = doc.number_all_headers()
        print(actual_formatted_doc)
        assert expected_formatted_doc == actual_formatted_doc

    def test_file_to_DocumentLineDict(self):
        source_file = "DocumentHandling/test/data/input/large_document.txt"
        documentLineSet = Document.file_to_DocumentLineDict(source_file)
        doc = Document(documentLineSet)
        assert 1 == 1

    def test_dict_values_to_file(self):
        target_file = "DocumentHandling/test/data/out.txt"
        my_dict = {}
        my_dict[0] = "some line"
        my_dict[1] = "two line"
        
        doc = Document(None)
        doc.dict_values_to_file(my_dict, target_file)

    # POC - This works on Python 3.9 on windows. still to test on Linux
    def test_stuff_with_temp_file(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            file_name = f"{tmpdir}/temp.txt"
            print(file_name)
            with (io.open(file_name,"w")) as fp:
                fp.writelines("do this now\n")
            file_name2 = f"{tmpdir}/temp.txt"
            print(file_name2)
            with (io.open(file_name2,"a")) as fp:
                fp.writelines("do this now2\n")
            with (io.open(file_name2,"r")) as fp:
                a = fp.readlines()
                print(a)
            
    """
    End to end test:
    Read a document which contains headings and body.
    The Rules are applied, resulting in numbered headers.
    For example:
    "Where do I begin?" => "1.2 Where do I begin?" 
    , making some assumptions about what precedes this header.
    """            
    def test_doc_on_file_formats_ok(self):
        source_file = "DocumentHandling/test/data/input/small_document.txt"
        #source_file = "c:/temp/b.txt"
        target_file = "c:/temp/a.txt"
        expected_content = ['1. First Header\n', '1.1 Header Two\n', 'Some body and then some repeat all that until more than max for header\n']
        documentLineSet = Document.file_to_DocumentLineDict(source_file)
        doc = Document(documentLineSet)
        a = doc.number_all_headers()
        doc.dict_values_to_file(a, target_file)
        with (io.open(target_file,'r')) as fp:
            actual_content = fp.readlines()
            assert expected_content == actual_content
