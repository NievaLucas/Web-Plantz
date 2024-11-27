# Componentes que se utilizaron
from flask import Blueprint ,render_template, redirect, url_for
from flask_login import login_required, current_user
from src.database.conectDB import db
from src.utils.forms import Registro
from src.utils.security import hash_password

# Definicion del Blueprint
main = Blueprint("update_blueprint", __name__)

# Ruta y los metodos permitidos
@main.route('', methods = ["GET", "POST"])
@login_required # Ruta que requiere un usuario para ingresar a la vista
def update() :
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
        # Sentecia SQL con la que modificamos los datos del usuario en la base de datos
        sql = """UPDATE usuarios SET Nombre = %s, Apellido = %s, Gmail = %s, Usuario = %s, Contraseña = %s 
                WHERE id = %s"""
        cursor.execute(sql, (name, surname, gmail, username, passwordHash, current_user.id))
        db.commit()

        # Redireccionamos a la misma plantilla
        return redirect(url_for("update_blueprint.update"))

    # Por defecto, cargamos la plantilla con el formulario y los datos ya existentes
    else : 

        cursor = db.cursor()
        sql = "SELECT Nombre, Apellido, Gmail, Usuario FROM usuarios WHERE id = %s"
        cursor.execute(sql, (current_user.id, ))
        row = cursor.fetchall()

        return render_template("auth/update.html", form = form, row = row)