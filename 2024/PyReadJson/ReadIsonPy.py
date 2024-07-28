import json

# Open the JSON file
with open('Orders.JSON') as file:
    # Load the JSON data
    data = json.load(file)

# Access the parsed data
# Example: Print the value of the 'name' key
print(data[0]['OrderID'])