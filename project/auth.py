from flask import (
    flash, request, render_template, redirect, url_for, session, Blueprint
)

from passlib.hash import sha256_crypt
from wtforms import Form, StringField, TextAreaField, PasswordField, validators


auth = Blueprint('auth', __name__)


class RegisterForm(Form):
    name = StringField('Name', [validators.Length(min=1, max=50)])
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email', [validators.Length(min=6, max=50)])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords do not match'),        
    ]) 
    confirm = PasswordField('Confirm Password')


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)

    if request.method == 'POST' and form.validate():
        ...
        name = form.name.data
        email = form.email.data
        username = form.username.data
        password = sha256_crypt.encrypt(str(form.password.data))

        #user1 = Users(name=name, email=email, username=username, password=password)
        #db.session.add(user1)
        #db.session.commit()



        flash('Registered successfully , ready to login !', 'success')

        return redirect(url_for('views.index'))

    return render_template('register.html', form=form)