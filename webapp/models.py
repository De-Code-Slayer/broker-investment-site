
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


# Blog website --------------------------------------------
class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String())
    password = db.Column(db.String())
    fullname = db.Column(db.String(100))
    confirmed = db.Column(db.Boolean, nullable=False, default=False)
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    date_deposit = db.Column(db.DateTime(timezone=True), default=func.now())
    date_of_last_update = db.Column(db.DateTime(timezone=True),default=func.now())
    verified = db.Column(db.Boolean, nullable=False, default=False)
    suspended = db.Column(db.Boolean, nullable=False, default=False)
    history = db.relationship('History', backref='user', uselist=True, lazy=False)
    profilephoto = db.Column(db.String(), default=None)
    btc = db.Column(db.Integer, default=0.0000)
    eth = db.Column(db.Integer, default=0.0000)
    balance = db.Column(db.Integer, default=0.0000)
    interest = db.Column(db.Integer, default=0)
    bonus = db.Column(db.Integer, default=0)
    referal_points = db.Column(db.Integer, default=0)
    referals = db.Column(db.String())
    current_plan = db.Column(db.String(), default="You are Currently Not on a Plan")
    limit = db.Column(db.Integer, default=500) #used to set each accountlimit

# ---------- Student--------------------------------------------------
class History(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    person_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    detail = db.Column(db.String())
    date = db.Column(db.Date, default=func.now())
    amount = db.Column(db.Integer)
#     last_name = db.Column(db.String())
#     nationality = db.Column(db.String())
#     age = db.Column(db.Integer())
#     school = db.Column(db.String(100))
#     course = db.Column(db.String())
#     degree = db.Column(db.String())
#     university = db.Column(db.String())
#     admission_status = db.Column(db.String())
#     email = db.Column(db.String())
#     phone = db.Column(db.String())
#     occupation = db.Column(db.String())
#     password = db.Column(db.String())
#     conditional_acceptance = db.Column(db.Integer())
#     admission = db.Column(db.Integer())
#     visa = db.Column(db.Integer())
#     flight = db.Column(db.Integer())
#     arrival = db.Column(db.Integer())
#     admin = db.Column(db.Boolean, default=False)
# #-------------------------------  end of database for blog -------------------------------------


# class Whatsapp(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String())
#     link = db.Column(db.String())
#     institute = db.Column(db.String(100))



# class Howto(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String())
#     content = db.Column(db.String())


# # ---------- students section---------


# class University(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     school = db.Column(db.String())
#     country = db.Column(db.String()) 
#     region = db.Column(db.String()) 
#     fee = db.Column(db.String()) 
#     schorlarship = db.Column(db.String())  
#     website = db.Column(db.String()) 