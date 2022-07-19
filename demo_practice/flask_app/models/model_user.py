from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
# This imports the model file
# from flask_app.model import model_books

DATABASE = "instrument_schema"


class User:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
# C

    @classmethod
    def create(cls, data: dict) -> int:
        query = "INSERT INTO users(first_name, last_name, email, pw) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(pw)s);"
        user_id = connectToMySQL('DATABASE').query_db(query, data)
        return user_id

# R

    @classmethod
    def get_one(cls, data: dict) -> list:
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL('DATABASE').query_db(query, data)
        if results:
            return cls(results[0])
        return False

    @classmethod
    def get_one_by_email(cls, data: dict) -> list:
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL('DATABASE').query_db(query, data)
        if results:
            return cls(results[0])
        return False

    @classmethod
    def get_all(cls) -> list:
        query = "SELECT * FROM users;"
        results = connectToMySQL('DATABASE').query_db(query)
        if results:
            all_users = []
            for user in results:
                all_users.append(cls(user))
            return all_users
        return False

# U
    @classmethod
    def update_one(cls, data) -> None:
        query = "UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s WHERE id = %(id)s;"
        return connectToMySQL('DATABASE').query_db(query, data)


# D

    @classmethod
    def delete_one(cls, data: dict) -> None:
        query = "DELETE FROM users WHERE id = %(id)s;"
        return connectToMySQL('DATABASE').query_db(query, data)

    @staticmethod
    def validator(data: dict) -> bool:
        is_valid = True

        if len(data['first_name']) < 1:
            flash('field is required', 'err_users_first_name')
            is_valid = False

        if len(data['last_name']) < 1:
            flash('field is required', 'err_users_last_name')
            is_valid = False

        if len(data['email']) < 1:
            flash('field is required', 'err_users_email')
            is_valid = False

        if len(data['pw']) < 1:
            flash('field is required', 'err_users_pw')
            is_valid = False

        if len(data['confirm_pw']) < 1:
            flash('field is required', 'err_users_confirm_pw')
            is_valid = False
        return is_valid
