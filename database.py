from pymongo.mongo_client import MongoClient
from config import settings
# from dotenv import load_dotenv
# import os
from config import settings
# load_dotenv()
class DataBase:
    def __init__(self):
        self.db=self._connect_db()


    def _connect_db(self):
        client=MongoClient(settings.mongodb_uri)
        return client[settings.mongodb_db_name]
    
    def get_collection(self,name_collection:str):
        return self.db[name_collection]
    

