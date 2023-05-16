from os import environ

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from exampractise.blueprints.user import auth_blueprint

# Create app instance
app = Flask(__name__)

if environ.get("CONFIG") == "production":
    app.config.from_object("config.ProdConfig")
    app.config['FLASK_DEBUG'] = 1
else:
    app.config.from_object("config.DevConfig")

# create SQLAlchemy instance
db = SQLAlchemy(app)

# create Migrate instance
migrate = Migrate(app, db)


# Register all blueprint
app.register_blueprint(auth_blueprint)

# Importing all models for migrations
from .models import AuthToken, User, UserType
