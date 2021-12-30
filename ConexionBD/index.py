import pymongo
import dns

#coneccion a la base de datos de mongodb atlas
client = pymongo.MongoClient("mongodb+srv://dbSebastian:12345@cluster0.f5clk.mongodb.net/gamenutrition?retryWrites=true&w=majority")
gamenutritionDB = client['gamenutrition']
collection=gamenutritionDB['usuarios']

#imprimir todas las bases de datos
#print(client.list_database_names())

#imprimir todas las colecciones
#print(gamenutritionDB.list_collection_names())

#insertar un solo registro
#user={"name":"Sebastian","lastname":"Andrango","phone":"0958730412"}
#insertOne=collection.insert_one(user)
#print(insertOne)

#insertar varios registros
# listUsers =[
#     {"nombre":"Jose","apellido":"Lopez","telefono":"0995623120"},
#     {"nombre":"Abigail","apellido":"Cabascango","telefono":"0985412014"},
#     {"nombre":"Juan","apellido":"Perez","telefono":"0998541023"}
# ]

# insert=collection.insert_many(listUsers)
# print(insert)

#eliminar un registro
#delete={"name":"Sebastian"}
# deleteOne=collection.delete_many({})
# print(deleteOne)

#eliminar todos los registros
# delete=collection.delete_many({})
# print(delete)

#recuperar todos los registros
# print('Todos los registros de la tabla usuarios')  
# for users in collection.find():
#   print(users) 


#recuperar registro con una condicion 
# print('Find documents with condition')  
# for x in collection.find({"name": "Jose"}):  
#   print(x) 