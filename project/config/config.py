import os 
import secrets


secret_key = secrets.token_hex(16)

""" DATABASE CREDENTIALS """

username = 'root'
passwd = 'tarokh0010'
host = 'localhost'
port = '3306'
database = 'network_automation'


class Config(object):

    SECRET_KEY = secret_key
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{0}:{1}@{2}:{3}/{4}?{5}'.format(

   
    username, 
    passwd, 
    host, 
    port, 
    database,
    'utf8_persian_ci'

    )