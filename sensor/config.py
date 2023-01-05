import pymongo
import pandas as pd
import json
from dataclasses import dataclass
from dotenv import load_dotenv
# Provide the mongodb localhost url to connect python to mongodb.
import os

@dataclass
class EnvironmentVariable:
    #mongo_db_url:str = os.getenv('MONGO_DB_URL')
    mongo_db_url:str = "mongodb+srv://hugar_rajesh:Rajesh_0808@rajesh.ud2bw.mongodb.net/?retryWrites=true&w=majority"
    
    
    aws_access_key_id:str = os.getenv("AWS_ACCESS_KEY_ID")
    aws_access_secret_key:str = os.getenv("AWS_SECRET_ACCESS_KEY")





env_var = EnvironmentVariable()

mongo_client = pymongo.MongoClient(env_var.mongo_db_url)
TARGET_COLUMN = "class"
mongo_db_url = os.getenv('MONGO_DB_URL')
print(mongo_client)
#print(mongo_db_url)