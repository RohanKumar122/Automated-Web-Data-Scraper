import pymongo

client = pymongo.MongoClient()
database = client["Scrapper"]
data_collection = database["Data"]
link_collection = database["Links"]