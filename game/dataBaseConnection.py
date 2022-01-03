import pymongo
import dns
class Connection():
    def __init__(self):
        #coneccion a la base de datos de mongodb atlas
        self.client = pymongo.MongoClient("mongodb+srv://dbSebastian:12345@cluster0.f5clk.mongodb.net/gamenutrition?retryWrites=true&w=majority")
        self.gamenutritionDB = self.client['gamenutrition']
        self.collection = self.gamenutritionDB['usuarios']
    def print_databases(self):
        #imprimir todas las bases de datos
        print(self.client.list_database_names())
    def print_collections(self):
        #imprimir todas las colecciones
        print(self.gamenutritionDB.list_collection_names())

    #insertar un solo registro
    def insert_user(self, name):
        user={"name": name,"lastname":"Andrango","phone":"0958730412"}
        insertOne=self.collection.insert_one(user)
        print(name)

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
    def print_users(self):
        #recuperar todos los registros
        print('Todos los registros de la tabla usuarios')  
        for users in self.collection.find():
            print(users) 


#recuperar registro con una condicion 
# print('Find documents with condition')  
# for x in collection.find({"name": "Jose"}):  
#   print(x) 