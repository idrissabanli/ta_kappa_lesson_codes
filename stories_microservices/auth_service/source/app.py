from flask import Flask

app = Flask(__name__)

from models import *
from api.routers import *
