from flask_app import app

# need to chagne controllers
from flask_app.controllers import instrument_controller, route_controller, user_controller

if __name__ == "__main__":
    app.run(debug=True)
