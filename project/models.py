""" Database IMports """


from flask import (
    flash, render_template, request, redirect, session, Flask
)


from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.sql import func
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy.sql import func

from flask_user import UserMixin

db = SQLAlchemy()

""" Database  { AriaData } """


class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(150), nullable=False, unique=True)
    PhonNum = db.Column(db.String(100), nullable=False, unique=True)
    is_active = db.Column('is_active', db.Boolean, default=False, nullable=False)


    # user_roles = db.relationship('UserRoles', backref='users', lazy=True)
    licenses = db.relationship('Licences', backref='users', lazy=True)
    settings = db.relationship('Settings', backref='users', lazy=True)

    roles = db.relationship('Role', secondary='user_roles')


    @property
    def password(self):
        raise AttributeError('Password is not a readable attribute !')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def varify_password(self, password):
        return check_password_hash(self.password_hash, password)
 


class Role(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False, unique=True)

    user_roles = db.relationship('UserRoles', backref='role', lazy=True)


class UserRoles(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id', ondelete='CASCADE'), nullable=False)


class Licences(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    SetDate = db.Column(db.DateTime(), nullable=False)
    ExpiryDate = db.Column(db.DateTime(), nullable=False)
    code = db.Column(db.String(110), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    status = db.Column(db.Boolean, default=False, nullable=False)


class Categories(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(110), nullable=False)
    status = db.Column(db.Boolean, default=False, nullable=False)

    settings = db.relationship('Settings', backref='categories', lazy=True)
    schedules = db.relationship('Schedules', backref='categories', lazy=True)
    reports = db.relationship('Reports', backref='categories', lazy=True)
    devices = db.relationship('Devices', backref='categories', lazy=True)


class Settings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    server_url = db.Column(db.String(100), nullable=False)
    port = db.Column(db.Integer, nullable=False)
    ssl = db.Column(db.Boolean, default=False, nullable=False)
    storage = db.Column(db.String(150), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id', ondelete='CASCADE'), nullable=False)

    commands = db.relationship('Commands', backref='settings', lazy=True)
    schedules = db.relationship('Schedules', backref='settings', lazy=True)


class Schedules(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id', ondelete='CASCADE'), nullable=False)
    type = db.Column(db.String(100), nullable=False)
    date1 = db.Column(db.DateTime(), nullable=False)
    date2 = db.Column(db.DateTime(), nullable=False)
    status = db.Column(db.Boolean, default=False, nullable=False)

    setting_id = db.Column(db.Integer, db.ForeignKey('settings.id', ondelete='CASCADE'), nullable=False)


class Devices(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(110), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    ip = db.Column(db.String(100), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id', ondelete='CASCADE'), nullable=False)
    status = db.Column(db.Boolean, default=False, nullable=False)

    reports = db.relationship('Reports', backref='devices', lazy=True)


class Reports(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id', ondelete='CASCADE'), nullable=False)
    device_id = db.Column(db.Integer, db.ForeignKey('devices.id', ondelete='CASCADE'), nullable=False)
    result = db.Column(db.Text)
    date = db.Column(db.DateTime(timezone=True), default=datetime.utcnow)


class Commands(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    priority = db.Column(db.Integer, nullable=False)
    content = db.Column(db.Text, nullable=False)
    setting_id = db.Column(db.Integer, db.ForeignKey('settings.id', ondelete='CASCADE'), nullable=False)


