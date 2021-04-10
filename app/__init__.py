from flask import Flask
from flask_wtf import csrf
from app.config import Config
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
csrf = CSRFProtect(app)

app.config.from_object(Config)

from app import views
