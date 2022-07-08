from flask import Flask
app = Flask(__name__)
# this is going to move in the future


@app.route('/')
def hello_world():
    return 'Hello World!'
# end of moving area


# this must be on the bottom of this file
if __name__ == "__main__":
    app.run(debug=True)
