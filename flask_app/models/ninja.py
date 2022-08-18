from flask_app.config.mysqlconnection import connectToMySQL
DATABASE = "dojos_and_ninjas_ca"


#Ninja Info
class Ninja:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    #Insert Info of Ninjas
    @classmethod
    def create_ninja(cls,data):
        query = "INSERT INTO ninjas (first_name, last_name, age, dojos_id) VALUES( %(first_name)s, %(last_name)s, %(age)s, %(dojos_id)s);"
        new_ninja_id = connectToMySQL(DATABASE).query_db(query,data)
        return new_ninja_id

