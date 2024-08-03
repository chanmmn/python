import pymongo

# Connect to MongoDB server
client = pymongo.MongoClient("mongodb://localhost:27017")

# Access the database and collection
db = client["mymongodb"]
collection = db["mymongocol"]

# Read data from the collection
data = collection.find()

# Print the retrieved documents
for document in data:
    print(document)

# Close the connection
client.close()