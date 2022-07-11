from flask import Flask, render_template, request, redirect
from datetime import datetime
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/checkout', methods=['POST'])
def checkout():
    print(request.form)
    total_buying = int(request.form['strawberry'])+int(request.form['raspberry'])+int(
        request.form['apple'])+int(request.form['blackberry'])
    time = datetime.now()
    current_Time = time.strftime("%B %d, %Y %I:%M:%S %p")
    print(f"'Charging {request.form['first_name']} for {total_buying} fruits'")
    return render_template("checkout.html", current_Time=current_Time, total_buying=total_buying)


@app.route('/fruits')
def fruits():
    return render_template("fruits.html")


if __name__ == "__main__":
    app.run(debug=True)
