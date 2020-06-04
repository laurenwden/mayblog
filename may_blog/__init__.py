from flask import Flask

from config import Config  # config tells our operating system were to find everything that we run

# Import for Flask Db and Migrator
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

#Import for Flask Mail
from flask_mail import Mail, Message

from flask_login import LoginManager

# Create flask app variable 
app = Flask(__name__)  #because we've imported flask, we have to give it a new name)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)  #app must be first, db second

mail = Mail(app)
#import for routes to start and then models when we start using db for this

#Login Config
login = LoginManager(app)
login.login_view = 'login'

from may_blog import routes,models

