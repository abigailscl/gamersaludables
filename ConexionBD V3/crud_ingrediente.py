import pymongo
import dns
from pymongo import collection
from ingrediente import Ingrediente
from bson.objectid import ObjectId

def obtener_bd():
    client = pymongo.MongoClient("mongodb+srv://dbSebastian:12345@cluster0.f5clk.mongodb.net/gamenutrition?retryWrites=true&w=majority")
    gamenutritionDB = client['gamenutrition']
    return gamenutritionDB


def obtener_colec_ingre():
    aux_bd=obtener_bd()
    collection=aux_bd["ingredientes"]
    return collection


#CRUD Ingredientes
def insertar_ingrediente(ingrediente):
    ingredientes=obtener_colec_ingre()
    return ingredientes.insert_one({
        "nombre_ingrediente": ingrediente.nombre_ingrediente,
        "tipo_ingrediente": ingrediente.tipo_ingrediente
    }).inserted_id


def actualizar_ingrediente(id, ingrediente):
    ingredientes=obtener_colec_ingre()
    resultado = ingredientes.update_one(
        {
        '_id': ObjectId(id)
        }, 
        {
            '$set': {
                "nombre_ingrediente": ingrediente.nombre_ingrediente,
                "tipo_ingrediente": ingrediente.tipo_ingrediente
            }
        })
    return resultado.modified_count


def obtener_ingrediente():
    ingredientes=obtener_colec_ingre()
    return ingredientes.find()


def eliminar_ingrediente(id):
    ingredientes=obtener_colec_ingre()
    resultado = ingredientes.delete_one(
        {
        '_id': ObjectId(id)
        })
    return resultado.deleted_count



#Ejecucion de funciones CRUD INGREDIENTE

#Ejecuta funcion Insertar  
"""
print("Insertar")
nombre_ingrediente=input("Nombre_ingrediente: ")
tipo_ingrediente=input("Tipo_ingrediente: ")


ingrediente= Ingrediente(nombre_ingrediente, tipo_ingrediente)
id= insertar_ingrediente(ingrediente)
print("El id del ingerdiente insertado es: ",id)"""


#Ejecuta funcion Actualizar
"""
print("Actualizar")
id = input("Ingresar el id para actualizar: ")
nombre_ingrediente=input("Nombre_ingrediente: ")
tipo_ingrediente=input("Tipo_ingrediente: ")

ingrediente= Ingrediente(nombre_ingrediente, tipo_ingrediente)
ingredientes_actualizados = actualizar_ingrediente(id,ingrediente)
print("Numero de ingredientes actualizados", ingredientes_actualizados)"""


#Ejecuta funcion eliminar
"""
print("Eliminar")
id = input("Id del ingrediente que desee eliminar: ")
ingredientes_eliminados = eliminar_ingrediente(id)
print("Número de ingedientes eliminados: ", ingredientes_eliminados)"""


#Ejecuta funcion Mostrar

print("Obteniendo ingredientes...")
for ingrediente in obtener_ingrediente():
            print("=================")
            print("Id: ", ingrediente["_id"])
            print("Nombre_Ingrediente: ", ingrediente["nombre_ingrediente"])
            print("Tipo_Ingrediente: ", ingrediente["tipo_ingrediente"])
            
