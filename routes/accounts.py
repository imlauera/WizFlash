from flask import render_template, redirect, url_for, request, flash, abort
#from util.security import is_safe_url
# Con esta linea estoy importando la variable routes de __init__.py
from . import routes
import datetime
from models import *
# https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-v-user-logins

from forms import LoginForm, RegisterForm, ResetForm, ProfileForm
#from util import ts, send_email
from flask_login import current_user, login_user, logout_user, login_required

from werkzeug.security import check_password_hash as checkph
from werkzeug.security import generate_password_hash as genph

@routes.route('/register/success')
def register_success():
    return '<h3>Ahora estás registrado.</h3><a href="/index">Home</a>';

@routes.route('/login/success')
def login_success():
    return '<h3>Recién ahora se validaron los datos pero todavía no estás logueado, acá tengo que chequear tus credenciales.</h3>';

@routes.route('/user/<username>')
def show_user(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('user/show_user.html', user=user)

@routes.route('/register/',methods=['GET','POST'])
def register():
    form = RegisterForm()
    print(form.errors)

    if form.is_submitted():
      print("submitted")

    #if form.validate():
      #print("valid")

    print(form.errors)
    print('Estoy acá1')

    if form.validate_on_submit():
        # No los puedo subir si están duplicados.
        user = User(
            username = form.username.data,
            hash_password = genph(form.password.data),
            karma = 0,
            posts = 0,
            email = form.email.data,
            email_confirmed = False,
            desc = "Este usuario aún no ha modificado su descripción.",
            banned = False,
            # date.today().isoformat()
            # created_date = date.today(),
            created_date = datetime.datetime.utcnow(),
            admin = False
        )
        db.session.add(user)
        db.session.commit()

        # Confirmación por correo algún dia lo voy a implementar
        '''
            subject = "Confirm your email"
            token = ts.dumps(form.email.data, salt='email-confirm-key')
            confirm_url = url_for(
                'confirm_email',
                token=token,
                _external=True
            )
            html = render_template(
                'email/activate.html',
                confirm_url=confirm_url
            )
            send_email(form.email.data, subject, html) 
        '''

        return redirect(url_for('routes.login',msg='Registrado! Ahora podés ingresar.'))
    return render_template('auth/register.html', form=form)

@routes.route('/login/',methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('routes.index'))

    form = LoginForm()
    print(form.errors)

    if form.is_submitted():
      print("submitted")

    print(form.errors)
    print('Estoy acá1')

    if request.method == 'POST' and form.validate():
        print(12341232134)
        user = User.query.filter_by(username=form.username.data).first()
        print(user)
        if user and checkph(user.hash_password, form.password.data):
            # https://flask-login.readthedocs.io/en/latest/
            login_user(user, remember=form.remember.data)
            # Sirve para redirigir a lo que el valor de next
            # este seteado, por ejemplo ?next=aboutus
            next = request.args.get("next")
            #if not is_safe_url(next):
            #if not (next):
            #    print("tu url no es safe: {}".format(next))
            #    return abort(400)
            #else:
            return redirect(next or url_for('routes.index'))
        else:
            flash("Login failed. Check your e-mail and password","danger")

    msg = request.args.get('msg')
    return render_template('auth/login.html', form=form, msg=msg)

@routes.route('/reset',methods=['GET','POST'])
def reset():
    form = ResetForm()
    print(form.errors)

    if form.is_submitted():
      print("submitted")

    #if form.validate():
      #print("valid")

    print(form.errors)
    print('Estoy acá1')
    #print(form.validate_on_submit())
    if form.validate_on_submit():
      print('Estoy acá2')
      return '<h4>Por el momento el recover password no esta implementado y no creo que lo este en por un tiempo largo</h4>';
    return render_template('auth/reset.html', form=form)


@routes.route("/settings/")
@login_required
def settings():
    return redirect(url_for('routes.profile'))

# Sacar POST
@routes.route("/settings/profile", methods=['GET'])
@login_required
def profile():
    form = ProfileForm()
    form.username.data = current_user.username
    form.email.data = current_user.email
    form.desc.data = current_user.desc
    print(form.errors)
    if form.validate_on_submit():
      return '<h4>Aún no implementado</h4>';

    return render_template('user/profile.html', form=form)

@routes.route("/settings/profile/edit", methods=['GET','POST'])
@login_required
def profile_edit():
    return render_template('user/profile_edit.html')

@routes.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('routes.index'))
