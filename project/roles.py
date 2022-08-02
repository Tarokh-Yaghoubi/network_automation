from textwrap import wrap
from flask import (
    render_template , request , make_response, flash , redirect, url_for
)

from functools import wraps
from flask_user import login_required

from flask_user import roles_required
from flask import session
from project.auth import login
from project.models import Role, Users, db
from flask import Blueprint
from werkzeug.security import generate_password_hash, check_password_hash

import os

roles = Blueprint('roles', __name__)



def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash("ابتدا وارد  حساب کاربری خود شوید !")
            return redirect(url_for('auth.login'))

    return wrap



@roles.route('/role_table')
@roles_required('admin')
@login_required
def role_table():

    return render_template('table_dt_basic.html')
