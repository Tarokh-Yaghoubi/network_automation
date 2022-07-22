from flask import (
    flash, render_template, request, redirect, url_for, session
)

from werkzeug.security import generate_password_hash, check_password_hash

from project.models import Users, Role, db
 
from flask_login import login_required

from flask import make_response

from flask import Blueprint

from flask import render_template_string

from flask_user import user_registered



auth = Blueprint('auth', __name__)

    


@auth.route('/')
def index_page():
    
    if 'username' in session:

        flash(f'logged in as {session["username"]}')
        return render_template('index.html')
    
    return render_template('auth_login.html')


@auth.route('/register', methods=['POST', 'GET'])
def register():

    admin_role = Role(name='admin')
    owner_role = Role(name='owner')
    user_role = Role(name='user')
    db.session.commit()

    if not Users.query.filter(Users.username=='admin').first():
        
        user = Users(
            username='admin',
            email='yaghoubitarokh@outlook.com',
            PhonNum = '09105664867',
            password_hash = generate_password_hash('funlife2002')
        )
        user.roles.append(admin_role)
        user.roles.append(owner_role)
        db.session.add(user)
        db.session.commit()
    
    if request.method == 'POST':

        username = request.form['username']
        email = request.form['email']
        phone = request.form['phone']
        password = request.form['password']

        password_hash = generate_password_hash(password)

        response = make_response(render_template('auth_login.html'))



        if Users.query.filter_by(username=username).first():

            flash(f'کاربر با نام کاربری {username} از قبل ثبت نام کرده است', 'error')
            return render_template('auth_register.html')
        
        elif Users.query.filter_by(email=email).first():

            flash(f'کاربر با این آدرس ایمیل از قبل ثبت نام کرده است', 'error')
            return render_template('auth_register.html')

        elif Users.query.filter_by(PhonNum=phone).first():

            flash(f'کاربر با شماره تلفن {phone} از قبل ثبت نام کرده است', 'error')
            return render_template('auth_register.html')




        else:
            
            
            user = Users(
                username = username,
                email = email,
                PhonNum = phone,
                password_hash = password_hash
    
            )

            session['username'] = username
            session.permanent = True
            db.session.add(user)
            db.session.commit()

            return response
            


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

@auth.route('/logout')
def logout():

    for key in list(session.keys()):
        session.pop(key)

    flash('با موفقیت از سیستم خارج شدید', 'success')
    return render_template('auth_login.html')


