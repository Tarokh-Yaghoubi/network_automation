from flask import (
    flash, render_template, request, redirect, url_for, session
)

from project.models import Users, db
 
from flask_login import login_required

from flask import make_response

from flask import Blueprint

import hashlib


auth = Blueprint('auth', __name__)

@auth.route('/')
def index_page():
    
    if 'username' in session:
        return f'Logged in as {session["username"]}'
    
    return render_template('auth_login.html')

@auth.route('/register', methods=['POST', 'GET'])
def register():
    
    if request.method == 'POST':

        username = request.form['username']
        email = request.form['email']
        phone = request.form['phone']
        password = request.form['password']
        password = generate_password_hash(password)


        response = make_response(render_template('result.html', username=username, password=password, email=email))
        session['username'] = username
        session.permanent = True

        user = Users(
            username = username,
            email = email,
            PhonNum = phone,
            password = password

        )

        db.session.add(user)
        db.session.commit()

        return response

    return render_template('auth_register.html')

@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('auth_login.html')

@auth.route('/forgot_pass')
def forgot_pass():
    return render_template('auth_pass_recovery_boxed.html')


