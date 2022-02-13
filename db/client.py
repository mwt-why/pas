import pymongo


def get_client(client_name):
    client = pymongo.MongoClient('mongodb://localhost:27017/')
    return client[client_name]
