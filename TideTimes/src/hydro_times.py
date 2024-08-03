import re
import pandas as pd
# see hydro_summary01.txt for example input data
# reduce this file a single line for each time and tide height combination

with open('test_tide/data/hydro_summary01.txt', 'r') as infile:
    lines = infile.readlines()

# Remove empty lines and lines starting with "High" or "Low", or containing "-"
cleaned_lines = [line.strip() for line in lines if line.strip() and not line.startswith(("High", "Low")) and not re.search(r"-", line)]

# Merge time and depth information
merged_lines = [f"{cleaned_lines[i]} {cleaned_lines[i + 1]}" for i in range(0, len(cleaned_lines), 2)]

# Convert merged_lines to a DataFrame
df = pd.DataFrame({"data": merged_lines})

for i in df:
    print(i[0])

# Extract the time and depth separately
df[["time", "depth"]] = df["data"].str.split(" ", 1).str

# Convert time to datetime format
df["time"] = pd.to_datetime(df["time"], format="%H:%M").dt.time

# Group by day and aggregate the data
grouped = df.groupby(df["time"].diff().dt.days.ne(0).cumsum())["data"].agg(" ".join)

# Write the grouped content to an output file (let's call it "output.txt")
with open("output22.txt", "w") as output_file:
    for line in grouped:
        output_file.write(line + "\n")

