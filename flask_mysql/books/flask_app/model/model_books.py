from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.model import model_authors


class Books:
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM books;"
        results = connectToMySQL('books_schema').query_db(query)
        books = []
        for book in results:
            books.append(cls(book))
        return books

    @classmethod
    def save(cls, data):
        query = "INSERT INTO books (title, num_of_pages) VALUES ( %(title)s, %(num_of_pages)s);"
        return connectToMySQL('books_schema').query_db(query, data)

    @classmethod
    def get_book_authors(cls, data):
        query = "SELECT * FROM books LEFT JOIN favorites ON books.id = favorites.book_id LEFT JOIN authors ON authors.id = favorites.author_id WHERE books.id = %(book_id)s"
        results = connectToMySQL(
            'books_schema').query_db(query, data)
        book = cls(results[0])
        book_authors = []
        for author in results:
            author_data = {
                "id": author['id'],
                "title": author['title'],
                "num_of_pages": author['num_of_pages'],
                "created_at": author['created_at'],
                "updated_at": author['updated_at'],
                "author_id": author['author_id']
            }
            book_authors.append(Authors(author_data))
        book.authors = book_authors
        return book
