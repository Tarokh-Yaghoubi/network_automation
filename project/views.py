from flask import Flask, render_template, request

from flask import Blueprint

views = Blueprint('views', __name__)

@views.route('/')
def index():
    return render_template('index.html')