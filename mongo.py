import pymongo

client= pymongo.MongoClient('mongodb+srv://megha:letmecheck@cluster0.05juglt.mongodb.net/inventory')
db=client.inventory

data = {
    'key':"value",
    'testtt':"check"
    }

database = client['inventory']
collection= database["testin1"]
collection.insert_one(data)