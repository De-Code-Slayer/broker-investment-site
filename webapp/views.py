

from flask.helpers import flash
from sqlalchemy.sql.expression import asc
from .models import User
from flask import Blueprint, render_template, url_for, request, redirect,abort
from flask_login import login_user, login_required, logout_user, current_user
from . import db
from .generic import generate_confirmation_token, confirm_token, send_email

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

@views.route("/home/market")
def market_home():
    
    return render_template("markets_home.html")

@views.route("/home/about")
def about_home():
    return render_template("about.html")


@views.route("/home/career")
def career_home():
    
    return render_template("careers.html")


@views.route("/home/contact")
def contact_home():
    
    return render_template("contact.html")


@views.route("/home/legal")
def legal_home():
    
    return render_template("legal-docs.html")


@views.route("/home/help")
def help_home():
    
    return render_template("help-center.html")


@views.route("/home/roadmap")
def roadmap_home():
    
    return render_template("roadmap.html")


@views.route("/home/customers")
def customers_home():
    
    return render_template("customers.html")


# @views.route("/home/market")
# def market_home():
    
#     return render_template("markets_home.html")
# @views.route("/home/market")
# def market_home():
    
#     return render_template("markets_home.html")
# @views.route("/home/market")
# def market_home():
    
#     return render_template("markets_home.html")


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
    

    return render_template("market.html",user=current_user)




@views.route("/exchange", methods=["GET", "POST"])
# @login_required
def exchange():
    

    return render_template("exchange-dark.html",user=current_user)


@views.route("/exchange/liveprice", methods=["GET", "POST"])
# @login_required
def exchange_liveprice():
    

    return render_template("exchange-dark-live-price.html")


@views.route("/exchange/ticker", methods=["GET", "POST"])
# @login_required
def exchange_ticker():
    

    return render_template("exchange-dark-ticker.html",user=current_user)


@views.route("/exchange/fluids", methods=["GET", "POST"])
# @login_required
def exchange_fluids():
    

    return render_template("exchange-dark-fluid.html")

@views.route("/profile", methods=["GET", "POST"])
@login_required
def profile():
    

    return render_template("settings-profile-dark.html",user=current_user)





@views.route("/settings", methods=["GET", "POST"])
# @login_required
def settings():
    

    return render_template("settings-dark.html",user=current_user)

@views.route("/wallet", methods=["GET", "POST"])
# @login_required
def wallet():
    

    return render_template("settings-wallet-dark.html",user=current_user)





@views.route("/crossrates", methods=["GET", "POST"])
@login_required
def crossrates():
    return render_template("cross-rates-dark.html",user=current_user)

@views.route("/marketinfo", methods=["GET", "POST"])
@login_required
def marketinfo():
    return render_template("symbol-info-dark.html",user=current_user)

@views.route("/technicalanalysis", methods=["GET", "POST"])
@login_required
def technical_analysis():
    return render_template("technical-analysis-dark.html",user=current_user)
#
# 

@views.route("/investment", methods=["GET", "POST"])
def investment():
    return render_template("investment.html")


@views.route("/withdrawals")
def withdraw():
    return render_template("withdraw.html",user=current_user)

@views.route("/verification")
def verification():
    return render_template("verification.html",user=current_user)


@views.route("/confirm/<token>")
def confirm_email(token):
    try:
        email = confirm_token(token)
    except:
        abort(404, response="The confirmation link is invalid or has expired")
    user = User.query.filter_by(email=email).first_or_404()
    if user.confirmed:
     
        abort(404, response="The email is already confirmed")
    else:
        user.confirmed = True
      
        db.session.add(user)
        db.session.commit()
       
    return redirect(url_for('profile'))



@views.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        fullname = str(request.form.get("fullname")).title()
        email = str(request.form.get("email"))
        password = str(request.form.get("password"))
        confirm_password = str(request.form.get("confirmpassword"))
        if password != confirm_password:
            flash(message="passwords dont match")
            abort(500, message="password_error")
        check = User.query.filter_by(
            email=email).first()
        if check:
            flash("An account with this email already exist please Login ")
        else:
            application = User(fullname=fullname, email=email, password=password)
            db.session.add(application)
            db.session.commit()
            token = generate_confirmation_token(application.email)
            confirm_url = url_for('views.confirm_email', token=token, _external=True)
            html = render_template('confirmemail.html', confirm_url=confirm_url)
            subject = "Please confirm your email"
            send_email(application.email, subject, html)

            user = User.query.filter_by(
                email=email, password=password).first()
            if user:
                login_user(user, remember=True)
                flash('A confirmation email has been sent via email.', 'success')
                return redirect(url_for("views.profile"))

    return render_template("signup-dark.html")











@views.route('/resendmail')
@login_required
def resend_confirmation():
    token = generate_confirmation_token(current_user.email)
    confirm_url = url_for('views.confirm_email', token=token, _external=True)
    html = render_template('confirmemail.html', confirm_url=confirm_url)
    subject = "Please confirm your email"
    send_email(current_user.email, subject, html)
    flash('A new confirmation email has been sent.', 'success')
    return redirect(url_for('views.home'))














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


