# Componentes que se utilizaran
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

# Clase que contiene los campos del formulario con FlaskForm
class Registro(FlaskForm) :
    
    # Cada campo con sus validaciones necesarias
    name = StringField("name", validators = [DataRequired()])
    surname = StringField("surname", validators = [DataRequired()])
    gmail = StringField("gmail", validators = [DataRequired(), Email()])
    user = StringField("user", validators = [DataRequired(), Length(min = 6)])
    password = PasswordField("password", validators = [DataRequired(), Length(min = 6)])
    submit = SubmitField("submit")