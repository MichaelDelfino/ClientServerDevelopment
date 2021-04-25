from pymongo import MongoClient
from bson.objectid import ObjectId
from bson.json_util import dumps
from bson.json_util import loads

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections. 
        self.client = MongoClient('mongodb://%s:%s@localhost:43390/AAC' % (username, password))
        self.database = self.client['AAC']
        

    # Create Method 
    def create(self, data):
        if data is not None:
            insert = self.database.animals.insert(data)  # data should be dictionary
            if insert != 0:
                return True
            else:
                return False
        else:
            raise Exception("Nothing to save, because data parameter is empty")

    # Read Method
    def read(self,criteria):
       
        result = self.database.animals.find(criteria, {"_id":False}).limit(10)          
        return result
      
            
        
    
    # Update Method
    def update(self, criteria, updatedData):
        if criteria is not None: 
            update = self.database.animals.update(criteria, updatedData)
            if update != 0:
                cursor = self.database.animals.find(criteria, {"_id": False})
                return dumps(cursor)
            else:
                return False
        else:
            raise Exception("Nothing to update, data not found in database")
            
    # Delete Method
    def delete(self, criteria):
        if criteria is not None:
            remove = self.database.animals.remove(criteria)
            if remove != 0:
                cursor = self.database.animals.find(criteria, {"_id": False})
                return loads(dumps(cursor))
            else:
                return False
        else:
            raise Exception("nothing to remove, data not found in database")