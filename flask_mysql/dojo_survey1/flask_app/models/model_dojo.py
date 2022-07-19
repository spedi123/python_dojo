from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

DATA = 'books_schema'


class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL(DATA).query_db(query)
        dojos = []
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos

    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos (name , location , language , comment) VALUES (%(name)s , %(location)s , %(language)s, %(comment)s);"
        return connectToMySQL(DATA).query_db(query, data)

    @staticmethod
    def validate(data):
        is_valid = True
        if len(data['name']) < 3:
            flash("You have to fill out your name", 'error_dojo_name')
            is_valid = False

        return is_valid
