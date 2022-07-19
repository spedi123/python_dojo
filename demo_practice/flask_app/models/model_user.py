from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import bcrypt
from flask import flash, session
import re

# This imports the model file
# from flask_app.model import model_books

DATABASE = "instrument_schema"
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.pw = data['pw']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.fullname = f"{self.first_name.capitalize()} {self.last_name.capitalize()}"

# C

    @classmethod
    def create(cls, data: dict) -> int:
        query = "INSERT INTO users(first_name, last_name, email, pw) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(pw)s);"
        user_id = connectToMySQL(DATABASE).query_db(query, data)
        return user_id

# R

    @classmethod
    def get_one(cls, data: dict) -> list:
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if results:
            return cls(results[0])
        return False

    @classmethod
    def get_one_by_email(cls, data: dict) -> list:
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if results:
            return cls(results[0])
        return False

    @classmethod
    def get_all(cls) -> list:
        query = "SELECT * FROM users;"
        results = connectToMySQL(DATABASE).query_db(query)
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
        return connectToMySQL(DATABASE).query_db(query, data)


# D


    @classmethod
    def delete_one(cls, data: dict) -> None:
        query = "DELETE FROM users WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)

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
        elif not EMAIL_REGEX.match(data['email']):
            flash('Invalid email', 'err_users_email')
            is_valid = False
        else:
            potential_user = User.get_one_by_email({'email': data['email']})
            if potential_user:
                flash('Email already in use', 'err_users_email')
                is_valid = False

        if len(data['pw']) < 1:
            flash('field is required', 'err_users_pw')
            is_valid = False

        if len(data['confirm_pw']) < 1:
            flash('field is required', 'err_users_confirm_pw')
            is_valid = False
        elif data['pw'] != data['confirm_pw']:
            flash('Passwords do not match', 'err_users_confirm_pw')
            is_valid = False
        return is_valid

    @staticmethod
    def validator_login(data: dict) -> bool:
        is_valid = True

        if len(data['email']) < 1:
            flash('field is required', 'err_users_email_login')
            is_valid = False
        elif not EMAIL_REGEX.match(data['email']):
            flash('Invalid email', 'err_users_email_login')
            is_valid = False
        else:
            potential_user = User.get_one_by_email({'email': data['email']})
            if not potential_user:
                flash('Invalid Credentials!', 'err_users_email_login')
                is_valid = False
            # check the hash
            elif not bcrypt.check_password_hash(potential_user.pw, data['pw']):
                flash('Invalid Credentials!!!', 'err_users_email_login')
                is_valid = False
            else:
                # store the id into session
                session['uuid'] = potential_user.id

        if len(data['pw']) < 1:
            flash('field is required', 'err_users_pw_login')
            is_valid = False
        return is_valid
