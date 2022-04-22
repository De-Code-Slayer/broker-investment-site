from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager, current_user
from werkzeug.utils import secure_filename
import os
from os.path import join, dirname, realpath

db = SQLAlchemy()
DB_NAME = "Paschals_sqlite_database.db"
# ALLOWED_EXTENSIONS = {'png', 'jpg','jpeg'}
# UPLOADS_PATH = join(dirname(realpath(__file__)), 'static/images')
# # basedir = os.path.abspath(os.path.dirname(__file__))

# UPLOAD_FOLDER = UPLOADS_PATH
app = Flask(__name__)


def create_app():
 global app
 app.config["SECRET_KEY"] = "paschal"
 app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///{}".format(DB_NAME)
#  app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
 app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

 db.init_app(app)

 from .views import views
#  from .admin import admin


 app.register_blueprint(views, url_prefix="/" )
#  app.register_blueprint(admin, url_prefix="/" )

 from .models import User
 create_database(app)


 login_manager = LoginManager()
 login_manager.login_view = "views.login"
 login_manager.init_app(app)

 @login_manager.user_loader
 def load_user(id):
    return User.query.get(int(id))


 
# ERROR PAGE HANDLER
 @app.errorhandler(404)
 def page_not_found(error):
    return render_template('404-dark.html', user=current_user), 404
 
 return app



# def allowed_file(filename):
#     return '.' in filename and \
#            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# def save_file(file):
#    if file and allowed_file(file.filename):
#             filename = secure_filename(file.filename)
#             file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#             # return url_for('static', filename="images/{filename}")
#             return filename
def create_database(app):
    # if not path.exists("webapp/" + DB_NAME):
        db.create_all(app=app)
        print("Database created!!")
