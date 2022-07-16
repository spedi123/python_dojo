#Pre-rec

```
pip3 install pipenv
```

# Checklist

1. create a folder / dir for your assignemnt
2. Navigate into that folder
3. Create your virtual env

```
pipenv install flask PyMySQL flask-bcrpyt
```

4.'Warnging' check for the files "pipfile" and "pipfile.lock" - if you don't see these you need ti fix it.

5. Launch the virtual env

```
pipenv shell
```

6. file structure list

   - assignment folder - static - css - js - img - templates - index.html - pipfile - pipfile.lock - server.py
     server.py file

7. create a

```py
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
# this is going to move in the future
@app.route('/')
def hello_world():
    return 'Hello World!'
# end of moving area

#this must be on the bottom of this file
if __name__=="__main__":
    app.run(debug=True)
```

8. mysqlconnections.py file

```py
# a cursor is the object we use to interact with the database
import pymysql.cursors
# this class will give us an instance of a connection to our database
class MySQLConnection:
    def __init__(self, db):
        # change the user and password as needed
        connection = pymysql.connect(host = 'localhost',
                                    user = 'root',
                                    password = 'rootroot',
                                    db = db,
                                    charset = 'utf8mb4',
                                    cursorclass = pymysql.cursors.DictCursor,
                                    autocommit = True)
        # establish the connection to the database
        self.connection = connection
    # the method to query the database
    def query_db(self, query, data=None):
        with self.connection.cursor() as cursor:
            try:
                query = cursor.mogrify(query, data)
                print("Running Query:", query)

                cursor.execute(query)
                if query.lower().find("insert") >= 0:
                    # INSERT queries will return the ID NUMBER of the row inserted
                    self.connection.commit()
                    return cursor.lastrowid
                elif query.lower().find("select") >= 0:
                    # SELECT queries will return the data from the database as a LIST OF DICTIONARIES
                    result = cursor.fetchall()
                    return result
                else:
                    # UPDATE and DELETE queries will return nothing
                    self.connection.commit()
            except Exception as e:
                # if the query fails the method will return FALSE
                print("Something went wrong", e)
                return False
            finally:
                # close the connection
                self.connection.close()
# connectToMySQL receives the database we're using and uses it to create an instance of MySQLConnection
def connectToMySQL(db):
    return MySQLConnection(db)
```

mode_table_nmae.py file

```py
# import the function that will return an instance of a connection
from mysqlconnection import connectToMySQL
# model the class after the friend table from our database
class Friend:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.occupation = data['occupation']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM friends;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('first_flask').query_db(query)
        # Create an empty list to append our instances of friends
        friends = []
        # Iterate over the db results and create instances of friends with cls.
        for friend in results:
            friends.append( cls(friend) )
        return friends


```

```py
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
# this is going to move in the future
from friend import Friend

@app.route('/')
def hello_world():
     friends = Friend.get_all()
     print(friends)
   return render_template("index.html")
# end of moving area

#this must be on the bottom of this file
if __name__=="__main__":
    app.run(debug=True)
```
