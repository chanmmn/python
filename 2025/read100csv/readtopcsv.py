import csv

input_file = 'Tweet_top200.csv'
output_file = 'Tweet_top100.csv'
num_rows = 100

with open(input_file, 'r', newline='', encoding='utf-8') as infile, \
    open(output_file, 'w', newline='', encoding='utf-8') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    for i, row in enumerate(reader):
       if i >= num_rows:
          break
       writer.writerow(row)