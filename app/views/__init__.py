from flask import Blueprint

from .register import *
from .login import *

accounts = Blueprint("accounts", __name__)
