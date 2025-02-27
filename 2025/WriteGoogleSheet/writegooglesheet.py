import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
# Define the scope
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive", 'https://www.googleapis.com/auth/spreadsheets']
# Add credentials to the account
creds = ServiceAccountCredentials.from_json_keyfile_name('myprojectiscc-e22bd9284a10.json', scope)
# Authorize the clientsheet 
client = gspread.authorize(creds)
# Get the instance of the Spreadsheet
sheet = client.open_by_url("https://docs.google.com/spreadsheets/d/130Npclfy9nPsXRihiczaUmW6-hza21bwfGfVa064sDo/edit")
# Get the first sheet of the Spreadsheet
worksheet = sheet.get_worksheet(0)
# Read CSV file into DataFrame
df = pd.read_csv('data.csv')
# Write DataFrame to Google Sheet
worksheet.update([df.columns.values.tolist()] + df.values.tolist())
