import pymongo

if __name__ == "__main__":
    print("Welcome to pyMongo")

    # Initialise a new db with collection.
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    print(client)

    # Create DB and collection
    db = client['Anupam']
    collection = db['mySampleCollection']

    # Find one record
    one_record = collection.find_one()
    print(one_record)

    # Get count of results
    count_records = collection.count_documents({'name':'Anupam'})
    print(count_records)

    # Find 1 record satisfying condition
    condition_record = collection.find_one({'name':'Anupam'})
    print(condition_record)

    # Find all records
    all_records = collection.find() 
    '''
        This is a cursor object hence
        needs to be iterated over
    '''
    for record in all_records:
        print(record)

    # Find selective fields satisfying condition
    selective_fields_records = collection.find({'name':'Anupam'}, {'Location':0})
    '''
        Specify the condition as first parameter, second parameter
        will contain fields along with 1 or 0 to return that field or not
        Ex : collection.find(first_param -> {'field_1':'value'}, second_param -> {'field_21':1/0,field_2:1/0})
    '''
    for record in selective_fields_records:
        print(record)
