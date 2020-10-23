from flask import Blueprint
routes = Blueprint('routes', __name__)

from .errors import *
from .general import *
from .accounts import *
from .auth.upload import *

