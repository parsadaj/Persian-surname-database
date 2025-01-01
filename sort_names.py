# Path to the file containing surnames
input_file = "surnames.txt"
output_file = "surnames_sorted.txt"  # You can overwrite the same file if desired

# Read surnames from the file
with open(input_file, "r", encoding="utf-8") as file:
    surnames = file.readlines()

# Strip whitespace and sort the names
surnames = [name.strip() for name in surnames]  # Remove newline characters
surnames.sort()  # Sort alphabetically

# Save the sorted surnames back to a file
with open(output_file, "w", encoding="utf-8") as file:
    for surname in surnames:
        file.write(surname + "\n")
