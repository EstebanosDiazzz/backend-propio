from pymongo import MongoClient

def connect_to_mongodb(db_name, collection_name):
    uri = "mongodb+srv://Juanesdiaz123-:juanete@tareabioif.p9och.mongodb.net/?retryWrites=true&w=majority&appName=TAREABIOIF"
    client = MongoClient(uri)
    db = client[db_name]
    collection = db[collection_name]
    return collection
