import pymongo
import certifi


mongo_url = "mongodb+srv://ColinOchs:77Finnybear@cluster0.yjqkn.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

client = pymongo.MongoClient(mongo_url, tlsCAFile=certifi.where())

db = client.get_database("CobblestoneOnline")


