import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
col = db["products"]

for x in col.find():
    print(x)
