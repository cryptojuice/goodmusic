from pymongo import MongoClient

client = MongoClient('192.168.33.13', 27017)

db = client.testdb
