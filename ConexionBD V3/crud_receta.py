import pymongo
import dns
from pymongo import collection
from receta import Receta
from bson.objectid import ObjectId

def obtener_bd():
    client = pymongo.MongoClient("mongodb+srv://dbSebastian:12345@cluster0.f5clk.mongodb.net/gamenutrition?retryWrites=true&w=majority")
    gamenutritionDB = client['gamenutrition']
    return gamenutritionDB


def obtener_colec_receta():
    aux_bd=obtener_bd()
    collection=aux_bd["recetas"]
    return collection


#CRUD recetas
def insertar_receta(receta):
    recetas=obtener_colec_receta()
    return recetas.insert_one({
        "nombre_receta": receta.nombre_receta,
        "nombre_ingrediente": receta.nombre_ingrediente,
        "tipo_ingrediente": receta.tipo_ingrediente
    }).inserted_id


def actualizar_receta(id, receta):
    recetas=obtener_colec_receta()
    resultado = recetas.update_one(
        {
        '_id': ObjectId(id)
        }, 
        {
            '$set': {
                "nombre_receta": receta.nombre_receta,
                "nombre_ingrediente": receta.nombre_ingrediente,
                "tipo_ingrediente": receta.tipo_ingrediente
            }
        })
    return resultado.modified_count


def obtener_receta():
    recetas=obtener_colec_receta()
    return recetas.find()


def eliminar_receta(id):
    recetas=obtener_colec_receta()
    resultado = recetas.delete_one(
        {
        '_id': ObjectId(id)
        })
    return resultado.deleted_count


#Ejecucion de funciones CRUD RECETA

"""
#Ejecuta funcion Insertar  
print("Insertar")
lista_nom_ingre=[]
lista_tip_ingre=[]
nombre_receta=input("Nombre_receta: ")
num_ingre=int(input("Cuantos ingredientes va ingresar: "))

for i in range(num_ingre):
    ingre=input("Nombre_ingrediente: ")
    lista_nom_ingre.append(ingre)

for j in range(num_ingre):
    tip_ingre=input("Tipo_Ingrediente: ")
    lista_tip_ingre.append(tip_ingre)

receta= Receta(nombre_receta,lista_nom_ingre, lista_tip_ingre)
id= insertar_receta(receta)
print("El id de la receta insertada es: ",id)"""


#Ejecuta funcion Actualizar
"""
print("Actualizar")
id = input("Ingresar el id para actualizar: ")
lista_nom_ingre=[]
lista_tip_ingre=[]
nombre_receta=input("Nombre_receta: ")
num_ingre=int(input("Cuantos ingredientes va ingresar: "))

for i in range(num_ingre):
    ingre=input("Nombre_ingrediente: ")
    lista_nom_ingre.append(ingre)

for j in range(num_ingre):
    tip_ingre=input("Tipo_Ingrediente: ")
    lista_tip_ingre.append(tip_ingre)

receta= Receta(nombre_receta,lista_nom_ingre, lista_tip_ingre)
recetas_actualizadas = actualizar_receta(id,receta)
print("Numero de recetas actualizadas", recetas_actualizadas)"""


#Ejecuta funcion eliminar
"""
print("Eliminar")
id = input("Id de la receta que desee eliminar: ")
recetas_eliminadas = eliminar_receta(id)
print("Número de recetas eliminadas: ", recetas_eliminadas)"""


#Ejecuta funcion Mostrar

print("Obteniendo recetas...")
for receta in obtener_receta():
            print("=================")
            print("Id: ", receta["_id"])
            print("Nombre_Receta: ", receta["nombre_receta"])
            print("Nombre_Ingrediente: ", receta["nombre_ingrediente"])
            print("Tipo_Ingrediente: ", receta["tipo_ingrediente"])
            
