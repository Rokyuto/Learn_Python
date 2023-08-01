from bson.json_util import dumps
from pymongo import MongoClient

def f_GetDatabaseQuestions():
    client = MongoClient("mongodb+srv://pyduo:pyduo@pyd.cjtsbfb.mongodb.net/?retryWrites=true&w=majority") # Our MongoClient
    db = client["pyduo"] # Our Mongo Database
    collection = db["setup"] # Our Database Collection/Table
    cursor = collection.find({}) # Get Documents in the Collection/Table
    with open('TestGenerator/DatabaseCollection.json', 'w') as file: # Create/ Open Collection.json file in write mode
        for document in cursor: # For each element in the document
            document.pop("_id") # Remove the "_id" key and his element from the document, so it will be not writen into the file
            file.write(dumps(document)) # Write the current element in the created json file
        