
from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://ShubhamDahaneTry18:Sonali18@cluster0.qlv6p.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

# from pymongo.mongo_client import MongoClient
# import urllib.parse

# # Encode the username and password
# username = urllib.parse.quote_plus("ShubhamDahaneTry18")
# password = urllib.parse.quote_plus("Sonali@18")

# # Construct the URI with the encoded credentials
# uri = f"mongodb+srv://{username}:{password}@cluster0.qlv6p.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# # Create a new client and connect to the server
# client = MongoClient(uri)

# # Send a ping to confirm a successful connection
# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)
