from flask import render_template, request, redirect, session
from flask_app import app
from flask_app.models.model_email import Email


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def process():
    if not Email.validate_user(request.form):
        return redirect('/')
    Email.save(request.form)
    return redirect('/result')


@app.route('/result')
def result():
    emails = Email.get_all()
    return render_template('result.html', emails=emails)


@app.route('/delete/<int:id>')
def delete_email(id):
    data = {
        'id': id
    }
    Email.delete(data)
    return redirect('/result')

# end of moving area


# this must be on the bottom of this file
if __name__ == "__main__":
    app.run(debug=True)
