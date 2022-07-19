from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import bcrypt
from flask import flash, session
import re
# This imports the model file
# from flask_app.model import model_books
DATABASE = "instrument_schema"
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class Table_name:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
# C

    @classmethod
    def create(cls, data: dict) -> int:
        query = "INSERT INTO table_name(name) VALUES (%(name)s);"
        return connectToMySQL(DATABASE).query_db(query, data)

# R

    @classmethod
    def get_one(cls, data: dict) -> list:
        query = "SELECT * FROM table_name WHERE id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if results:
            return cls(results[0])
        return False

    @classmethod
    def get_one_by_email(cls, data: dict) -> list:
        query = "SELECT * FROM table_name WHERE email = %(email)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if results:
            return cls(results[0])
        return False

    @classmethod
    def get_all(cls) -> list:
        query = "SELECT * FROM table_name;"
        results = connectToMySQL(DATABASE).query_db(query)
        if results:
            all_tables = []
            for table_name_single in results:
                all_tables.append(cls(table_name_single))
        return all_tables

# U
    @classmethod
    def update_one(cls, data) -> None:
        query = "UPDATE table_name SET column_name = %(column_name)s WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)


# D


    @classmethod
    def delete_one(cls, data: dict) -> None:
        query = "DELETE FROM table_name WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)

    @staticmethod
    def validator(data: dict) -> bool:
        is_valid = True

        # if not EMAIL_REGEX.match(user['email']):
        #     flash("Invalid email address!")
        #     is_valid = False

        if len(data['first_name']) < 1:
            flash('field is required', 'err_users_first_name')
            is_valid = False
        return is_valid
