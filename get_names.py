from bs4 import BeautifulSoup

# Path to your downloaded HTML file
file_path = "content.htm"

# Path to the output file where surnames will be saved
output_file = "surnames.txt"

# Open and read the HTML file
with open(file_path, "r", encoding="utf-8") as file:
    html_content = file.read()

# Parse the HTML with BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

# Find all table rows (skip the header row)
table_rows = soup.find_all("tr")[1:]  # Skip the first row, which is the header

# Extract surnames
surnames = []
for row in table_rows:
    surname_td = row.find("td", class_="sur")  # Look for the <td> with class "sur"
    if surname_td:
        surname = surname_td.get_text(strip=True)  # Extract and clean the surname text
        surnames.append(surname)

# Save surnames to the output file
with open(output_file, "w", encoding="utf-8") as file:
    for surname in surnames:
        file.write(surname + "\n")
