from db.client import get_client


class CRUD(object):

    def __init__(self, dbname, collection):
        db = get_client(dbname)
        self.collection = db[collection]

    def find(self, condition):
        return self.collection.find(condition)

    def find_one(self):
        return self.collection.find_one()

    def insert_one(self, content):
        self.collection.insert_one(content)

    def delete(self, condition):
        self.collection.delete_one(condition)

    def delete_many(self, condition):
        self.collection.delete_many(condition)
