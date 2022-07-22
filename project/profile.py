from flask import (
    flash , render_template, request, Blueprint, session
)

from flask_sqlalchemy import SQLAlchemy
from project.models import Users, db


import os 

profile = Blueprint('profile', __name__)




@profile.route('/user_profile')
def user_profile():

    user = Users.query.filter_by(username=session['username']).first()
    return render_template('user_profile.html', user=user)


@profile.route('/user_account_settings', methods=('GET', 'POST'))
def user_account_settings():    

    user = Users.query.filter_by(username=session['username']).first()

    if request.method == 'POST':

        username = request.form['username']
        email = request.form['email']
        phonenumber = request.form['phonenumber']

        user.username = username
        user.email = email
        user.PhonNum = phonenumber

        db.session.add(user)
        db.session.commit() 

        return render_template('user_account_setting.html', user=user)
    1   
    return render_template('user_account_setting.html', user=user)