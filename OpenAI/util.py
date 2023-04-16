# pip install wheel, pyperclip
import pyperclip

# Get the (single?) value in the clipboard.
# Getpass should be good enough, but does not seem to work in VS code terminal
def get_clipboard(): 
    return pyperclip.paste()
    
# - no use case yet, plus needs a class
# def set_clipboard(string_for_clipboard):

