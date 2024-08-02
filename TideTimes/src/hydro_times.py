# Read data from input.txt
with open('test_tide/data/hydro_summary01.txt', 'r') as infile:
    lines = infile.readlines()

# Filter out blank lines, lines starting with "High" or "Low", and lines containing a "-"
filtered_lines = [line.strip() for line in lines if line.strip() and not line.startswith(("High", "Low")) and "-" not in line]

# Write the filtered lines to output.txt
with open('test_tide/data/xoutput.txt', 'w') as outfile:
    outfile.write('\n'.join(filtered_lines))
