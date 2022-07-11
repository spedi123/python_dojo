from flask import Flask, render_template, request, redirect
app = Flask(__name__)
# this is going to move in the future


@app.route('/')
def hello_world():
    name = "peter"
    return render_template('index.html', name=name)
# end of moving area


@app.route('/process_info', methods=['POST'])
def process_info():
    print(f"You purchased {request.form['item']}")
    return redirect('/tracking_info')


@app.route('/tracking_info')
def tracking_info():
    return render_template('tracking.html')


# this must be on the bottom of this file
if __name__ == "__main__":
    app.run(debug=True)
