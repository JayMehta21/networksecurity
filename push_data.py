import os 
import json 
import sys 

from dotenv import load_dotenv

load_dotenv()


MONGO_DB_URL = os.getenv("MONGO_DB_URL") 
print(MONGO_DB_URL)


import certifi ## thisis a python package which give roots certificates which helps us in secure https connection . for valid requests 
ca = certifi.where() ##retrieves path and basically gives assurance that server we are connected to is authorised or not.


import pandas as pd 
import numpy as np 
import pymongo
from networksecurity.logging.logger import logging
from networksecurity.exception.exception import NetworkSecurityException

class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e :
            raise NetworkSecurityException(e,sys)
        

    def csv_to_json_converter(self,file_path):
        try:
            data = pd.read_csv(file_path)
            data.reset_index(drop = True , inplace=True)
            records = list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        

    def insert_data_mongodb(self, records, database, collection):
        try:
        # Assign instance variables
            self.database = database
            self.collection = collection
            self.records = records

        # Connect to MongoDB
            self.mongo_client = pymongo.MongoClient(MONGO_DB_URL)

        # Access the database
            db = self.mongo_client[self.database]

        # Access the collection
            col = db[self.collection]

        # Insert data into the collection
            col.insert_many(self.records)
            return len(self.records)

        except Exception as e:
            raise NetworkSecurityException(e, sys)

if __name__ == '__main__':
    FILE_PATH = "Network_Data/phisingData.csv"
    DATABASE = "JAYAI"
    Collection  = "NetworkData"
    networkobj =  NetworkDataExtract()
    records = networkobj.csv_to_json_converter(file_path= FILE_PATH)
    print(records)
    no_of_records = networkobj.insert_data_mongodb(records , DATABASE , Collection)
    print(no_of_records)


