
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


# Blog website --------------------------------------------
class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(256))
    password = db.Column(db.String(256))
    fullname = db.Column(db.String(100))
    confirmed = db.Column(db.Boolean, nullable=False, default=False)
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    date_deposit = db.Column(db.DateTime(timezone=True), default=func.now())
    date_of_last_update = db.Column(db.DateTime(timezone=True),default=func.now())
    verified = db.Column(db.Boolean, nullable=False, default=False)
    suspended = db.Column(db.Boolean, nullable=False, default=False)
    history = db.relationship('History', backref='user', uselist=True, lazy=False)
    profilephoto = db.Column(db.String(256), default=None)
    btc = db.Column(db.Integer, default=0.0000)
    eth = db.Column(db.Integer, default=0.0000)
    balance = db.Column(db.Integer, default=0.0000)
    interest = db.Column(db.Integer, default=0)
    bonus = db.Column(db.Integer, default=0)
    referal_points = db.Column(db.Integer, default=0)
    referals = db.Column(db.String(256))
    current_plan = db.Column(db.String(256), default="You are Currently Not on a Plan")
    limit = db.Column(db.Integer, default=500) #used to set each accountlimit

# ---------- Student--------------------------------------------------
class History(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    person_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    detail = db.Column(db.String(1000))
    date = db.Column(db.Date, default=func.now())
    amount = db.Column(db.Integer)



