import openpyxl
book = openpyxl.load_workbook('sample.xlsx')
#sheet = book.get_sheet_by_name("sample")
sheet = book["sample"]
sheet['A250'] = "Result"
book.save('sample.xlsx')