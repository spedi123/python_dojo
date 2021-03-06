from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'peteran'
# this is going to move in the future


@app.route('/')
def counter():
    if 'count' in session:
        session['count'] += 1
    else:
        session['count'] = 0
    return render_template('index.html', count=session['count'])
# end of moving area


@app.route('/addcount', methods=['POST'])
def addcount():
    # session['count'] += 1
    # if 'count' in session:
    #     session['count'] += 1
    # else:
    #     session['count'] = 1
    return redirect('/')


@app.route('/addtwo', methods=['POST'])
def addtwo():
    if 'count' in session:
        session['count'] += 1
    else:
        session['count'] = 0
    return redirect('/')


@app.route('/reset', methods=['POST'])
def reset():
    session.clear()
    session['count'] = 0
    return redirect('/')


# this must be on the bottom of this file
if __name__ == "__main__":
    app.run(debug=True)
