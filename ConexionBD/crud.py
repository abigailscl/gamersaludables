import pymongo
import dns
from pymongo import collection
from usuario import Usuario
from bson.objectid import ObjectId

def obtener_bd():
    client = pymongo.MongoClient("mongodb+srv://dbSebastian:12345@cluster0.f5clk.mongodb.net/gamenutrition?retryWrites=true&w=majority")
    gamenutritionDB = client['gamenutrition']
    return gamenutritionDB

def obtener_colec():
    aux_bd=obtener_bd()
    collection=aux_bd["usuarios"]
    return collection

#CRUD
def insertar(usuario):
    usuarios=obtener_colec()
    return usuarios.insert_one({
        "nombre": usuario.nombre,
        "apellido": usuario.apellido,
        "telefono": usuario.telefono,
        "puntaje": usuario.puntaje
    }).inserted_id


def actualizar(id, usuario):
    usuarios=obtener_colec()
    resultado = usuarios.update_one(
        {
        '_id': ObjectId(id)
        }, 
        {
            '$set': {
                "nombre": usuario.nombre,
                "apellido": usuario.apellido,
                "telefono": usuario.telefono,
                "puntaje": usuario.puntaje
            }
        })
    return resultado.modified_count

#Mostar datos
def obtener():
    usuarios=obtener_colec()
    return usuarios.find()


#eliminar un dato
def eliminar(id):
    usuarios=obtener_colec()
    resultado = usuarios.delete_one(
        {
        '_id': ObjectId(id)
        })
    return resultado.deleted_count

#Ejecucion de funciones CRUD

#Ejecuta funcion Insertar  
"""
print("Insertar")
nombre=input("Nombre: ")
apellido=input("Apellido: ")
telefono=input("Telefono: ")
puntaje=float(input("Puntaje: "))

usuario= Usuario(nombre,apellido,telefono,puntaje)
id= insertar(usuario)
print("El id del usuario insertado es: ",id)"""


#Ejecuta funcion Actualizar
"""
print("Actualizar")
id = input("Ingresar el id para actualizar: ")
nombre=input("Nombre: ")
apellido=input("Apellido: ")
telefono=input("Telefono: ")
puntaje=float(input("Puntaje: "))
usuario= Usuario(nombre,apellido,telefono,puntaje)
usuarios_actualizados = actualizar(id,usuario)
print("Numero de productos actualizados", usuarios_actualizados)"""


#Ejecuta funcion eliminar
"""
print("Eliminar")
id = input("Id del usuario que desee eliminar: ")
usuarios_eliminados = eliminar(id)
print("Número de productos eliminados: ", usuarios_eliminados)
"""

#Ejecuta funcion Mostrar
"""
print("Obteniendo usuarios...")
for usuario in obtener():
            print("=================")
            print("Id: ", usuario["_id"])
            print("Nombre: ", usuario["nombre"])
            print("Apellido: ", usuario["apellido"])
            print("Telefono: ", usuario["telefono"])
            print("Puntaje: ", usuario["puntaje"]) 
"""

