from ofxtools.Parser import OFXTree

def process_ofx_file(file_path, target_prefix):
    parser = OFXTree()
    with open(file_path,'rb') as f:
        print('File opened OK')  
        parser.parse(f)
        print('File parsed OK') 
    type(parser._root)
    parser.findall('.//')

# Example usage
if __name__ == "__main__":
    input_file_path = "test/SweetTest.ofx"
    process_ofx_file(input_file_path, target_prefix="ABC")


