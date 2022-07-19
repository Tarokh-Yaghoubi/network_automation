from flask import Flask, render_template, request, redirect, url_for
from flask import Blueprint
import werkzeug
views = Blueprint('views', __name__)



@views.route('/hello')
def hello():
    return 'hello'

@views.errorhandler(404)
def errorpage(error):
    return 'error 404', 404


def page_not_found(e):
  return render_template('error_404.html'), 404
