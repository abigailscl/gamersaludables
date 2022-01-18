import pymongo
import dns
from pymongo import collection
from bson.objectid import ObjectId
class User():
    def __init__(self):
        self.id = ""
        self.name = ""
        self.lastname = ""
        self.phone = ""
        self.points = 0
        self.client = pymongo.MongoClient("mongodb+srv://dbSebastian:12345@cluster0.f5clk.mongodb.net/gamenutrition?retryWrites=true&w=majority")
        self.gamenutritionDB = self.client['gamenutrition']

    def obtener_colec(self):
        collection=self.gamenutritionDB["usuarios"]
        return collection

    def ver_phone(self, phone):
        if phone[0:4] == "+593" and phone[4] == "9" and len(phone) == 13:
            print("valido")
            return True
        else:
            print("no valido")
            return False


    #CRUD USUARIO
    def insertar(self, name, lastname, phone, points):
        usuarios=self.obtener_colec()
        if self.ver_phone(phone):
            
            return usuarios.insert_one({
                "nombre": name,
                "apellido": lastname,
                "telefono": phone,
                "puntaje": points
            }).inserted_id



    def actualizar(self, id, name, lastname, phone, points):
        usuarios = self.obtener_colec()
        self.name = name
        self.lastname = lastname
        self.phone = phone
        self.points = points
        resultado = usuarios.update_one(
            {
            '_id': ObjectId(id)
            }, 
            {
                '$set': {
                    "nombre": name,
                    "apellido": lastname,
                    "telefono": phone,
                    "puntaje": points
                }
            })
        return resultado.modified_count

    #Mostar datos
    def obtener(self):
        usuarios=self.obtener_colec()
        return usuarios.find()
    
    def verificar_usuario(self, name):
        for usuario in self.obtener():
            _id = usuario["_id"]
            _name = usuario["nombre"]
            _lastname = usuario["apellido"]
            _phone = usuario["telefono"]
            _points = usuario["puntaje"]
            if (_name == name):
                print("usuario existente")
                return True
        return False

    
    def buscar(self, name):
        for usuario in self.obtener():
            print("=================")
            _id = usuario["_id"]
            _name = usuario["nombre"]
            _lastname = usuario["apellido"]
            _phone = usuario["telefono"]
            _points = usuario["puntaje"]
            if (_name == name):
                return _points
        return ""



    #eliminar un dato
    def eliminar(self, id):
        usuarios=self.obtener_colec()
        resultado = usuarios.delete_one(
            {
            '_id': ObjectId(id)
            })
        return resultado.deleted_count