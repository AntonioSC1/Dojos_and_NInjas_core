from flask_app.config.mysqlconnection import connectToMySQL
DATABASE = "dojos_and_ninjas_ca"
from flask_app.models import ninja


#Dojo Info
class Dojo:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    #inserts/creates into Dojos
    @classmethod
    def create_new_dojo(cls,data):
        query = "INSERT INTO dojos (name) VALUES( %(name)s);"
        new_dojo_id = connectToMySQL(DATABASE).query_db(query,data)
        return new_dojo_id

    #selects all dojos
    @classmethod 
    def get_all_dojos(cls):
        query= "SELECT * FROM dojos"
        results= connectToMySQL(DATABASE).query_db(query)
        return results

    #Selects Dojos and Ninjas together
    @classmethod
    def get_one_dojo(cls,data):  #Joins tables of dojos and ninjas together on ID
        query= "SELECT * FROM dojos JOIN ninjas ON dojos.id=dojos_id WHERE dojos.id=%(id)s;"
        result= connectToMySQL(DATABASE).query_db(query,data)
        if result:
            dojo_instance = cls(result[0])
            ninja_list = []
            for row_in_db in result:
                print(row_in_db)
                ninjas_data = {    #gathers all info from Ninjas Table 
                    'id': row_in_db['ninjas.id'],
                    'first_name': row_in_db['first_name'],
                    'last_name': row_in_db['last_name'],
                    'age': row_in_db['age'],
                    'created_at': row_in_db['ninjas.created_at'],
                    'updated_at': row_in_db['ninjas.updated_at']
                }
                ninjas_instance = ninja.Ninja(ninjas_data)
                ninja_list.append(ninjas_instance)
            dojo_instance.list_ninjas = ninja_list
            return dojo_instance
        return result
    
    
    
    
    
    
    
    #inserting data into Ninjas @ New ninjas page
    @classmethod
    def create(cls,data):
        print("inside create() method", data)
        query = "INSERT INTO ninjas (first_name, last_name, age) VALUES( %(first_name)s, %(last_name)s, %(age)s);"
        return connectToMySQL(DATABASE).query_db(query,data)
    
    
    #selects Individual Id for dojos
    # @classmethod
    # def get_one_dojo(cls,data):
    #     query= "SELECT * FROM dojos WHERE id=%(id)s;"
    #     result= connectToMySQL(DATABASE).query_db(query)
    #     return result