from flask import Flask, render_template
app = Flask(__name__)
# this is going to move in the future


@app.route('/')
def hello_world():
    return render_template('index.html')
# end of moving area


@app.route('/peter')
def peter():
    return 'Hello Peter!'


@app.route('/name/<name>')
def name(name):
    print(name)
    return f"'Hello {name}!'"


@app.route('/name/<name>/<int:age>')
def name1(name, age):
    return render_template('people.html', name=name, age=age)


# this must be on the bottom of this file
if __name__ == "__main__":
    app.run(debug=True)
