from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["testdb"]
collection = db["users"]

# Create
collection.insert_one({"name": "Asha", "email": "asha@example.com"})

# Read
print(list(collection.find()))

# Update
collection.update_one({"name": "Asha"}, {"$set": {"email": "asha@newmail.com"}})

# Delete
collection.delete_one({"name": "Asha"})
