import json
import pymongo

# connect to the MongoDB
# To establish a connection to MongoDB with PyMongo you use the MongoClient class
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
col = db["products"]

# load data.json into database
with open('./data.json') as f:
    file_data = json.load(f)
    print("data loaded")

x = col.insert_many(file_data)

#print list of the _id values of the inserted documents:
print(x.inserted_ids)
