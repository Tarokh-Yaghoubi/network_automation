from flask import Flask
from project.models import Role
from project.views import views
import secrets 
import os 
from datetime import timedelta
from project.views import page_not_found
from project.models import db

""" Flask Application Factory """

username = 'root'
passwd = 'tarokh0010'
host = 'localhost'
port = '3306'
database = 'network_automation'


secret_key = secrets.token_hex(16)

def create_app():

    
    app = Flask(__name__)
    app.config['SECRET_KEY'] = secret_key
    app.register_error_handler(404, page_not_found)
    app.permanent_session_lifetime = timedelta(days=3)
    db.init_app(app)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{0}:{1}@{2}:{3}/{4}?{5}'.format(
    
       
        username, 
        passwd, 
        host, 
        port, 
        database,
        'utf8_persian_ci'
    
    ) 


    from project import views
    from .views import views as views_blueprint
    from .auth import auth as auth_blueprint
    from .profile import profile as profile_blueprint

    app.register_blueprint(views_blueprint) 
    app.register_blueprint(auth_blueprint)    
    app.register_blueprint(profile_blueprint)
    


    return app