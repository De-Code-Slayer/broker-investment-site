

from flask.helpers import flash
from sqlalchemy.sql.expression import asc
from .models import Articles, Whatsapp, Howto, User, University
from flask import Blueprint, render_template, url_for, request, redirect
from flask_login import login_user, login_required, logout_user, current_user
from . import db


views = Blueprint("views", __name__)




@views.route("/" )
def home():

    # Queries to database to get the post by the 5 most recent
    
    
    return render_template("index.html")


# @views.route("/<id>/hh")
# def more(id):
#     ident = id

#     post = Articles.query.get(ident)
#     return render_template("more_post.html", content=post, user=current_user,  id=ident)


# @views.route("/whatsapp", methods=["GET", "POST"])
# def whatsapp():
#     if request.method == "POST":
#         institute = request.form.get("category")
#         category = Whatsapp.query.filter_by(institute=institute).all()
#         # print(category)
#         if category:
#             whatsapp = category
#             return render_template("whatsapp.html", whatsapp=whatsapp, user=current_user,  id="!!")
            
#     # Queries to database to get All the whatsapp links
#     whatsapp_groups = db.session.query(Whatsapp).all()
#     return render_template("whatsapp.html", whatsapp=whatsapp_groups, user=current_user,  id="!!")


# @views.route("/how")
# def how_to():

#     how_to = Howto.query.all()
#     return render_template("how-to.html", how_to=how_to, user=current_user,  id="!!")


# @views.route("/how_to/<id>")
# def view_how_to(id):
#     ident = id
#     how_to = Howto.query.all()
#     view = Howto.query.get(ident)
#     return render_template("how-to.html", how_to=how_to, view=view, user=current_user,  id="!!")


# @views.route("/university")
# def university():

#     university = University.query.order_by(asc(University.school)).all()
#     print(university)

#     return render_template("university.html", university=university, user=current_user,  id="!!")


# @views.route("/profile", methods=["GET", "POST"])
# @login_required
# def profile():
#     if request.method == "POST":
#         school = str(request.form.get("university")).title()
#         course = str(request.form.get("course")).title()
#         degree = str(request.form.get("degree")).title()
#         email = current_user.email
#         application = User.query.filter_by(email=email).first()
#         print(application)
#         application.university = school
#         application.course = course
#         application.degree = degree
#         db.session.commit()
#         flash("Application Submitted")

#     return render_template("profile.html", student=current_user, user=current_user,  id="!!")

@views.route("/market", methods=["GET", "POST"])
# @login_required
def market():
    

    return render_template("market.html")




@views.route("/exchange", methods=["GET", "POST"])
# @login_required
def exchange():
    

    return render_template("exchange-dark.html")


@views.route("/exchange/liveprice", methods=["GET", "POST"])
# @login_required
def exchange_liveprice():
    

    return render_template("exchange-dark-live-price.html")


# @views.route("/market", methods=["GET", "POST"])
# @login_required
# def market():
    

#     return render_template("profile.html")
# @views.route("/market", methods=["GET", "POST"])
# @login_required
# def market():
    

#     return render_template("profile.html")
# @views.route("/market", methods=["GET", "POST"])
# @login_required
# def market():
    

#     return render_template("profile.html")
# @views.route("/market", methods=["GET", "POST"])
# @login_required
# def market():
    

#     return render_template("profile.html")


@views.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        first_name = str(request.form.get("first-name")).title()
        last_name = str(request.form.get("last-name")).title()
        nationality = str(request.form.get("nationality")).title()
        age = str(request.form.get("age"))
        email = str(request.form.get("email"))
        phone = str(request.form.get("phone")).title()
        occupation = str(request.form.get("occupation")).title()
        password = str(request.form.get("password"))

        check = User.query.filter_by(
            email=email).first()
        if check:
            flash("An account with this email already exist please Login ")
        else:
            application = User(first_name=first_name, last_name=last_name, nationality=nationality,
                               age=age, email=email, phone=phone, occupation=occupation, password=password)
            db.session.add(application)
            db.session.commit()

            user = User.query.filter_by(
                email=email, password=password).first()
            if user:
                login_user(user, remember=True)
                return redirect(url_for("views.profile"))

    return render_template("signup-dark.html")


@views.route("/signin", methods=["GET", "POST"])
def signin():
    if request.method == "POST":

        email = str(request.form.get("email"))
        password = str(request.form.get("password"))

        check = User.query.filter_by(
            email=email, password=password).first()
        if check:

            login_user(check, remember=True)
            return redirect(url_for("views.profile"))
        else:
            flash("Email or Password is not correct")

    return render_template("signin.html")


@views.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("views.signin"))


