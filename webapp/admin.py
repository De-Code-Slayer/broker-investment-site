
from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import User
from .models import Articles, Whatsapp, Howto, University
from . import db
from flask_login import login_user, login_required, current_user
from . import save_file
admin = Blueprint("admin", __name__)



@admin.route("/admin", methods=["GET", "POST"])
@login_required
def administrator():
     if not current_user.admin == True:
        flash('You do not have access to view this page.')
        return render_template("403.html")
     if request.method == "POST":
         # this is to seperate the admin page requests payloads
         section = str(request.form.get("section"))
         
         if section == "Blog":
         #add if statements to check if the post added are long enough and acutually valid
                articletitle = str(request.form.get("articletitle")).title()
                articles = str(request.form.get("articles")).title()
                author = str(request.form.get("author")).title()
                file = request.files['file']
                if file:
                 
                 file_path = save_file(file)
                else:
                    file_path = None
                     
                  
                  
                  
                new_article = Articles(
            articles=articles, author=author, articletitle=articletitle, file_path=file_path)
                db.session.add(new_article)
                db.session.commit()
                flash("posted")
#------------------- Whatsapp section -------------------------------------------------------------
         elif section == "Whatsapp":
         #add if statements to check if the links added are acutually valid
                whatsapp_title = str(request.form.get("whatsapp_title")).title()
                whatsapp_link = str(request.form.get("Whatsapp_link")).title()
                institute = str(request.form.get("Institute")).title()

                new_whatsapp = Whatsapp(
                    name=whatsapp_title, link=whatsapp_link, institute=institute)
                db.session.add(new_whatsapp)
                db.session.commit()
                flash("New Whatsapp added")

         
         
         
         elif section == "HowTo":
         #add if statements to check if the links added are acutually valid
                title = str(request.form.get("title")).title()
                content = str(request.form.get("content"))

     
                new_howto = Howto(
                    title=title, content=content)
                db.session.add(new_howto)
                db.session.commit()
              
                flash("Howto updated")
         
         elif section == "University":
                print("University")
         #add if statements to check if the links added are acutually valid
                school = str(request.form.get("school")).title()
                region = str(request.form.get("region")).title()
                schorlarship = str(request.form.get("Schorlarship")).title()
                fee = str(request.form.get("Fee")).title()
                website = str(request.form.get("Website")).title()
                country = str(request.form.get("country")).title()
     
                new_university = University(
                    school=school, region=region, schorlarship=schorlarship, fee=fee, country=country, website=website)
                db.session.add(new_university)
                db.session.commit()
    
                flash("University updated")

         
         
         
         else:
            flash("error")
     return render_template("admin_page.html")


# -----route to login admins-------------
#Login for admin of the website
@admin.route("/login_admin", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("username")
        password = request.form.get("password")
        user = User.query.filter_by(email=email, password=password).first()
        
        if user:
           login_user(user, remember=True)
           return redirect(url_for("admin.administrator"))
        if  user == None:
            # print("user is none")
            flash("No administrator found")

    return render_template("admin_login.html")

# ------------------ route to add admins---------------------
@admin.route("/add_admin", methods=["POST"])
def signup():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        user = User.query.filter_by(user_name=username).first()
        if user:
            return "username already exist"

        else:

         new_admin = User( password=password, user_name=username)
         db.session.add(new_admin)
         db.session.commit()
         return "added {username} as admin with {password} as password"
