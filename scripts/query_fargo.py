import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
col = db["products"]

myquery = { "name": "Fargo" }

mydoc = col.find(myquery)

for x in mydoc:
  print(x)
