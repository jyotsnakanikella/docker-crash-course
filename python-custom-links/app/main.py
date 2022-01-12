from pymongo import MongoClient
from pprint import pp, pprint

MONGO_URL = "mongodb://mongo:27017"
client = MongoClient(MONGO_URL)
db = client.records
collection = db.links
collection.insert_one({"link":"stashchuk.com"})
links = collection.find({})
for link in links:
    pprint(link)