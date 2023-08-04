"""Defines methods that returns response objects(dict) of our models"""
from models.user import User
from global_vars import USER

def getUserResponse(user: User) -> dict:
    if user:
        userObj = {}
        userObj['id'] = user.id
        userObj['name'] = user.first_name + " " + user.last_name
        userObj['email'] = user.email
        userObj['phone'] = user.phone
        userObj['role'] = user.role.value
        userObj['gender'] = user.gender.value

        return userObj
    
def getListOfResponseObjects(modelType, models: list, pure: bool = False) -> list:
    if modelType and models:
        objList = []
        
        if modelType == USER:
            for model in models:
                objList.append(getUserResponse(model, pure))

        return objList
