
output_file= "filtered_links.txt"

with open("downloadable_links.txt", "r") as dl_file:
    lines = dl_file.readlines()

# Remove duplicates using set
unique_lines = set(lines)

# Open output file for writing
with open(output_file, 'w') as f:
    f.writelines(unique_lines)
