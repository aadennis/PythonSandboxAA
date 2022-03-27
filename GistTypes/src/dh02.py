import io


"""
  Simple person name class
"""
class Name():
    """
    Simple person name class
    """
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


    def get_name(self):
        """
        get the concatted first and last names
        """
        return f"{self.first_name} {self.last_name}"

    def dont_be_annoyed(self):
        """
        added only to please linter
        """
        return f"{self.last_name} {self.first_name}"

def parse_file():
    ax = {}
    file_path = "DocumentHandling/somenames.txt"
    index = 0
    with io.open(file_path, 'r') as f:
        for line in f:
            elements = line.split(",")
            ax[index] = Name(elements[0], elements[1])
            index += 1
    return ax

# entry point
bx = parse_file()
for i in bx:
    print(bx[i].get_name())
            



