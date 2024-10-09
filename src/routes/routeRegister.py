# Componentes que se utilizaran
from flask import Blueprint, request, render_template, redirect, url_for, flash
from src.database.conectDB import db
from src.utils.security import hash_password

# Definicion del Blueprint
main = Blueprint("registers_blueprint", __name__)

# Ruta y los metodos permitidos
@main.route('', methods = ["GET", "POST"])
def registers() :
    # Si el metodo del formulario es POST
    if request.method == "POST":
        # Se obtienen los datos del formulario
        name = request.form["name"]
        surname = request.form["surname"]
        gmail = request.form["gmail"]
        newUser = request.form["user"]
        newPassword = request.form["password"]
        # Tupla a evaluar
        valueNull = (name, surname, gmail, newUser, newPassword)
        # Si algun dato esta vacio
        if "" in valueNull :
            # Si devuelve verdadero notificamos el error
            flash("Todos los campos son obligatorios")
            return render_template('/auth/register.html')
        else :
            # Tupla a insertar en la base de datos
            insertToDB = (name, surname, gmail, newUser, hash_password(newPassword))
            # Sentencias de la base de datos
            sql = "INSERT INTO usuarios (Nombre, Apellido, Gmail, Usuario, Contraseña) VALUES (%s, %s, %s, %s, %s)"
            cursor = db.cursor()
            cursor.execute(sql, (insertToDB))
            db.commit()
            # Redireccionamos a la ruta de estadisticas si el registro fue exitoso
            return redirect(url_for('statistic_blueprint.esp32'))
    # Si el metodo es GET renderizamos la plantilla
    return render_template('/auth/register.html')