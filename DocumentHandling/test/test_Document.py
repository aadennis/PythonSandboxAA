import io
from tomlkit import item
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

    """
    Checks that all headers are correctly numbered, and that body text is unchanged.
    """
    def test_number_all_headers(self):
        expected_formatted_doc = {0: '1. First Header\n', 1: '1.1 Header Two\n', 2: 'Some body and then some repeat all that until more than max for header\n'}
        documentLineSet = self.get_testset_1()
        doc = Document(documentLineSet)
        actual_formatted_doc = doc.number_all_headers()
        print(actual_formatted_doc)
        assert expected_formatted_doc == actual_formatted_doc


    def test_prefix_is_applied_to_document(self):    
        test_sets = [self.get_testset_2]

        for i in test_sets:
            
            # arrange
            documentLineSet = self.get_testset_2()
            doc = Document(documentLineSet)
            doc.set_header_levels()        

            # act
            h1_ctr = 0
            h2_ctr = 0

            with io.open("c:/temp/set1.txt","w") as f:

                for key, value in doc.documentline_set.items():
                    print(value.get_header_level())
                    if value.get_header_level() == 'H1':
                        h1_ctr += 1
                        print("got one here")
                        f.writelines(f"{h1_ctr}. {value.get_line()}\n")
                        h2_ctr = 0 # reset h2 counter
                    elif value.get_header_level() == 'H2':
                        print("got two here")
                        h2_ctr += 1
                        f.writelines(f"{h1_ctr}.{h2_ctr} {value.get_line()}\n")
                    else:
                        f.writelines(f"{value.get_line()}\n")
                    print(value.get_header_level())
                    print(value.get_line())

        assert 1 == 1            
