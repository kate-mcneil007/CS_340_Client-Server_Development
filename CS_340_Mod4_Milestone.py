# Imports
from pymongo import MongoClient

# Creating a class
class AnimalShelter (object):
    
    # Constructor to initialize connection with MongoDB
    def __init__(self, username, password):
        self.client = MongoClient('mongodb://%s:%s@localhost:38791/AAC' % (username, password))
        self.db = self.client['AAC']
        print("done")    
        
    # Prints MongoDB databases
    def showDatabases(self):
        print(self.client.list_database_names())

    # Prints MongoDB Collections
    def showCollections(self):
        print(self.db.list_collection_names())

    # Method to create
    def create(self, data):
        # If data field not empty, insert data to db
        if data is not None:
            return self.db.animals.insert_one(data)
        else:
            # Prints error statement
            raise Exception("Failed to create new animal")

    # Method to read
    def read(self, data):
        # If data field is not empty, insert data to db
        if data is not None:
            return self.db.animals.find(data, {"_id": 0})
        else:
            # Prints error statement
            raise Exception("Error, no record matches that id")

    # Method to update
    def update(self, query, data):
        # If data field is not empty
        if data is not None:
            # Update all info matching the inputted query and data
            self.db.animals.update_many(query, data)
            print("Information successfully updated")
            # Find the info being requested
            for x in self.db.animals.find(query):
                # Print info
                print(x)
        else:
            # Print error statement
            raise Exception("Error, information was not updated ")

    #Method to delete
    def delete(self, data):
        # If data field is not empty
        if data is not None:
            # Delete all info matching the inputted data
            self.db.animals.delete_many(data)
            # Find the info being requested
            for x in self.db.animals.find(data):
                # Print info
                print(x)
        else:
            # Print error statement
            raise Exception("Error, could not find any matching data to delete")