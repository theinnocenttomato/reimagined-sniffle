from flask import current_app
from flask_login import UserMixin, UserMixin
from flask_sqlalchemy import SQLAlchemy
from itsdangerous import URLSafeTimedSerializer as Serializer
from datetime import datetime
from gamemoguls import db
  
class Scenario(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    statamount = db.Column(db.Integer, nullable=False)
    death = db.Column(db.Boolean, nullable=False,default=False)
    alignment = db.Column(db.Boolean, nullable=False,default=False)
    winners = db.Column(db.Boolean, nullable=False,default=False)
    teams = db.Column(db.Boolean,nullable=False,default=False)
    traits = db.Column(db.Boolean, nullable=False,default=False)
    multiseq = db.Column(db.Boolean, nullable=False,default=False)
    locations = db.Column(db.Boolean, nullable=False,default=False)
    staff = db.Column(db.Boolean, nullable=False,default=False)
    staffstats = db.Column(db.Boolean, nullable=False,default=False)
    stafftype = db.Column(db.Integer, nullable=False,default=0)
    items = db.Column(db.Boolean, nullable=False,default=False)
    ratingamount = db.Column(db.Integer, nullable=False,default=0)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    date_updated = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)


class Scenariorating(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)
    scenario_id = db.Column(db.Integer, db.ForeignKey('scenario.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)


class Translations(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    language = db.Column(db.String(100), nullable=False)
    welcome = db.Column(db.String(100), nullable=False)
    login = db.Column(db.String(100), nullable=False)
    register = db.Column(db.String(100), nullable=False)
    logout = db.Column(db.String(100), nullable=False)


class Users(db.Model, UserMixin):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    email = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    last_login = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

    def get_reset_token(user):
        s= Serializer(current_app.config['SECRET_KEY'], 1800)
        return s.dumps({'user_id': user.id}).decode('utf-8')
    
    @staticmethod
    def verify_reset_token(token):
        s= Serializer(current_app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return Users.query.get(user_id)
    

class Performers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    pronouns = db.Column(db.Integer, nullable=False)
    hometown = db.Column(db.String(100), nullable=False)
    alignment = db.Column(db.String(100), nullable=False)
    isactive = db.Column(db.Boolean, nullable=False,default=True)
    death = db.Column(db.Boolean, nullable=False,default=False)
    creatorid = db.Column(db.Integer, foreign_key=True, nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    date_updated = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)


class Companies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    isactive = db.Column(db.Boolean, nullable=False,default=True)
    currency = db.Column(db.Integer, nullable=False,default=0)
    reputation = db.Column(db.Integer, nullable=False,default=0)
    rostersize = db.Column(db.Integer, nullable=False,default=0)
    isbrand = db.Column(db.Boolean, nullable=False,default=False)
    creatorid = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    date_updated = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)


class Locations(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    size = db.Column(db.String(100), nullable=False)
    population = db.Column(db.Integer, nullable=False)
    parentid = db.Column(db.Integer, nullable=False)
    creatorid = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    date_updated = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

class Staff(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    pronouns = db.Column(db.Integer, nullable=False)
    hometown = db.Column(db.String(100), nullable=False)
    creatorid = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    date_updated = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)


class logs(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    logtype = db.Column(db.String(100), nullable=False)
    logtext = db.Column(db.Text, nullable=False)
    logorigin = db.Column(db.String(100), nullable=False)
    logcreatorid = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    logdate = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)