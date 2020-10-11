from flask import Flask
# A diferencia de (import routes) usando from routes import *
# podes acceder a las funciones directamente sin el prefijo
from routes import *
# Cuando hago esto estoy llamando al archivo __init__ de la
# carpeta models
from models import *
from auth import *
from flask_script import Manager
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flashlightning.db'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@server/db
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'adam$@bjorkdogsandcatsBm1O5s_p#y#r,AH13Q3XXsolP*faХ#3radianteaХ#3'

app.config['RECAPTCHA_PUBLIC_KEY'] = '6Leyw88ZAAAAAMuYs49e-NQ5F-_xIR3XHqz0_5I9'
app.config['RECAPTCHA_PRIVATE_KEY'] ='6Leyw88ZAAAAAP59I0IdLQoZvcyO5_9Z6ngQZKlk'

app.config['UPLOAD_FOLDER'] = 'static/user_data/'
migrate = Migrate()

db.init_app(app)
migrate.init_app(app, db)
app.register_blueprint(routes)
login_manager.init_app(app)


@login_manager.unauthorized_handler
def unauthorized_callback():
    return redirect('/login')


if __name__ == '__main__':
    app.run(debug=True)
