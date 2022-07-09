from flask import Flask, render_template
app = Flask(__name__)
# this is going to move in the future


@app.route('/')
def hello_world():
    return 'Hello World!'
# end of moving area


@app.route('/dojo')
def hello_dojo():
    return 'Dojo'


@app.route('/say/<string:name>')
def hello_name(name):
    return f"Hi {name}!"


@app.route('/repeat/<int:num>/<string:hello>')
def repeat_hello(num, hello):
    return f"{num * hello}"


# this must be on the bottom of this file
if __name__ == "__main__":
    app.run(debug=True)
