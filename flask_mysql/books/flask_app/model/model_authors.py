from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.model import model_books


class Authors:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.favorites = []

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM authors;"
        results = connectToMySQL('books_schema').query_db(query)
        authors = []
        for author in results:
            authors.append(cls(author))
        return authors

    @classmethod
    def save(cls, data):
        query = "INSERT INTO authors (name) VALUES ( %(name)s);"
        return connectToMySQL('books_schema').query_db(query, data)

    @classmethod
    def get_author_books(cls, data):
        query = "SELECT * FROM authors LEFT JOIN favorites ON authors.id = favorites.author_id LEFT JOIN books ON books.id = favorites.book_id WHERE authors.id = %(id)s"
        results = connectToMySQL('books_schema').query_db(query, data)
        author = cls(results[0])
        for book in results:
            book_data = {
                "id": book['id'],
                "title": book['title'],
                "num_of_pages": book['num_of_pages'],
                "created_at": book['created_at'],
                "updated_at": book['updated_at'],
                "author_id": book['author_id']
            }
            author.favorites.append(model_books.Books(book_data))
        return author
