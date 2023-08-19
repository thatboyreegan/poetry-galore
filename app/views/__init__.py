from flask import Blueprint

accounts = Blueprint("accounts", __name__)

from .register import *
from .login import *
