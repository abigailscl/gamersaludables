import pymongo
import dns
from pymongo import collection
from bson.objectid import ObjectId
class User():
    def __init__(self):
        self.id = ""
        self.name = ""
        self.phone = ""
        self.points = 0
        self.client = pymongo.MongoClient("mongodb+srv://dbSebastian:12345@cluster0.f5clk.mongodb.net/gamenutrition?retryWrites=true&w=majority")
        self.gamenutritionDB = self.client['gamenutrition']

    def get_colec(self):
        collection=self.gamenutritionDB["usuarios"]
        return collection

    def check_phone(self, phone):
        if phone[0:4] == "+593" and phone[4] == "9" and len(phone) == 13:
            print("valido")
            return True
        return False

    def insert(self, name, phone, points):
        users = self.get_colec()
        return users.insert_one({
            "nombre": name,
            "telefono": phone,
            "puntaje": points
        }).inserted_id


    def update(self, id, name, phone, points):
        users = self.get_colec()
        self.name = name
        self.phone = phone
        self.points = points
        result = users.update_one(
            {
            '_id': ObjectId(id)
            }, 
            {
                '$set': {
                    "nombre": name,
                    "telefono": phone,
                    "puntaje": points
                }
            })
        return result.modified_count

    #Mostar datos
    def get_collection_users(self):
        users = self.get_colec()
        return users.find()
    
    def check_user(self, name):
       users = self.get_colec()
       if(users.find_one({ "nombre": name })):
           return True
       return False
   
    def get_user(self, name):
       users = self.get_colec()
       return users.find_one({ "nombre": name })
    
    def get_id(self, name):
        users = self.get_colec()
        user = users.find_one({ "nombre": name })
        return user["_id"]
    
    def print_all_user(self, name):
        for user in self.get_collection_users():
            print("Users")
            print( user["_id"] )
            print( user["nombre"] )
            print( user["telefono"] )
            print( user["puntaje"] )

    #eliminar un dato
    def delete_user(self, id):
        users=self.get_colec()
        result = users.delete_one(
            {
            '_id': ObjectId(id)
            })
        return result.deleted_count
    
"""
user = User()
#print(user.insert('user1', '+593960953023', 0))
print(user.get_id('user1'))

"""
