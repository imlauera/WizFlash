from wtforms.validators import ValidationError

class Unique(object):
    def __init__(self, model, field, message=u'This element already exists.'):
        self.model = model
        self.field = field
        self.message = message

    def __call__(self, form, field):
        #User.query.filter(User.email == 'dresuer@gmail.com').first()
        #No entiendo de donde sale field.data
        #Esta parte de código lo saqué de https://uniwebsidad.com/libros/explore-flask/chapter-11/flask-wtf
        print("La variable [field.data] me la pasa wtforms automaticamente creo y vale {}".format(field.data))
        check = self.model.query.filter(self.field == field.data).first()
        if check:
            raise ValidationError(self.message)
