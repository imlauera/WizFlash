from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, BooleanField
from wtforms.fields.html5 import EmailField
from wtforms.validators import *

app = Flask(__name__)
app.secret_key = 'very secret, change to something random'

class MyForm(FlaskForm):
  username = StringField("Name",  [InputRequired("Please enter your name.")])
  email = StringField("Email",  [InputRequired("Please enter your email address."), Email("This field requires a valid email address")])
  ipv4 = StringField("IPV4",  [InputRequired("Please enter your email address."), IPAddress("This field requires a valid email address")])
  recuerdame = BooleanField("Recuerdame")
  submit = SubmitField("Send")

@app.route('/submit', methods=('GET', 'POST'))
def submit():
    form = MyForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('register.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
