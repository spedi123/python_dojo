# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
# model the class after the friend table from our database


class Users:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('users_schema').query_db(query)
        # Create an empty list to append our instances of friends
        all_users = []
        # Iterate over the db results and create instances of friends with cls.
        for user in results:
            all_users.append(cls(user))
        return all_users

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users ( first_name , last_name , email) VALUES ( %(first_name)s , %(last_name)s , %(email)s);"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('users_schema').query_db(query, data)

    @classmethod
    def update(cls, data):
        query = "UPDATE users SET first_name=%(first_name)s, last_name=%(last_name)s, email=%(email)s WHERE id=%(id)s;"
        return connectToMySQL('users_schema').query_db(query, data)

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s"
        result = connectToMySQL('users_schema').query_db(query, data)
        return cls(result[0])

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM users WHERE id = %(id)s"
        return connectToMySQL('users_schema').query_db(query, data)
