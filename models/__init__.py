from flask_sqlalchemy import SQLAlchemy

# Primero tengo que declarar esto sino users.py no 
# podría tener acceso a esta variable
db = SQLAlchemy()

# Ahora importo todas las funciones de users 
from .users import *
from .posts import *
