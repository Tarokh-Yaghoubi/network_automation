from flask import Flask
from project.views import views
import secrets 
import os 

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

    app.register_blueprint(views_blueprint)     
    

    return app

