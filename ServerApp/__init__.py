from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('ServerApp.setting')
db = SQLAlchemy(app)

pw = "12345"

from ServerApp.controller import WebManager