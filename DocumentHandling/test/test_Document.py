import pytest
import io
import tempfile
from src.DocumentLine import DocumentLine
from src.Document import Document

class TestDocument:
    def get_testset_1(self):
        dl = {}
        line = [
            'The Title',
            '',
            'First Header',
            'Header Two',
            '',
            'Some body and then some repeat all that until more than max for header',
            '2 First Header',
            '2 Header Two',
            '',
            '2 Some body and then some repeat all that until more than max for header',
            
        ]

        for i in range(0, len(line)):
            dl[i] = DocumentLine(line[i], i)
        return dl

    def get_testset_2(self):
        dl = {}
        line = [
            'setting the scene',  # h1 => 1
            'the cow in the field',  # h2 => 1.1
            'When I got to the other side of the gate, the bull had gone, but some cows were looking ' +
            'scarily protective of their young. I edged along the corner of the sodden field, ' +
            'regretting the loss of a single wellington, both on grounds of comfort and safety. ' +
            ' Injury was very nearly added to insult when the pilot of the autogyro cocked his maxim ' +
            ' as he flew towards me. Happily, the machine gun failed after a single round, and the ' +
            ' tiny helicopter, pilot, gun and all, smashed into a sorry oak. It hadn\'t previously ' +
            ' been sorry, but now it sure was. The advantage to me was that bull, cows and calves were ' +
            ' thoroughly startled, and galumphed to the next field, leaving me to make a soggy exit ' +
            ' to relative safety as a pedestrian now limping, now stumbling along the A34.',  # body
            'A trip up the road',  # h2 => 1.2
            ' I chose Launceston as my destination, trying and mostly failing to keep to a 30cm strip of ' +
            'pavement between an unending series of brick walls, and an unending stream of wing mirrors ' +
            ' on lorries, whistling past my ears at 5 second intervals.',  # body
            'Jam today',  # h1 => 2 (because next line is h2)
            'mouldy',  # h2 => 2.1
            'The arse-end of a number of jars loosely fitting the description of "jam" sat unloved on the ' +
            'communal table of the B&B. Eat? A hint of green at the bottom of at least two of those made the ' +
            'decision for me. ',  # body
            'Get out',  # h2 => 2.2
            'I closed the front door quietly, and headed for The Shops, hopeful that I would find somewhere ' +
            'to eat, which could boast at least 3, ok, 2 hygiene stars.',  # body
            'Close encounters',  # h1 => 3 (because next line is h2)
            'aliens',  # h2 => 3.1
            'I have always felt it unwise to broadcast that we are here. Why would aliens show any less greed ' +
            'for resources protected by feeble competitors then we have, if that is a mark of "intelligence"? ' +
            'And so it proved. With the technology to kill, at will, the bulk of the human population, while ' +
            'preserving more useful resources, no-one escaped. Well, almost no-one. But romantic and ignorant ' +
            'hopes that a computer virus devised by Earth could somehow spike the guns of the invasion? ' +
            'I blame Independence Day. ',  # body
            'Limited time',  # h2 => 3.2
            'So like our own individual lives, which are over before we have had time to properly consider ' +
            'their meaning and value, Humanity will soon be gone, with no legacy worth preserving.'  # body
        ]

        for i in range(0, len(line)):
            dl[i] = DocumentLine(line[i], i)

        return dl

    def get_testset_3(self):
        dl = {}
        line = [
            'This is a Title - a',
            'This is a Heading 1 - b',
            'This is a Heading 2 - c',
            'This is body text because it exceeds a certain number of words blah blah blah  - d',
            'This is body text because it exceeds a certain number of words blah blah blah  - e',
            'This is a heading 2 - f',
            'This is body text because it exceeds a certain number of words blah blah blah  - g',
            'This is a Heading 1 - h',
            'This is a Heading 2 - i',
            'This is body text because it exceeds a certain number of words blah blah blah  - j',
        ]

        for i in range(0, len(line)):
            dl[i] = DocumentLine(line[i], i)

        return dl

    def test_lines_are_in_ok_order(self):
        # arrange
        documentLineSet = self.get_testset_1()

        # act
        doc = Document(documentLineSet)

        # assert
        assert doc.get_line_count() == 10
        assert doc.get_line(0) == 'The Title'
        assert doc.get_line(1) == ''
        
        assert doc.get_line(2) == 'First Header'

        assert doc.get_line(3) == 'Header Two'
        assert doc.get_line(4) == ''
        
        assert doc.get_line(5) == 'Some body and then some repeat all that until more than max for header'
        assert doc.get_line(6) == '2 First Header'
        assert doc.get_line(7) == '2 Header Two'
        assert doc.get_line(8) == ''
        assert doc.get_line(9) == '2 Some body and then some repeat all that until more than max for header'

    def test_set_header_levels(self):

        # arrange
        documentLineSet = self.get_testset_1()
        doc = Document(documentLineSet)

        # act
        doc.set_header_levels()

        # assert
        expected_set = ['T','','H1', 'H2','','','H1', 'H2','','']
        ctr = 0
        for i in expected_set:
            header_level = documentLineSet[ctr].get_header_level()
            assert header_level == i, f"{ctr}: should be '{i}', got '{header_level}'"
            ctr += 1

    """
    Checks that all headers are correctly numbered, and that body text is unchanged.
    """
    def test_number_all_headers(self):
        expected_formatted_doc = {
            0: 'The Title', 1: '1. First Header', 2: '1.1 Header Two',
            3: 'Some body and then some repeat all that until more than max for header',
            4: '2. 2 First Header', 5: '2.1 2 Header Two',
            6: '2 Some body and then some repeat all that until more than max for header'}
        documentLineSet = self.get_testset_1()
        doc = Document(documentLineSet)
        actual_formatted_doc = doc.number_all_headers()
        assert expected_formatted_doc == actual_formatted_doc

    def test_file_to_DocumentLineDict(self):
        source_file = "DocumentHandling/test/data/input/large_document.txt"
        documentLineSet = Document.file_to_DocumentLineDict(source_file)
        doc = Document(documentLineSet)
        assert 1 == 1

    def test_dict_values_to_file(self):
        output_root = "DocumentHandling/test/data"
        my_dict = {}
        my_dict[0] = "some line"
        my_dict[1] = "two line"

        doc = Document(None)
        doc.dict_values_to_file(my_dict, output_root)

    # POC - This works on Python 3.9 on windows. still to test on Linux
    def test_stuff_with_temp_file(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            file_name = f"{tmpdir}/temp.txt"
            with (io.open(file_name, "w")) as fp:
                fp.writelines("do this now\n")
            file_name2 = f"{tmpdir}/temp.txt"
            with (io.open(file_name2, "a")) as fp:
                fp.writelines("do this now2\n")
            with (io.open(file_name2, "r")) as fp:
                a = fp.readlines()

    

    """
    End to end test:
    Read a document which contains headings and body.
    Expected output is a file with its name taken from the title, 
    where the title is the first non-blank line in the source document.
    """
    def test_headings_are_numbered_in_dest_file(self):
        # arrange
        source_file = "DocumentHandling/test/data/input/large_document.txt"
        expected_results = "DocumentHandling/test/data/expected_results/expected_formatted_doc.txt"
        output_root = "DocumentHandling/test/data/output"

        # act
        lines = Document.file_to_DocumentLineDict(source_file)
        doc = Document(lines)
        doc.save_number_headings_to_file(output_root)

        # assert
        actual_results = output_root + "/setting the scene.txt"
        assert Document.files_are_same(self, expected_results, actual_results), "Actual file content is not as expected."



