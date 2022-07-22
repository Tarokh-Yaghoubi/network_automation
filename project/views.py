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
  return render_template('pages_error404.html'), 404


@views.errorhandler(500)
def errorpage(error):
    return 'error 500', 500


def page_not_found(e):
  return render_template('pages_error500.html'), 500


@views.errorhandler(503)
def errorpage(error):
    return 'error 503', 503


def page_not_found(e):
  return render_template('pages_error503.html'), 503