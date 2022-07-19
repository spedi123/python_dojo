from flask_app.model.model_driver import Drivers
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
# this is going to move in the future


@app.route('/')
def hello_world():
    all_drivers = Drivers.get_all()
    print(all_drivers)
    return render_template("index.html", all_drivers=all_drivers)
# end of moving area


# this must be on the bottom of this file
if __name__ == "__main__":
    app.run(debug=True)
