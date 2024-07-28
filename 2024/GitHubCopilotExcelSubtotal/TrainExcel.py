import pandas as pd

# Read the Excel file
df = pd.read_excel('Train.xlsx')

# Group by Outlet_Location_Type and sum Item_Outlet_Sales
result = df.groupby('Outlet_Location_Type')['Item_Outlet_Sales'].sum()

# Print the result
print(result)