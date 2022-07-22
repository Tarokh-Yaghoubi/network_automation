from flask import (
    flash , render_template, request, Blueprint
)

from flask_sqlalchemy import SQLAlchemy
from project.models import Users, db


import os 

profile = Blueprint('profile', __name__)




@profile.route('/user_profile/<int:id>')
def user_profile(id):

    user = Users.query.get_or_404(id)
    return render_template('user_profile.html', user=user)


@profile.route('/user_account_settings/<int:id>')
def user_account_settings(id):

    user = Users.query.get_or_404(id)

    if request.method == 'POST':

        username = request.form['username']
        email = request.form['email']
        phonenumber = request.form['PhonNum']

        user.username = username
        user.email = email
        user.PhonNum = phonenumber

        db.session.add(user)
        db.session.commit() 

        return render_template('index.html', user=user)
    1
    return render_template('user_account_setting.html', user=user)