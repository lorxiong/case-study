import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
col = db["products"]

list = [
  { "id": 13860428,
    "name": "The Big Lebowski (Blu-ray) (Widescreen)",
    "current_price": {
        "currency_code": "USD",
        "value": 13.49
    }
  },
  { "id": 15117729,
    "name": "Fargo",
    "current_price": {
        "currency_code": "USD",
        "value": 14.49
    }
  },
  { "id": 16483589,
    "name": "The Hangover",
    "current_price": {
        "currency_code": "USD",
        "value": 15.49
    }
  },
  { "id": 16696652,
    "name": "Fight Club",
    "current_price": {
        "currency_code": "USD",
        "value": 16.49
    }
  },
  { "id": 16752456,
    "name": "The Nice Guys",
    "current_price": {
        "currency_code": "USD",
        "value": 17.49
    }
  },
  { "id": 15643793,
    "name": "Office Space",
    "current_price": {
        "currency_code": "USD",
        "value": 18.49
    }
  }
]


x = col.insert_many(list)

#print list of the _id values of the inserted documents:
print(x.inserted_ids)
