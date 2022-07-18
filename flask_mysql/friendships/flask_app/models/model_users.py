from flask_app.config.mysqlconnection import connectToMySQL


class Users:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT id, concat(first_name, ' ', last_name) as name FROM users;"
        users = connectToMySQL('friendships_schema').query_db(query)
        return users

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name, last_name) VALUES ( %(first_name)s, %(last_name)s);"
        return connectToMySQL('friendships_schema').query_db(query, data)

    @classmethod
    def add_friendship(cls, data):
        query = "INSERT INTO friendship (user_id, friend_id) VALUES(%(user_id)s, %(friend_id)s)"
        return connectToMySQL('friendships_schema').query_db(query, data)

    @classmethod
    def get_user_friendships(cls):
        query = """
                    SELECT concat(user1.first_name, ' ', user1.last_name) as User, 
                    concat(user2.first_name, ' ', user2.last_name) as Friend 
                    FROM users as user1 
                    LEFT JOIN friendships ON user1.id = friendships.user_id 
                    JOIN users as user2 ON friendship.friend_id = user2.id 
                    ORDER BY User;
                """
        return connectToMySQL('friendships_schema').query_db(query)
