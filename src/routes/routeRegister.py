# Componentes que se utilizaran
from flask import Blueprint, render_template, redirect, url_for
from src.database.conectDB import db
from src.utils.forms import Registro
from src.utils.security import hash_password

# Definicion del Blueprint
main = Blueprint("registers_blueprint", __name__)

# Ruta y los metodos permitidos
@main.route('', methods = ["GET", "POST"])
def registers() :
    # Traemos la clase Registro, la cual contiene el formulario
    form = Registro()
    # Si el submit del formulario es valido (Es decir: True)
    if form.validate_on_submit() :
        
        # Obtenemos cada dato del formulario
        name = form.name.data
        surname = form.surname.data
        gmail = form.gmail.data
        username = form.user.data
        # Hasheado de contraseña
        passwordHash = hash_password(form.password.data)

        cursor = db.cursor()
        # Sentecia SQL con la que ingresamos el nuevo registro a la base de datos
        sql = """INSERT INTO usuarios (Nombre, Apellido, Gmail, Usuario, Contraseña) 
                VALUES (%s, %s, %s, %s, %s)"""
        cursor.execute(sql, (name, surname, gmail, username, passwordHash))
        db.commit()
       
        # Redireccionamos a Login
        return redirect(url_for('login_blueprint.login'))
    
    # Sino, renderizamos la plantilla y el formulario que contiene la clase Registro
    else :
        return render_template('/auth/register.html', form = form)