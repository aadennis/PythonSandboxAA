# Read data from input.txt
with open('test_tide/data/hydro_summary01.txt', 'r') as infile:
    lines = infile.readlines()


# Remove empty lines and lines starting with "High" or "Low"
cleaned_lines = [line.strip() for line in lines if line.strip() and not line.startswith(("High", "Low"))]

# Merge time and depth information
merged_lines = [f"{cleaned_lines[i]} {cleaned_lines[i + 1]}" for i in range(0, len(cleaned_lines), 2)]

# Write the modified content to an output file
with open("test_tide/data/xoutput.txt", "w") as output_file:
    for line in merged_lines:
        output_file.write(line + "\n")

