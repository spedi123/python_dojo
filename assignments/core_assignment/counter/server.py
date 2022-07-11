from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'peteran'
# this is going to move in the future


@app.route('/')
def counter():
    if 'count' in session:
        session['count'] += 1
    else:
        session['count'] = 1
    return render_template('index.html', count=session['count'])
# end of moving area


@app.route('/addcount', methods=['POST'])
def addcount():
    session['count'] += 1
    return redirect('/')


@app.route('/reset', methods=['POST'])
def reset():
    session['count'] = 0
    return redirect('/')

# @app.route('/', methods=['POST'])
# def add_counter():
#     print(request.form)
#     return render_template('index.html')


# this must be on the bottom of this file
if __name__ == "__main__":
    app.run(debug=True)
