import json

# Open and read the Orders.json file
with open('Orders.json') as file:
    data = json.load(file)

# Print all elements in the JSON data
for element in data:
    print(element)
    print(data[0]['OrderID'])