from bson import ObjectId

from db.crud import CRUD


def insert_test():
    crud = CRUD("ps", "result")
    content = {"name": "why", "age": "25", "gender": "man"}
    crud.insert_one(content)


def query_test():
    crud = CRUD("ps", "result")
    result = crud.find({})
    for r in result:
        print(r)


def delete_test():
    crud = CRUD("ps", "result")
    crud.delete({"_id": ObjectId("6200dfa2e21f46589a780bd3")})


def delete_many():
    crud = CRUD("ps", "result")
    crud.delete_many({})


# delete_test()
query_test()
