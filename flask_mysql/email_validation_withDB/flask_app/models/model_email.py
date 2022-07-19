from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

DATABASE = 'email_schema'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class Email:
    def __init__(self, data):
        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM emails;"
        results = connectToMySQL(DATABASE).query_db(query)
        emails = []
        for email in results:
            emails.append(cls(email))
        return emails

    @classmethod
    def save(cls, data):
        query = "INSERT INTO emails (email) VALUES (%(email)s);"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM emails WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)

    @staticmethod
    def validate_user(email):
        is_valid = True
        query = "SELECT * FROM emails WHERE email = %(email)s"
        results = connectToMySQL(DATABASE).query_db(query, email)
        if len(results) >= 1:
            flash("Email is exist", 'error_email')
        if not EMAIL_REGEX.match(email['email']):
            flash("Invalid email address!", 'error_email')
            is_valid = False
        return is_valid
