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

# entry point
ax = {}

n1 = Name("dennis", "jones")
n2 = Name("harold", "maud")

ax[0] = n1
ax[1] = n2

for i in ax:
    print(ax[i].get_name())
