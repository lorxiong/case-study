import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
col = db["products"]

# update all doc where the name starts with "T" to new id "123"
myquery = { "name": { "$regex": "^T" } }
newvalues = { "$set": { "id": 123 } }

x = col.update_many(myquery, newvalues)

print(x.modified_count, "documents updated.")
