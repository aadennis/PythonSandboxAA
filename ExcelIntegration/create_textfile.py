# This script is a simple example of how to use the xlwings library to 
# interact with Excel from Python.
# This use of xlwings promotes separation of concerns between
# presentation-and-source-data (Excel), and functionality (keep that in Python).
# Unlike Excel's current push (03.2025) for tight coupling between Excel and Python, 
# this approach, in my opinion, is more maintainable and scalable.Excel can never be
# properly versioned, and it drags Python down with it, if Python modules are stored in Excel.
# But at least with this approach, the Python code can be versioned and maintained separately.
#
# The default example given by the xlwings starter template is a good starting point, but
# it targets only a single cell. I want to show how to target a range of cells.
# The example requirement (increment the first character of a name) is a bit contrived, but is
# sufficient to demonstrate the concept.
# Be aware that the xlwings library is currently thrown out by Windows Defender as a Trojan, so
# you may be required to add an exception for it.

import xlwings as xw
#import random

# Generate 20 fake names (simple random names for demo purposes)
def generate_fake_names(n=20):
    first_names = ["Alice", "Bob", "Charlie", "David", "Emma", "Florence", "George",
                   "Hannah", "Ian", "Jack", "Katie", "Liam", "Mia", "Nathan", "Olivia",
                   "Paul", "Quinn", "Rachel", "Samuel", "Tina"]
#   return random.sample(first_names, n)
    return first_names


# Increment the first character of a name
def increment_first_letter(name):
    if not name:
        return name
    first_letter = name[0]
    new_letter = chr(((ord(first_letter.lower()) - ord('a') + 1) % 26) + ord('a'))
    if first_letter.isupper():
        new_letter = new_letter.upper()
    return new_letter + name[1:]

def mainx():
    # Open the workbook
    wb = xw.Book("demo1.xlsm")  # Adjust if your workbook has a different name
    sheet0 = wb.sheets[0]
    sheet2 = wb.sheets[2]

    # Populate sheet[0] with fake names in column A
    fake_names = generate_fake_names()
    sheet0.range("A1").options(transpose=True).value = fake_names

    # Transform names and write to sheet[2] column A
    transformed_names = [increment_first_letter(name) for name in fake_names]
    sheet2.range("A1").options(transpose=True).value = transformed_names

    print("Processing complete")

if __name__ == "__main__":
    mainx()
