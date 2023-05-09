import pymongo
from pymongo import MongoClient
from dotenv import dotenv_values
 
config = dotenv_values(".env")

client = MongoClient("mongodb://localhost:27017")
# client = MongoClient(config["MONGO_HOST"],config["MONGO_PORT"])
mydb = client["example_db"]
print(mydb)
mycol = mydb["books"]

print(config["MONGO_DATABASE"])
print("You are connected!")
print(client.list_database_names())
print(mydb.list_collection_names())

client.close()

# def get_database():
#     # Provide the mongodb atlas url to connect python to mongodb using pymongo
#    CONNECTION_STRING = "mongodb://localhost:27017"
 
#    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
#    client = MongoClient(CONNECTION_STRING)
#    db = client.config["MONGO_DATABASE"]
#    print(config["MONGO_DATABASE"])
#    print("You are connected!")
#    print(client.list_database_names())

#    # Create the database for our example (we will use the same database throughout the tutorial
#    return db
  
# # This is added so that many files can print(client.list_collection_names())reuse the function get_database()
# if __name__ == "__main__":   
  
#    # Get the database
#    dbname = get_database()