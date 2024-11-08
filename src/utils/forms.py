from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class Registro(FlaskForm) :
    
    name = StringField("name", validators = [DataRequired()])
    surname = StringField("surname", validators = [DataRequired()])
    gmail = StringField("gmail", validators = [DataRequired(), Email()])
    user = StringField("user", validators = [DataRequired(), Length(min = 6)])
    password = PasswordField("password", validators = [DataRequired(), Length(min = 6)])
    submit = SubmitField("submit")