from flask_sqlalchemy import SQLAlchemy            
import datetime
from . import db
from flask_login import UserMixin

# Para buscar usuarios  
#User.query.filter_by(username='admsin').first_or_404(description='Go fuck yourself')
#

# Para hashear las passwords
#
#>>> from werkzeug.security import check_password_hash as checkph
#>>> from werkzeug.security import generate_password_hash as genph
#>>> # Guardamos en una variable llamada hash_clave nuestra contraseña generada por Werkzeug
#... hash_clave = genph('12345')
#>>> # Ahora veamos que contraseña ha generado.
#... hash_clave
#'pbkdf2:sha256:50000$PLLuA5PF$30a9ef9efd6b6f799e6071b1013ca9fe53e31bcbb60359e9cab6c3c2fe82aa55'
#>>> # Pueden ver que ha generado una contraseña cifrando nuestra contraseña original '12345' #... # Ahora vamos a decirle que chequee la contraseña cifrada con la original, esto devuelve true si coinciden y false si no.
#... checkph(hash_clave, '12345')
#True
#>>> # Como vemos las verifica y devuelve true pero si le pasamos un valor distinto devolvera false
#... checkph(hash_clave, '123')
#False
#>>> # Ahora creemos un usario en la base de datos con esta contraseña cifrada
#... nuevoUsuario = Usuario(username = "jose19", email = "josemartinez@gmail.com", hash_clave = hash_clave)
#>>> bdd.session.add(nuevoUsuario)
#>>> bdd.session.commit()

# Para más info de que es UserMixin mirar
# https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-v-user-logins
class User(UserMixin, db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String, unique=True, nullable=False)
  email = db.Column(db.String, unique=True, nullable=False)
  # 0(false), 1(true)
  email_confirmed = db.Column(db.Boolean) 
  karma = db.Column(db.Integer, nullable=True)
  desc = db.Column(db.String, nullable=True)
  posts = db.Column(db.Integer, nullable=True)
  created_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
  hash_password = db.Column(db.String, nullable=False)
  banned = db.Column(db.Boolean, nullable=True)
  admin = db.Column(db.Boolean)
