import pymongo

if __name__ == "__main__":
    print("Welcome to pyMongo")
    # Initialise a new db with collection.
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    print(client)
    # Create DB and collection
    db = client['Anupam']
    collection = db['mySampleCollection']

    # Insert new record to collection.
    dictionary = {'name': 'Anupam', 'location': 'Pune', 'age': 24}
    collection.insert_one(dictionary)

    # Insert many records as a list of BSON.
    data_list = [
        {'id': 1, 'name': 'Anupam', 'Location': 'Pune', 'age': 23},
        {'id': 2, 'name': 'Saurabh', 'Location': 'Pune', 'age': 24},
        {'id': 3, 'name': 'Harsh', 'Location': 'Ahmedabad', 'age': 26},
    ]
    collection.insert_many(data_list)
