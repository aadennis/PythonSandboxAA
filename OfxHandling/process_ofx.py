# Given an ofx file, every time a match is found for target_prefix as part of a larger string, 
# replace the current value of the larger string with the value of target_prefix.
# Context for this is that certain vendors choose different names for each transaction, but
# still containing their core name.
# This is unhelpful when trying to identify payees during an import to a finance program.
# Example: AcmeTrading might identify themselves as AcmeTrading139$kkk and AcmeTrading9.9GG 
# in a bank statement. They are still AcmeTrading.
from ofxtools.Parser import OFXTree

def process_ofx_file(file_path, target_prefix):
    parser = OFXTree()
    with open(file_path, 'rb') as f:
        print('File opened OK')
        parser.parse(f)
        print('File parsed OK')

        # Iterate through all elements with the target prefix
        for element in parser.findall('.//'):
            if element.text and target_prefix in element.text:
                # Replace the current value with the target prefix
                element.text = target_prefix

    # Save the modified OFX data to a new file
    random_file_name = generate_random_string(10) + ".ofx"
    with open(random_file_name, 'wb') as new_file:
        parser.write(new_file)

    print(f"Modified OFX data saved to {random_file_name}")

# Helper function to generate a random string
def generate_random_string(length):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

# Example usage
if __name__ == "__main__":
    input_file_path = "SweetTest.ofx"
    process_ofx_file(input_file_path, target_prefix="ABC")

