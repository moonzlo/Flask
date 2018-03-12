from wtforms import Form, StringField, TextAreaField

class PosstForm(Form):
    title = StringField('Title')
    body = TextAreaField('Body')
