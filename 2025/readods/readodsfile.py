import ezodf

# Path to the ODS file
file_path = 'journal_ranking_data.ods'

# Load the ODS document
doc = ezodf.opendoc(file_path)

# Get the first sheet
sheet = doc.sheets[0]

# Iterate through the rows and print each row as a list
for row in sheet.rows():
    values = [cell.value for cell in row]
    print(values)