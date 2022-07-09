from flask import Flask, render_template
app = Flask(__name__)
# this is going to move in the future


@app.route('/')
def checker_board():
    return render_template('index.html', num_x=8, num_y=8, row_color="red", column_color="blue")
# end of moving area


@app.route('/<int:num_x>')
def checker_board_x(num_x):
    return render_template('index.html', num_x=num_x, num_y=2, row_color="red", column_color="blue")


@app.route('/<int:num_x>/<int:num_y>')
def checker_board_xy(num_x, num_y):
    return render_template('index.html', num_x=num_x, num_y=num_y, row_color="red", column_color="blue")


@app.route('/<int:num_x>/<int:num_y>/<string:row_color>')
def row_color(num_x, num_y, row_color):
    return render_template('index.html', num_x=num_x, num_y=num_y, row_color=row_color, column_color="blue")


@app.route('/<int:num_x>/<int:num_y>/<string:row_color>/<string:column_color>')
def row_column_color(num_x, num_y, row_color, column_color):
    return render_template('index.html', num_x=num_x, num_y=num_y, row_color=row_color, column_color=column_color)


# this must be on the bottom of this file
if __name__ == "__main__":
    app.run(debug=True)
