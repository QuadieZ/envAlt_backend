# import json
import pymongo

# with open('./databases/user.json','r') as json_file:
#     data = json.load(json_file)


def connect_database():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["EnvAlt"]
    # print(mydb.list_collection_names())
    mycol = mydb["user"]
    result = mycol.find()
    myclient.close()
    
    for user in result:
        user.pop("_id")
        data.append(user)
    # print(json.dumps(data, indent=4))
    return data


def check_username(username:str):
    for user in data:
        if (user["username"] == username):
            return True
    return False


def check_password(username:str, password:str):
    for user in data:
        if (user["username"] == username):
            if (user["password"] == password):
                return True
    return False


def login(username:str, password:str):
    usernameExsit = check_username(username)
    passwordExsit = check_password(username, password)
    if (usernameExsit == True & passwordExsit == True):
        return True
    else:
        return False


data = []
connect_database()