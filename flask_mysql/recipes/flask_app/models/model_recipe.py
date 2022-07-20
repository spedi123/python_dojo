from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import model_user


# This imports the model file
# from flask_app.model import model_books
DATABASE = "recipes_schema"


class Recipe:
    def __init__(self, data):
        self.id = data['id']
        self.user_id = data['user_id']
        self.name = data['name']
        self.description = data['description']
        self.instruction = data['instruction']
        self.date_made = data['date_made']
        self.under_thirty = data['under_thirty']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


# C

    @classmethod
    def create(cls, data: dict) -> int:
        query = """INSERT INTO recipes(name, description, instruction, date_made, under_thirty, user_id) 
                VALUES (%(name)s, %(description)s, %(instruction)s, %(date_made)s, %(under_thirty)s, %(user_id)s);"""
        return connectToMySQL(DATABASE).query_db(query, data)

# R

    @classmethod
    def get_one(cls, data: dict) -> list:
        query = "SELECT * FROM recipes WHERE id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if results:
            return cls(results[0])
        return False

    @classmethod
    def get_all(cls) -> list:
        query = "SELECT * FROM recipes JOIN users ON users.id = recipes.user_id;"
        results = connectToMySQL(DATABASE).query_db(query)
        if results:
            all_recipes = []
            for dict in results:
                recipe = cls(dict)
                user_data = {
                    'id': dict['users.id'],
                    'created_at': dict['users.created_at'],
                    'updated_at': dict['users.updated_at'],
                    'name': dict['name'],
                    'description': dict['description'],
                    'instruction': dict['instruction'],
                    'date_made': dict['date_made'],
                    'under_thirty': dict['under_thirty']
                }
                user = model_user.User(user_data)
                recipe.cooker = user
                all_recipes.append(recipe)
        return all_recipes

# U
    @classmethod
    def update_one(cls, data) -> None:
        query = """UPDATE recipes SET name = %(name)s, description = %(description)s, 
                instruction = %(instruction)s, date_made = %(date_made)s, under_thirty = %(under_thirty)s 
                WHERE id = %(id)s;"""
        return connectToMySQL(DATABASE).query_db(query, data)


# D


    @classmethod
    def delete_one(cls, data: dict) -> None:
        query = "DELETE FROM recipes WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)

    @staticmethod
    def validator(data: dict) -> bool:
        is_valid = True

        if len(data['name']) < 1:
            flash('field is required', 'err_recipes_name')
            is_valid = False

        if len(data['description']) < 1:
            flash('field is required', 'err_recipes_description')
            is_valid = False

        if len(data['instruction']) < 1:
            flash('field is required', 'err_recipes_instruction')
            is_valid = False

        if len(data['date_made']) < 1:
            flash('field is required', 'err_recipes_date_made')
            is_valid = False

        if len(data['under_thirty']) < 1:
            flash('field is required', 'err_recipes_under_thirty')
            is_valid = False

        return is_valid
