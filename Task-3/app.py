from flask import Flask, render_template, request, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
from werkzeug.security import generate_password_hash, check_password_hash
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret'

# Read users from CSV
def read_users_from_csv():
    users = []
    with open('Task-3/users.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            users.append({'username': row['username'], 'password': row['password']})
    return users

users = read_users_from_csv()

# WTForms for login form
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

# User Login Endpoint
@app.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        for user in users:
            if user['username'] == username and user['password'] == password:
                flash('Login successful', 'success')
                return render_template('login.html', form=form)

        flash('Invalid credentials', 'danger')
        return render_template('login.html', form=form)

    return render_template('login.html', form=form)

if __name__ == '__main__':
   
    app.run(host='0.0.0.0', port=5000, debug=True)
