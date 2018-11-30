from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object('config.Development')

db = SQLAlchemy(app)


# IMPORT ROUTES
from app.routes.main import index, hello
