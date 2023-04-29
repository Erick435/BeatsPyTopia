from flask_app import app
from flask import render_template, redirect, request, session
from flask import flash
from flask_app.models.user import User

from flask_bcrypt import Bcrypt #make sure to (pip install flask-bcrypt)
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('login_register.html')

@app.route('/users/register', methods=['POST'])
def register_user():

    #validate user
    if User.validate_user(request.form):
        data = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email' : request.form['email'],
            'password': bcrypt.generate_password_hash(request.form['password'])
        }
        User.create_user(data)
        # print(data)
    else:
        print("is not valid")
    #if valid, add to Database (DB)

    return redirect('/')

@app.route('/users/login', methods=['POST'])
def login_user():

    users = User.get_user_by_email(request.form)

    if len(users) != 1:
        flash("Incorrect email address")
        return redirect('/')

    user = users[0]

    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash("Incorrect password")
        return redirect('/')
    
#use the session values to use on the html to display (besides id)
    session['user_id'] = user.id
    session['first_name'] = user.first_name
    session['last_name'] = user.last_name
    return redirect('/dashboard')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')