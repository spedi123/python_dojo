from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.model.model_ninjas import Ninjas


class Dojos:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        all_dojos = []
        for dojo in results:
            all_dojos.append(cls(dojo))
        return all_dojos

    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos (name) VALUES ( %(name)s);"
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)

    @classmethod
    def get_dojo_ninjas(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(dojo_id)s"
        results = connectToMySQL(
            'dojos_and_ninjas_schema').query_db(query, data)
        dojo = cls(results[0])
        dojo_ninjas = []
        for ninja in results:
            ninja_data = {
                "id": ninja['id'],
                "first_name": ninja['first_name'],
                "last_name": ninja['last_name'],
                "age": ninja['age'],
                "created_at": ninja['created_at'],
                "updated_at": ninja['updated_at'],
                "dojo_id": ninja['dojo_id']
            }
            dojo_ninjas.append(Ninjas(ninja_data))
        dojo.ninjas = dojo_ninjas
        return dojo
