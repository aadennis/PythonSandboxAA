import re

def clean_text_strict(input_file, output_file):
    # Pattern to keep ONLY: A-Z, a-z, 0-9, apostrophe, space, and CR/LF
    allowed = re.compile(r"[^A-Za-z0-9'\r\n ]")

    with open(input_file, 'r', encoding='utf-8') as infile:
        content = infile.read()

    # Normalize line endings to CRLF if needed
    content = content.replace('\r\n', '\n').replace('\r', '\n')  # Normalize all to \n
    cleaned_lines = [allowed.sub('', line) for line in content.split('\n')]
    cleaned_text = '\r\n'.join(cleaned_lines)  # Convert to CRLF

    with open(output_file, 'w', encoding='utf-8', newline='') as outfile:
        outfile.write(cleaned_text)

# Usage

clean_text_strict('daydream.txt', 'out.txt')
