from flask_wtf import FlaskForm
from flask_wtf import RecaptchaField

from wtforms import (
    StringField,
    SelectField,
    PasswordField,
    BooleanField,
    SubmitField,
)
from wtforms.fields.html5 import EmailField
from wtforms.validators import (
    DataRequired,
    InputRequired,
    Email,
    Length,
    EqualTo,
)
from wtforms.widgets import TextArea
from flask_wtf.file import (
    FileField,
    FileRequired,
    FileAllowed,
)
from util.validators import Unique
from models import User


class LoginForm(FlaskForm):
    '''
        email = EmailField("Email",
            [
                InputRequired("Please enter your email address."),
                Email("This field requires a valid email address")
            ]
        )
    '''
    username = StringField(
        'Username',
        validators=[
            InputRequired("Please enter your username."),
        ]
    )
    password = PasswordField(
        "Password",
        [
            InputRequired("Please enter your password.")
        ]
    )
    remember = BooleanField("Remember me")
    recaptcha = RecaptchaField("Are you real?")
    submit = SubmitField("Go")


class RegisterForm(FlaskForm):
    username = StringField(
        'Username',
        validators=[
            InputRequired("Please enter your username."),
            Length(min=4, max=25),
            Unique(
                User,
                User.username,
                message='There is already an account with that username.'
            )
        ]
    )
    password = PasswordField('New Password', [
      DataRequired(),
      EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    '''
        accept_emails = BooleanField(
            'Quiero recibir correos sobre novedades de ThunderNetwork'
        )
    '''
    accept_tos = BooleanField(
        'Acepto las condiciones de uso',
        [DataRequired()]
    )
    recaptcha = RecaptchaField("Are you real?")
    submit = SubmitField("Go")


class UploadForm(FlaskForm):
    subject = StringField(
        'Título',
        validators=[
            InputRequired("Por favor ingrese el nombre del negocio"),
            Length(min=3)
        ]
    )
    desc = StringField(
        "Descripción",
        [
            InputRequired("""Por favor ingrese una
                          pequeña descripción de su negocio."""),
            Length(min=5)
        ],
        widget=TextArea()
    )
    category = SelectField(
        'Categoría',
        [
            InputRequired()
        ],
        choices=[("", "Elegir categoría")]
    )
    hidden = BooleanField('Hidden?')
    tags = StringField('Tags (separado por espacios)', [InputRequired()])
    files = FileField(
        'Archivo',
        [
            FileRequired(),
            FileAllowed(
                [
                    'webm',
                    'mp4',
                    'jpg',
                    'png',
                    'gif',
                    'jpeg',
                    'svg'
                ],
                """Sólo archivos jpg, png, gif,
                jpeg, mp4, webm están permitidos!"""
            )
        ],
        # widget=FileInput(multiple=True, accept=['image/*'])
    )
    # recaptcha = RecaptchaField("Are you real?")
    submit = SubmitField("Upload")


class DeleteForm(FlaskForm):
    accept = BooleanField(
        'Estoy seguro que quiero borrar esto',
        [DataRequired()]
    )
    # recaptcha = RecaptchaField()
    submit = SubmitField("Borrar")


class DeleteCommentForm(FlaskForm):
    accept = BooleanField(
        'Estoy seguro que quiero borrar esto',
        [DataRequired()]
    )
    # recaptcha = RecaptchaField()
    submit = SubmitField("Borrar")


class CommentForm(FlaskForm):
    subject = StringField(
        'Título'
    )
    comment = StringField(
        'Comentario',
        validators=[
            InputRequired()
        ],
        widget=TextArea()
    )
    password = StringField(
        'Contraseña',
        validators=[
            InputRequired()
        ]
    )
    file = FileField(
        'Archivo',
        [
            FileAllowed(
                [
                    'webm',
                    'mp4',
                    'jpg',
                    'png',
                    'gif',
                    'jpeg',
                    'svg'
                ],
                """Sólo archivos jpg, png, gif,
                jpeg, mp4, webm están permitidos!"""
            )
        ],
        # widget=FileInput(multiple=True, accept=['image/*'])
    )
    # recaptcha = RecaptchaField()
    submit = SubmitField("Comentar")


class ProfileForm(FlaskForm):
    username = StringField(
        'Username'
    )
    email = EmailField(
        "Email",
        validators=[
            Email("This field requires a valid email address")
        ]
    )
    desc = StringField(
        "Message",
        # Validators
        validators=[
            InputRequired("Please enter your message here"),
            Length(min=5)
        ],
        widget=TextArea()
    )
    # recaptcha = RecaptchaField()
    submit = SubmitField("Go")


class CreateCategoryForm(FlaskForm):
    category = StringField('Nombre', [InputRequired()])
    recaptcha = RecaptchaField("Are you real?")
    submit = SubmitField("Crear")


class ThankPostForm(FlaskForm):
    accept = BooleanField('Quiero agradecer a este post', [DataRequired()])
    # recaptcha = RecaptchaField("Are you real?")
    submit = SubmitField("Agradecer")


class ThankUserForm(FlaskForm):
    accept = BooleanField(
        'Estoy seguro que quiero agradecer a este usuario',
        [DataRequired()]
    )
    # recaptcha = RecaptchaField("Are you real?")
    submit = SubmitField("Agradecer")


class LikeForm(FlaskForm):
    accept = BooleanField('Me gusta esta publicación', [DataRequired()])
    recaptcha = RecaptchaField("Are you real?")
    submit = SubmitField("Like")


class ResetForm(FlaskForm):
    email = EmailField(
        "Email",
        [
            InputRequired("Please enter your email address."),
            Email("This field requires a valid email address")
        ]
    )

    recaptcha = RecaptchaField("Are you real?")
    submit = SubmitField("Go")
