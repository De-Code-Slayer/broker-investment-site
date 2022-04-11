
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


# Blog website --------------------------------------------
class Articles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    articles = db.Column(db.String())
    articletitle = db.Column(db.String())
    author = db.Column(db.String(100))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    time = db.Column(db.DateTime)
    file_path = db.Column(db.String())
# ---------- Student--------------------------------------------------
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(150))
    first_name = db.Column(db.String())
    last_name = db.Column(db.String())
    nationality = db.Column(db.String())
    age = db.Column(db.Integer())
    school = db.Column(db.String(100))
    course = db.Column(db.String())
    degree = db.Column(db.String())
    university = db.Column(db.String())
    admission_status = db.Column(db.String())
    email = db.Column(db.String())
    phone = db.Column(db.String())
    occupation = db.Column(db.String())
    password = db.Column(db.String())
    conditional_acceptance = db.Column(db.Integer())
    admission = db.Column(db.Integer())
    visa = db.Column(db.Integer())
    flight = db.Column(db.Integer())
    arrival = db.Column(db.Integer())
    admin = db.Column(db.Boolean, default=False)
#-------------------------------  end of database for blog -------------------------------------


class Whatsapp(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    link = db.Column(db.String())
    institute = db.Column(db.String(100))



class Howto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String())
    content = db.Column(db.String())


# ---------- students section---------


class University(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    school = db.Column(db.String())
    country = db.Column(db.String()) 
    region = db.Column(db.String()) 
    fee = db.Column(db.String()) 
    schorlarship = db.Column(db.String())  
    website = db.Column(db.String()) 