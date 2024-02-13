from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager, current_user
from werkzeug.utils import secure_filename
from os.path import join, dirname, realpath
from flask_mail import Mail
from flask_talisman import Talisman
from apscheduler.schedulers.background import BackgroundScheduler

# from flask_crontab import Crontab


db = SQLAlchemy()
DB_NAME = "185.212.70.154"
ALLOWED_EXTENSIONS = {'png', 'jpg','jpeg'}
UPLOADS_PATH = join(dirname(realpath(__file__)), 'static/images')
basedir = path.abspath(path.dirname(__file__))

UPLOAD_FOLDER = UPLOADS_PATH
app = Flask(__name__)
# crontab = Crontab()

def create_app():
 global app
 app.config["SECRET_KEY"] = "Titans232"
 app.config["SECURITY_PASSWORD_SALT"] = "salt_for_paschal"
#  app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///{}".format(DB_NAME)
 app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://u212458944_glace:Titans232@{}:3306/u212458944_Glacewealth".format(DB_NAME)
 # mail settings
 app.config["MAIL_SERVER"] = "smtp.gmail.com"
 app.config["MAIL_PORT"] = 587
 app.config['SQLALCHEMY_POOL_RECYCLE'] = 0.1
 app.config["MAIL_USE_TLS"] = True
 app.config["MAIL_USE_SSL"] = False
#  crontab.init_app(app)
  # gmail authentication
 app.config["MAIL_USERNAME"] = "veronicapage232@gmail.com"
 app.config["MAIL_PASSWORD"] = "nlevlvdrriimjxdh"

    # mail accounts
 app.config["MAIL_DEFAULT_SENDER"] = 'veronicapage232@gmail.com'



 app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
 app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

 with app.app_context():   
    db.init_app(app)





 from .views import views



 app.register_blueprint(views, url_prefix="/" )


 from .models import User
#  create_database(app)


 login_manager = LoginManager()
 login_manager.login_view = "views.signin"
 login_manager.init_app(app)

 @login_manager.user_loader
 def load_user(id):
    return User.query.get(int(id))


 
# ERROR PAGE HANDLER
 @app.errorhandler(404)
 def page_not_found(error):
    return render_template('404-dark.html', user=current_user), 404
 
 return app

mail = Mail(app)

Talisman(app, content_security_policy=None)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def save_file(file):
   if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(path.join(app.config['UPLOAD_FOLDER'], filename))
            # return url_for('static', filename="images/{filename}")
            return filename

def create_database(app):
    # if not path.exists("webapp/" + DB_NAME):
        db.create_all(app=app)
        print("Database created!!")



#  Initializing scheduler for intrest
from .views import add_interest

def test_job():
   with app.app_context():
     add_interest()

scheduler = BackgroundScheduler()
job       = scheduler.add_job(test_job, 'interval', days=1)
scheduler.start()