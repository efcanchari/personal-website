from os import environ, path

from flask import Flask
from flask_sqlalchemy import  SQLAlchemy
from flask_login import LoginManager
from sqlalchemy_utils.functions import database_exists

db = SQLAlchemy()

dbUser = environ.get('DB_USER')
dbPass = environ.get('DB_PASS')
dbServer = environ.get('DB_SERVER')
dbPort = environ.get('DB_PORT')
dbName = environ.get('DB_NAME')

webLog = "WEBSITE"

def create_app():
    app = Flask(__name__) #start flask
    # cookie pass
    app.config['SECRET_KEY']='ASDasdae323as'
    # database string
    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{dbUser}:{dbPass}@{dbServer}:{dbPort}/{dbName}'
    localDB = False

    print(f"{webLog}: Check DB Details....")
    if not database_exists(app.config["SQLALCHEMY_DATABASE_URI"]):
        print(f"{webLog}: We couldn't connect to {app.config['SQLALCHEMY_DATABASE_URI']}")
        localDB = True
    else:
        print(f"{webLog}: Connected to {app.config['SQLALCHEMY_DATABASE_URI']} success")

    #start database related to our Flask app
    print(f"{webLog}: Init_app on DB...")
    db.init_app(app)

    from .views import views #import global variables
    from .auth import auth   #import global variables

    app.register_blueprint(views,url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    if localDB:
        create_local_database(app)
    else:
        db.create_all(app=app)
        print(f'{webLog}: Created Postgre Database!')

    # import .models as models
    from .models import User
    from .models import Note

    print(f'{webLog}: Creating LoginManager!')
    # enable session and redirect when you are not login
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    # load user details
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

def create_local_database(app):
    # check db file exist
    if not path.exists(f'./{dbName}.db'):
        app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{dbName}.db'
        db.create_all(app=app)
        print(f'{webLog}: Created local Database!')



