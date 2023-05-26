import pymongo

if __name__ == "__main__":
    print("Welcome to pyMongo")
    # Initialise a new db with collection.
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    print(client)