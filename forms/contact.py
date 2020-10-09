from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, SelectField, PasswordField, BooleanField, SubmitField
from wtforms.widgets import TextArea
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, InputRequired, Email, Length

class ContactForm(FlaskForm):
    subject = StringField('Username', [InputRequired("Please enter the subject"), Length(min=4, max=25)])
    kind_of_question = SelectField(u'Tipo de Consulta', choices=[
        ('hi', 'Say hi'),
        ('bussisness', 'Bussisness'),
        ('bug', 'Report a bug')
    ])
    email = EmailField(
        "Email",  
        validators=[
            InputRequired("Please enter your email address."),
            Email("This field requires a valid email address")
        ]
    )
    message = StringField(
        "Message", 
        # Validators
        validators=[
            InputRequired("Please enter your message here"),
            Length(min=125)
        ],
        widget=TextArea()
    )
    accept_tos = BooleanField('Acepto las condiciones de uso & política de privacidad', [InputRequired()])
    recaptcha = RecaptchaField()
    submit = SubmitField("Go")
