import logging
import os

from flask import Flask
from flaskext.sqlalchemy import SQLAlchemy
from flaskext.markdown import Markdown

logging.basicConfig(level=logging.DEBUG)

HOST = "localhost"
app = Flask(__name__)
db = SQLAlchemy(app)

from .views.admin import admin
from .views.classes import classes
from .views.frontend import frontend
from .views.lessons import lessons
from .views.prover import prover
from .util import register_modules

register_modules(app, [admin, classes, frontend, lessons, prover])

app.secret_key = os.urandom(24)

# XXX: see if the db exists, if not make it and initialize
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'

# reconfigure app jinja enviroment
md = Markdown(app)
