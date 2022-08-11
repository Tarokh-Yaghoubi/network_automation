from project.models import Role, Users
from project.views import views
import secrets 
import os 
from datetime import timedelta
from project.views import page_not_found
from project.models import db
from flask import Flask 

from project.config.config import Config

from flask_login import LoginManager

""" Flask Application Factory """


secret_key = secrets.token_hex(16)


app = Flask(__name__)
app.config.from_object(Config)
app.register_error_handler(404, page_not_found)
app.permanent_session_lifetime = timedelta(days=3)
login = LoginManager(app)
db.init_app(app)



with app.app_context():
    user_role = Role.query.get(3).name
    owner_role = Role.query.get(2).name
    admin_role = Role.query.get(1).name


from project import views
from .views import views as views_blueprint
from .auth import auth as auth_blueprint
from .profile import profile as profile_blueprint

app.register_blueprint(views_blueprint) 
app.register_blueprint(auth_blueprint)    
app.register_blueprint(profile_blueprint)
    



@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    
    return r


with app.app_context():


    
    if not Role.query.filter(Role.name=='admin').first():

    
    
        admin_role = Role(name='admin')
    
        db.session.add(admin_role)
    
        db.session.commit()
    
    if not Role.query.filter(Role.name=='owner').first():
    
        owner_role = Role(name='owner')
    
        db.session.add(owner_role)
    
        db.session.commit()
    
    if not Role.query.filter(Role.name=='user').first():
    
        user_role = Role(name='user')
    
        db.session.add(user_role)
    
        db.session.commit()
