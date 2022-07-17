from flask import (

    flash, redirect, render_template, request, Blueprint, session,
    logging, url_for

)
from flask_sqlalchemy import SQLAlchemy

from passlib.hash import sha256_crypt
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from .data import Articales


Articles = Articales()

db = SQLAlchemy()

views = Blueprint('views', __name__)

@views.route('/')
def index():
    return render_template('home.html')

@views.route('/about')
def about():
    return render_template('about.html')

@views.route('/articles')
def articles():
    return render_template('articles.html', articles=Articles)

@views.route('/articles/<id>')
def articlesId(id):
    return render_template('articles_id.html', id=id)

