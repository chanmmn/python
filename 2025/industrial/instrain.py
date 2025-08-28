import os
import csv

# Path to the CSV file
csv_file_path = 'industrial.csv'

# Base directory where folders will be created
base_directory = './'

# Read the CSV file and create folders
try:
    with open(csv_file_path, mode='r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row:  # Ensure the row is not empty
                folder_name = row[0].strip()
                folder_path = os.path.join(base_directory, folder_name)
                os.makedirs(folder_path, exist_ok=True)
                print(f"Created folder: {folder_path}")
except FileNotFoundError:
    print(f"Error: The file '{csv_file_path}' does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")