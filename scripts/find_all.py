import pymongo
from flask import jsonify

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
col = db["products"]

# return all documents in the "products" collection, and print each document
for x in col.find():
    print(x)
