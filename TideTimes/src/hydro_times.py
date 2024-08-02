import re
# see hydro_summary01.txt for example input data
# reduce this file a single line for each time and tide height combination

with open('test_tide/data/hydro_summary01.txt', 'r') as infile:
    lines = infile.readlines()

# Remove empty lines and lines starting with "High" or "Low", or containing "-"
cleaned_lines = [line.strip() for line in lines if line.strip() and not line.startswith(("High", "Low")) and not re.search(r"-", line)]

# Merge time and depth information
merged_lines = [f"{cleaned_lines[i]} {cleaned_lines[i + 1]}" for i in range(0, len(cleaned_lines), 2)]

with open("test_tide/data/xoutput.txt", "w") as output_file:
    for line in merged_lines:
        output_file.write(line + "\n")

