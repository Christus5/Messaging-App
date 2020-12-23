import pymongo


client = pymongo.MongoClient(
     "mongodb+srv://admin:admin@messaging.gfeax.mongodb.net/messaging_app?retryWrites=true&w=majority")
# client = pymongo.MongoClient('192.168.0.108', 27017)
db = client['messaging_app']
messages = db['messages']
users = db['users']