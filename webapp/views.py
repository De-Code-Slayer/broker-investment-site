
import os
from datetime import datetime, timedelta,tzinfo
from flask.helpers import flash
from sqlalchemy.sql.expression import asc
from .models import User, History
from flask import Blueprint, render_template, url_for, request, redirect,abort
from flask_login import login_user, login_required, logout_user, current_user
from . import db,save_file
from .generic import generate_confirmation_token, confirm_token, send_email, get_btc,forex,sndmail,get_coin
from .telegram import send_msg

views = Blueprint("views", __name__)



@views.after_request
def add_header(response):
    response.cache_control.max_age = 1209600
    response.cache_control.public = True
    return response


@views.route("/" )
def home():

    
    
    return render_template("index.html", forex=forex() ,name="Home",user=current_user )


# @views.route("/<id>/hh")
# def more(id):
#     ident = id

#     post = Articles.query.get(ident)
#     return render_template("more_post.html", content=post, user=current_user,  id=ident)

@views.route("/home/market")
def market_home():
    
    return render_template("markets_home.html", forex=forex() ,name="Market",user=current_user)

@views.route("/home/about")
def about_home():
    return render_template("about.html", forex=forex() ,name="About",user=current_user)


# @views.route("/home/career")
# def career_home():
    
#     return render_template("careers.html", forex=forex() ,name="Home",user=current_user)


@views.route("/home/contact")
def contact_home():
    
    return render_template("contact.html", forex=forex() ,name="Contact",user=current_user)


@views.route("/home/legal")
def legal_home():
    
    return render_template("legal-docs.html", forex=forex() ,name="Legal",user=current_user)


@views.route("/home/help")
def help_home():
    
    return render_template("help-center.html", forex=forex() ,name="Help",user=current_user)


@views.route("/home/roadmap")
def roadmap_home():
    
    return render_template("roadmap.html", forex=forex() ,name="Road Map",user=current_user)


@views.route("/home/customers")
def customers_home():
    
    return render_template("customers.html", forex=forex() ,name="Customers",user=current_user)


# @views.route("/home/market")
# def market_home():
    
#     return render_template("markets_home.html")
# @views.route("/home/market")
# def market_home():
    
#     return render_template("markets_home.html")
# @views.route("/home/market")
# def market_home():
    
#     return render_template("markets_home.html")




@views.route("/market")
@login_required
def market():
    

    return render_template("market-crypto-dark.html",user=current_user , forex=forex() ,name="Trade Market")




@views.route("/exchange")
@login_required
def exchange():
    

    return render_template("exchange-dark.html",user=current_user, forex=forex() ,name="Exchange")


@views.route("/exchange/liveprice")
@login_required
def exchange_liveprice():
    

    return render_template("exchange-dark-live-price.html",forex=forex() ,name="Live Prices", user=current_user)


@views.route("/exchange/ticker")
@login_required
def exchange_ticker():
    

    return render_template("exchange-dark-ticker.html",user=current_user,forex=forex() ,name="Ticker")


@views.route("/exchange/fluids")
@login_required
def exchange_fluids():
    

    return render_template("exchange-dark-fluid.html",forex=forex() ,name="Fluids",user=current_user)

@views.route("/profile", methods=["GET", "POST"])
@login_required
def profile():
    
    # eth=get_btc("ETH")
    # btc=get_btc("BTC")
    # eth=get_coin("ETH")
    # btc=get_coin("BTC")
    # the investment plan is set here
    if current_user.btc >= 500 and current_user.btc < 2000:
        current_user.current_plan = "You are on BASIC Plan"
        # current_user.interest = 20
        db.session.commit()
    if current_user.btc >= 4000 and current_user.btc < 10000:
        current_user.current_plan = "You are on STANDARD Plan"
        # current_user.interest = 25
        db.session.commit()
    if current_user.btc >= 10000 and current_user.btc < 50000:
        current_user.current_plan = "You are on SILVER Plan"
        # current_user.interest = 28
        db.session.commit()
    if current_user.btc >= 50000 :
        current_user.current_plan = "You are on GOLD Plan"
        # current_user.interest = 30
        db.session.commit()
    # if current_user.confirmed == False:
    #     flash("Please confirm your email, an email was sent to your account","info")
    # if current_user.verified == False:
    #     flash("Please verify your account, go to credential verifications", "info")

    if request.method == "POST":
        file = request.files['img']
        if file:
            file_path = save_file(file)
            current_user.profilephoto = file_path
            db.session.commit()
            flash("Picture updated successfully","success")
        else:
            flash("There was a problem saving your photo. Please try again later","danger")
    
    return 'render_template("settings-wallet-dark.html",forex=forex() ,name="Profile",user=current_user,btc=float(btc), eth=float(eth))'




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
    return render_template("cross-rates-dark.html",user=current_user,forex=forex() ,name="Cross Rates")

@views.route("/marketinfo")
@login_required
def marketinfo():
    return render_template("symbol-info-dark.html",user=current_user,forex=forex() ,name="Market Info")

@views.route("/technicalanalysis")
@login_required
def technical_analysis():
    return render_template("technical-analysis-dark.html",user=current_user,forex=forex() ,name="Analysis")
#
# 

@views.route("/investment")
@login_required
def investment():
    return render_template("investment.html",user=current_user,forex=forex() ,name="Investment")


@views.route("/withdrawals", methods=["GET", "POST"])
@login_required
def withdraw():
    if current_user.verified == False:
        flash("Please verify Your Account to Withdraw","warning")
        return redirect(url_for("views.profile"))

    if request.method == "POST":
       amount = request.form.get("amount")
       address = request.form.get("address")
       note = request.form.get("note")
       customer = current_user.email
       message = f"Withdrawal Request from {customer}\nA withdrawal request of {amount} has been made to this wallet address {address}, the request came with the following note {note}"
       mail = send_msg(message)
       if mail:
           flash("Your request is being proccessed, wait 24hrs before submiting another request","success")
           return redirect(url_for("views.profile"))
       else:
            flash("there is a problem with the server we couldnt receive your request","warning")
            return redirect(url_for("views.profile"))
    return render_template("withdraw.html",user=current_user,forex=forex() ,name="Withdraw")






@views.route("/resetpassword", methods=["GET", "POST"])
@login_required
def reset_password():
    if request.method == "POST":
        email = request.form.get("email")
        user = User.query.filter_by(email=email).first()
        if user:
            password = user.password
            # sndmail(email,"password Recovered",f"Here is your password {password} do not lose it again")
            flash("An Email was sent to you, Please check Your Mail Box", "success")
        else:
            flash("No User With that email was found", "info")
    return render_template("resendpassword.html",user=current_user,forex=forex(),name="Password Recovery")









@views.route("/verification", methods=["GET", "POST"])
@login_required
def verification():
    if request.method=="POST":
        address = str(request.form.get("address"))
        country = str(request.form.get("country"))
        type_of_document = str(request.form.get("id_type"))
        state = str(request.form.get("state"))
        gender = str(request.form.get("gender"))
        zip = str(request.form.get("zip"))
        document = request.files['file']
        number = str(request.form.get("id_number"))
        email = current_user.email
        receiver = "info@glacewealthmanagement.com" # owner of site email
        message = f"Email:{email}\nAddress:{address}\nCountry:{country}\nDoc Type:{type_of_document}\nState:{state}\nGender:{gender}\nZip:{zip}\nID Number:{number}"
        data = save_file(document) 
        basedir = os.path.abspath(os.path.dirname(__file__))
        path = str(basedir) + url_for('static', filename=f"images/{data}")
        a = path.replace("\\","/")
        b = a.replace("/","//")
        # print(b,"===========================>")
        status = sndmail(receiver,"Verification Request",message=message,file=b)
 
       
       

        if status:
            flash("We have Received your Documents we will verify you Shortly", "success")
            return redirect(url_for("views.profile"))
        else:
            flash("We are facing some problems with verification try again later","danger")
            return redirect(url_for("views.profile"))
    return render_template("verification.html",user=current_user,forex=forex() ,name="Verification Center")


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
            # sndmail(application.email, subject, html)
            
            user = User.query.filter_by(
                email=email, password=password).first()
            if user:
                login_user(user, remember=True)
                flash('A confirmation email has been sent via email.', 'success')
                return redirect(url_for("views.profile"))

    return render_template("signup-dark.html",forex=forex() ,name="Register",user=current_user)



@views.route('/resendmail')
@login_required
def resend_confirmation():
    token = generate_confirmation_token(current_user.email)
    confirm_url = url_for('views.confirm_email', token=token, _external=True)
    html = render_template('confirmemail.html', confirm_url=confirm_url)
    subject = "Please confirm your email"
    sndmail(current_user.email, subject, html)
    flash('A new confirmation email has been sent.', 'success')
    return redirect(url_for('views.profile'))



@views.route("/signin", methods=["GET", "POST"])
def signin():
    if request.method == "POST":

        email = str(request.form.get("email"))
        password = str(request.form.get("password"))

        try:
          check = User.query.filter_by(
              email=email, password=password).first()
        except Exception as e:
            db.session.rollback()
        finally:
            db.session.close()
        if check:

            login_user(check, remember=True)
            return redirect(url_for("views.profile"))
        else:
            flash("Email or Password is not correct","warning")

    return render_template("signin.html",user=current_user,forex=forex() ,name="Login")


@views.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("views.signin"))

ZERO = timedelta(0)

class UTC(tzinfo):
  def utcoffset(self, dt):
    return ZERO
  def tzname(self, dt):
    return "UTC"
  def dst(self, dt):
    return ZERO

utc = UTC()


@views.route("/user/update/account/verified")
# @login_required
def update_account():
    
    # import pytz

    
    result = db.session.query(User.btc,User.balance,User.interest,User.date_of_last_update,User.date_deposit,User.id).all()
    status = "Account Updated Successfully"
    mode = "success"
    for i in result:
        # initilize the columns
        deposit = i[0]
        balance = i[1]
        interest_rate = i[2]
        time_stamp = i[3]
        # deposit_date = i[4]
        id = i[5]
        user = User.query.filter_by(id=id).first()

        # conv = deposit_date+timedelta(days=31)
        # print(user.id)
        # days_old = datetime.now() - deposit_date
        last_check = time_stamp+timedelta(days=1)
        # test = deposit_date - timedelta(days=30)
        # print(deposit_date)
        # print(time_stamp - timedelta(seconds=40) )
        # print(time_stamp > (time_stamp - timedelta(seconds=40)) )
        # check if its up to a month since user deposited
        # if conv < datetime.now(utc):
            # check if it been up to a month since last interest was paid
        if last_check < datetime.now(utc):
            print("=============UPDATING====")
            # calculate his interest
            try:
             interest = (deposit*interest_rate)/100
            except Exception as e:
                return e
            # print(interest,"=================================>>>>>>>>")
            user.balance = interest+balance
            status = "Interest paid successfully"
            date=datetime.now()
            amount=interest
            history = History(person_id=current_user.id,detail=status,date=date,amount=amount)
            # stamping date
            user.date_of_last_update = datetime.now()
            db.session.add(history)
            db.session.commit()

            status = "Success"
            # print("============SAVED=====================>>>>>>>>")
        else:
            status = "Interest is alreaady UpToDate"
            # mode = "info"
        # else:  
            # status = "Interest will be paid after a month from deposit Date"
            # mode = "info"
        # flash(status,mode)    
    return redirect(url_for("views.profile"))
        # print(i,"=================================>>>>>>>>")
""""

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
"""








def add_interest():
     

    
    result = db.session.query(User.btc,User.balance,User.interest,User.date_of_last_update,User.date_deposit,User.id).all()
    status = "Account Interest Successfully"
    mode = "success"
    counter = 0
    for i in result:
        counter += 1
        # initilize the columns
        print(counter, "counter")
        deposit = i[0]
        balance = i[1]
        interest_rate = i[2]
        id = i[5]
        user = User.query.filter_by(id=id).first()
        print(deposit,interest_rate,id,"interest")
        
        print("=============UPDATING====")
            # calculate interest
        
        interest = (deposit*interest_rate)/100
        print(interest,deposit,interest_rate,"interest")
        date         =  datetime.now()
        amount       =  interest

        

        user.balance = interest+balance
        print(user.balance,"balance")
        status       = "Interest paid successfully"
            # stamping date
        history      = History(person_id=id,detail=status,date=date,amount=amount)
        user.date_of_last_update = datetime.now()
        db.session.add(history)
        db.session.commit()

        status       = "Success" 
    return status