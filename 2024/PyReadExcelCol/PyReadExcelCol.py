import pandas as pd

# Read the Excel file
file_path = 'POOPHCR.xlsx'
df = pd.read_excel(file_path, usecols="A:C")

# Loop through each row
for index, row in df.iterrows():
    column_a = row['OutletId']
    column_b = row['name']
    column_c = row['bz']
    print(f"Row {index}: A={column_a}, B={column_b}, C={column_c}")