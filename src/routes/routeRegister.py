# Componentes que se utilizaran
from flask import Blueprint, request, render_template, redirect, url_for, flash
from src.database.conectDB import db
from src.utils.forms import Registro
from src.utils.security import hash_password

# Definicion del Blueprint
main = Blueprint("registers_blueprint", __name__)

# Ruta y los metodos permitidos
@main.route('', methods = ["GET", "POST"])
def registers() :
    form = Registro()
    if form.validate_on_submit() :
        
        name = form.name.data
        surname = form.surname.data
        gmail = form.gmail.data
        username = form.user.data
        passwordHash = hash_password(form.password.data)

        cursor = db.cursor()
        sql = """INSERT INTO usuarios (Nombre, Apellido, Gmail, Usuario, Contraseña) 
                VALUES (%s, %s, %s, %s, %s)"""
        cursor.execute(sql, (name, surname, gmail, username, passwordHash))
        db.commit()
       
        return redirect(url_for('login_blueprint.login'))
    # Si el metodo es GET renderizamos la plantilla
    else :
        return render_template('/auth/register.html', form = form)