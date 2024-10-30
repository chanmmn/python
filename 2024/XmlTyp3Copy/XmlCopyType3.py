import os
import shutil
import csv

# Define paths
csv_file_path = 'OnlyXmlType3.csv'
source_directory = r'C:\xml\path_to_save_xml_files'
destination_directory = r'C:\xml\Type3Bulk'

# Create destination directory if it doesn't exist
if not os.path.exists(destination_directory):
    os.makedirs(destination_directory)

# Read the CSV file
with open(csv_file_path, mode='r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        file_name = row[0]  # Assuming the file names are in the first column
        source_file = os.path.join(source_directory, file_name)
        destination_file = os.path.join(destination_directory, file_name)
        
        # Check if the source file exists
        if os.path.exists(source_file):
            # Copy the file
            shutil.copy2(source_file, destination_file)
            print(f"Copied: {file_name}")
        else:
            print(f"File not found: {file_name}")