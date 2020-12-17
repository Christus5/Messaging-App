import pymongo


client = pymongo.MongoClient(
    "mongodb+srv://admin:admin@messaging.gfeax.mongodb.net/messaging_app?retryWrites=true&w=majority")
db = client['messaging_app']
messages = db['messages']
users = db['users']