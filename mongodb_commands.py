import pymongo

if __name__ == "__main__":
    print("Welcome to pyMongo")
    # Initialise a new db with collection.
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    print(client)

    # List all the databases `show_dbs`
    db_list = client.list_database_names()
    print(db_list)

    # list all collections `show collections`
    collections_list = client['<Anupam>'].list_collection_names()
    print(collections_list)
