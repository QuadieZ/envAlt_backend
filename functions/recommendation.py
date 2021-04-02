# import json
import pymongo


# with open('../databases/recommendation.json','r') as json_file:
#     db = json.load(json_file)


def connect_database():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["EnvAlt"]
    # print(mydb.list_collection_names())
    mycol = mydb["recommendation"]
    result = mycol.find()
    myclient.close()
    
    for user in result:
        user.pop("_id")
        db.append(user)
    # print(json.dumps(db, indent=4))
    return db


def recommendations(branchId:str):
    for branch in db:
        if (branch["branchid"] == branchId):
            return branch


db = []
connect_database()