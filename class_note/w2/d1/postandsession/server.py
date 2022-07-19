from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'peteran'
# this is going to move in the future


@app.route('/')
def hello_world():
    name = "peter"
    return render_template('index.html', name=name)
# end of moving area


@app.route('/process_info', methods=['POST'])
def process_info():
    print(f"You purchased {request.form['item']}")
    session['cardnumber'] = str(request.form['card_number'])[-4:]
    return redirect('/tracking_info')


@app.route('/tracking_info')
def tracking_info():
    print("Your Card Number is ")
    if 'cardnumber' not in session:
        return redirect('/')
    # print(session['cardnumber'])
    return render_template('tracking.html')


# this must be on the bottom of this file
if __name__ == "__main__":
    app.run(debug=True)
