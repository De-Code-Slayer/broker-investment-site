

from flask.helpers import flash
from sqlalchemy.sql.expression import asc
from .models import User
from flask import Blueprint, render_template, url_for, request, redirect,abort
from flask_login import login_user, login_required, logout_user, current_user
from . import db,save_file
from .generic import generate_confirmation_token, confirm_token, send_email, get_btc
# from flask_crontab import Crontab

views = Blueprint("views", __name__)




@views.route("/" )
def home():

    
    
    return render_template("index.html", name="Home",user=current_user )


# @views.route("/<id>/hh")
# def more(id):
#     ident = id

#     post = Articles.query.get(ident)
#     return render_template("more_post.html", content=post, user=current_user,  id=ident)

@views.route("/home/market")
def market_home():
    
    return render_template("markets_home.html", name="Home",user=current_user)

@views.route("/home/about")
def about_home():
    return render_template("about.html", name="Home",user=current_user)


@views.route("/home/career")
def career_home():
    
    return render_template("careers.html", name="Home",user=current_user)


@views.route("/home/contact")
def contact_home():
    
    return render_template("contact.html", name="Home",user=current_user)


@views.route("/home/legal")
def legal_home():
    
    return render_template("legal-docs.html", name="Home",user=current_user)


@views.route("/home/help")
def help_home():
    
    return render_template("help-center.html", name="Home",user=current_user)


@views.route("/home/roadmap")
def roadmap_home():
    
    return render_template("roadmap.html", name="Home",user=current_user)


@views.route("/home/customers")
def customers_home():
    
    return render_template("customers.html", name="Home",user=current_user)

"""
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
"""


@views.route("/market")
@login_required
def market():
    

    return render_template("market-crypto-dark.html",user=current_user , name="Home")




@views.route("/exchange")
@login_required
def exchange():
    

    return render_template("exchange-dark.html",user=current_user, name="Home")


@views.route("/exchange/liveprice")
@login_required
def exchange_liveprice():
    

    return render_template("exchange-dark-live-price.html",name="Home", user=current_user)


@views.route("/exchange/ticker")
@login_required
def exchange_ticker():
    

    return render_template("exchange-dark-ticker.html",user=current_user,name="Home")


@views.route("/exchange/fluids")
@login_required
def exchange_fluids():
    

    return render_template("exchange-dark-fluid.html",name="Home",user=current_user)

@views.route("/profile", methods=["GET", "POST"])
@login_required
def profile():
    
    eth=get_btc("eth")
    btc=get_btc("btc")
    # the investment plan is set here
    if current_user.btc >= 1000 and current_user.btc < 2000:
        current_user.current_plan = "You are on BASIC Plan"
        current_user.interest = 20
        db.session.commit()
    if current_user.btc >= 4000 and current_user.btc < 10000:
        current_user.current_plan = "You are on STANDARD Plan"
        current_user.interest = 25
        db.session.commit()
    if current_user.btc >= 10000 and current_user.btc < 50000:
        current_user.current_plan = "You are on SILVER Plan"
        current_user.interest = 28
        db.session.commit()
    if current_user.btc >= 50000 :
        current_user.current_plan = "You are on GOLD Plan"
        current_user.interest = 30
        db.session.commit()
    if current_user.confirmed == False:
        flash("Please confirm your email, an email was sent to your account","info")
    if current_user.verified == False:
        flash("Please verify your account, go to credential verifications", "info")

    if request.method == "POST":
        file = request.files['img']
        if file:
            file_path = save_file(file)
            current_user.profilephoto = file_path
            db.session.commit()
            flash("Picture updated successfully","success")
        else:
            flash("There was a problem saving your photo. Please try again later","danger")
        
    return render_template("settings-wallet-dark.html",name="Home",user=current_user,btc=float(btc), eth=float(eth))




"""
# @views.route("/settings", methods=["GET", "POST"])
# # @login_required
# def settings():
#     eth=get_btc("eth")
#     btc=get_btc("btc")

#     return render_template("settings-dark.html",user=current_user,btc=float(btc), eth=float(eth))

# @views.route("/wallet", methods=["GET", "POST"])
# # @login_required
# def wallet():
    
#     eth=get_btc("eth")
#     btc=get_btc("btc")
    
#     return render_template("settings-wallet-dark.html",user=current_user,btc=float(btc), eth=float(eth))


# @views.route("/settings/updatephoto", methods=["POST"])
# # @login_required
# def update_photo():
#     file = request.files['img']
#     print(file)
#     if file:
#       file_path = save_file(file)
#       current_user.profilephoto = file_path
#       db.session.commit()
#       print("saving=======================>")
#       flash()
#     else:
#       print("nofile====================>")
#       flash()
#     return redirect(url_for('views.profile'))


"""



@views.route("/crossrates")
@login_required
def crossrates():
    return render_template("cross-rates-dark.html",user=current_user,name="Home")

@views.route("/marketinfo")
@login_required
def marketinfo():
    return render_template("symbol-info-dark.html",user=current_user,name="Home")

@views.route("/technicalanalysis")
@login_required
def technical_analysis():
    return render_template("technical-analysis-dark.html",user=current_user,name="Home")
#
# 

@views.route("/investment")
@login_required
def investment():
    return render_template("investment.html",user=current_user,name="Home")


@views.route("/withdrawals")
@login_required
def withdraw():
    return render_template("withdraw.html",user=current_user,name="Home")

@views.route("/verification")
@login_required
def verification():
    return render_template("verification.html",user=current_user,name="Home")


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
       
    return redirect(url_for('views.profile'))



@views.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        fullname = str(request.form.get("fullname")).title()
        email = str(request.form.get("email"))
        password = str(request.form.get("password"))
        confirm_password = str(request.form.get("confirmpassword"))
        if password != confirm_password:
            flash("passwords dont match", "warning")
            return redirect(url_for("views.signup"))
        check = User.query.filter_by(
            email=email, password=password).first()
        if check:
            flash("An account with this email already exist please Login ", "warning")
            return redirect(url_for("views.signin"))
        else:
            application = User(fullname=fullname, email=email, password=password)
            db.session.add(application)
            db.session.commit()
            token = generate_confirmation_token(application.email)
            confirm_url = url_for('views.confirm_email', token=token, _external=True)
            html = render_template('confirmemail.html', confirm_url=confirm_url)
            subject = "Please confirm your email"
            # send_email(application.email, subject, html)

            user = User.query.filter_by(
                email=email, password=password).first()
            if user:
                login_user(user, remember=True)
                flash('A confirmation email has been sent via email.', 'success')
                return redirect(url_for("views.profile"))

    return render_template("signup-dark.html",name="Home",user=current_user)



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
            flash("Email or Password is not correct","warning")

    return render_template("signin.html",user=current_user,name="Home")


@views.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("views.signin"))


@views.route("/user/update/account/verified")
@login_required
def update_account():
    from datetime import datetime, timedelta

    result = db.session.query(User.btc,User.balance,User.interest,User.date_of_last_update,User.date_deposit,User.id).all()
    status = "Account Updated Successfully"
    mode = "success"
    for i in result:
        # initilize the columns
        deposit = i[0]
        balance = i[1]
        interest_rate = i[2]
        time_stamp = i[3]
        deposit_date = i[4]
        id = i[5]
        user = User.query.filter_by(id=id).first()
        # print(user.id)
        # days_old = datetime.now() - deposit_date
        last_check = time_stamp - timedelta(days=30)
        # test = deposit_date - timedelta(days=30)
        print(deposit_date)
        # print(time_stamp - timedelta(seconds=40) )
        # print(time_stamp > (time_stamp - timedelta(seconds=40)) )
        # check if its up to a month since user deposited
        if deposit_date+timedelta(days=31) < datetime.now():
            # check if it been up to a month since last interest was paid
          if last_check > datetime.now()-timedelta(days=31):
            print("=============UPDATING====")
            # calculate his interest
            try:
             interest = (deposit*interest_rate)/100
            except Exception as e:
                return e
            # print(interest,"=================================>>>>>>>>")
            user.balance = interest+balance
            user.history = f" Intrest of {interest}  has been credited to Your account on {time_stamp}"
            # stamping date
            user.date_of_last_update = datetime.now()
            db.session.commit()

            status = "Success"
            # print("============SAVED=====================>>>>>>>>")
          else:
            statsu = "Interest is alreaady UpToDate"
            mode = "info"
        else:  
            status = "Interest will be paid after a month from deposit Date"
            mode = "info"
        flash(status,mode)    
    return redirect(url_for("views.profile"))
        # print(i,"=================================>>>>>>>>")


# [(400, 20000), (50, 656), (85, 8487)]
 

# @crontab.job(minute="1")
# def my_scheduled_job():
#     print("===============> running cronjob")
#     balance = update_balance(current_user) 
#     if current_user.balance == 0:
#        current_user.balance = balance + current_user.btc
#     else:
#        current_user.balance = balance + current_user.btc 
#     db.session.commit()