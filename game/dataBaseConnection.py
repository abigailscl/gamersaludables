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
    def insert_user(self, name, lastname, phone):
        user={"name": name,"lastname":lastname,"phone":phone}
        insertOne=self.collection.insert_one(user)
    
    def print_users(self):
        #recuperar todos los registros
        print('Todos los registros de la tabla usuarios')  
        for users in self.collection.find():
            print(users) 
