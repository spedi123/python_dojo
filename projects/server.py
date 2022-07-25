from flask_app import app
from flask_app.controllers import user_controller, route_controller
# need to chagne controllers

if __name__ == "__main__":
    app.run(debug=True)
