from flask import (
    flash, render_template, request, redirect, url_for, session
)

from werkzeug.security import generate_password_hash, check_password_hash

from project.models import Users, db
 
from flask_login import login_required

from flask import make_response

from flask import Blueprint

from flask import render_template_string


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

        password_hash = generate_password_hash(password)

        response = make_response(render_template('auth_login.html'))
        session['username'] = username
        session.permanent = True


        if Users.query.filter_by(email=email).first() or Users.query.filter_by(username=username).first() or Users.query.filter_by(PhonNum=phone).first():

            return "You have already signed-in ! , do you wanna <a href='/login'>login</a> ?"

        else : 

            user = Users(
                username = username,
                email = email,
                PhonNum = phone,
                password_hash = password_hash
    
            )
    
            db.session.add(user)
            db.session.commit()
    
            return response
        
    if len(phone) < 11 or len(phone) >= 12:

            flash('شماره تلفن شما صحیح نیست', 'خطا')
            return render_template('auth_register.html')


    return render_template('auth_register.html')

@auth.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':
        
        username = request.form['username']        
        password = request.form['password']
        user = Users.query.filter_by(username=username).first()
        
        session['username'] = username
        session.permanent = True

        if user and check_password_hash(user.password_hash, password):


            return render_template('index.html', username=username)
        
        else:

            ''' return '<script>alert("Check your account credentials");</script>' '''
            if not user:

                flash('اطلاعات ورودی شما صحیح نمیباشد', 'خطا')
                return render_template('auth_login.html')

            elif not check_password_hash(user.password_hash, password):

                flash('رمز عبور شما صحیح نمیباشد', 'خطا')
                return render_template('auth_login.html')

        if username == '' and password == '':

            flash('لطفا نام کاربری و رمز عبور خودرا تکمیل کنید !')
            return render_template('auth_login.html')       



    return render_template('auth_login.html')

@auth.route('/forgot_pass')
def forgot_pass():
    return render_template('auth_pass_recovery_boxed.html')


