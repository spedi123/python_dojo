from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import model_user


# This imports the model file
# from flask_app.model import model_books
DATABASE = "cocktails_schema"


class Cocktail:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.instruction = data['instruction']
        self.ingredient = data['ingredient']
        self.img_url = data['img_url']
        self.like_count = data['like_count']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


# C


    @classmethod
    def create(cls, data: dict) -> int:
        if data["img_url"][len(data["img_url"])-1] == "/":
            new_data = {
                **data,
                "img": data["img_url"][0:len(data["img_url"])-1]
            }
        else:
            new_data = {
                **data,
                "img": data["img_url"]
            }
        query = """INSERT INTO cocktails(name, instruction, ingredient, img_url, user_id) 
                VALUES (%(name)s, %(instruction)s, %(ingredient)s, %(img)s, %(user_id)s);"""
        return connectToMySQL(DATABASE).query_db(query, new_data)

# R

    @classmethod
    def get_one(cls, data: dict) -> list:
        query = "SELECT * FROM cocktails WHERE id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if results:
            return cls(results[0])
        return False

    @classmethod
    def get_user_all(cls, data: dict) -> list:
        query = "SELECT * FROM cocktails JOIN users ON cocktails.user_id = users.id WHERE users.id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        all_cocktails = []
        for cocktail in results:
            all_cocktails.append(cls(cocktail))
        return all_cocktails

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM cocktails;"
        results = connectToMySQL(DATABASE).query_db(query)
        all_cocktails = []
        for cocktail in results:
            all_cocktails.append(cls(cocktail))
        return all_cocktails

    # @classmethod
    # def get_all(cls) -> list:
    #     query = "SELECT * FROM cocktails JOIN users ON users.id = cocktail.user_id;"
    #     results = connectToMySQL(DATABASE).query_db(query)
    #     if results:
    #         all_cocktails = []
    #         for dict in results:
    #             cocktail = cls(dict)
    #             user_data = {
    #                 'id': dict['users.id'],
    #                 'created_at': dict['users.created_at'],
    #                 'updated_at': dict['users.updated_at'],
    #                 'first_name': dict['first_name'],
    #                 'last_name': dict['last_name'],
    #                 'email': dict['email'],
    #                 'pw': dict['pw']
    #             }
    #             user = model_user.User(user_data)
    #             cocktail.player = user
    #             all_cocktails.append(cocktail)
    #     return all_cocktails

# U
    @classmethod
    def update_one(cls, data) -> None:
        query = """UPDATE cocktails SET name = %(name)s, instruction = %(instruction)s, 
                ingredient = %(ingredient)s, img_url = %(img_url)s WHERE id = %(id)s;"""
        return connectToMySQL(DATABASE).query_db(query, data)


# D

    @classmethod
    def delete_one(cls, data: dict) -> None:
        query = "DELETE FROM cocktails WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)

    @staticmethod
    def validator(data: dict) -> bool:
        is_valid = True

        if len(data['name']) < 1:
            flash('field is required', 'err_cocktails_name')
            is_valid = False

        if len(data['instruction']) < 1:
            flash('field is required', 'err_cocktails_time_played')
            is_valid = False

        if len(data['ingredient']) < 1:
            flash('field is required', 'err_cocktails_type')
            is_valid = False

        if len(data['img_url']) < 1:
            flash('field is required', 'err_cocktails_avg_price')
            is_valid = False

        return is_valid
