# Componentes que se utilizaron
from flask import Blueprint, redirect, url_for
from flask_login import login_required, current_user
from src.database.conectDB import db

# Definicion del Blueprint
main = Blueprint("delete_blueprint", __name__)

@main.route('')
@login_required # Ruta que requiere un usuario para ingresar a la vista
def delete() :

    cursor = db.cursor()
    # Sentencia SQL con la que borramos al usuario
    sql = "DELETE FROM usuarios WHERE id = %s"
    cursor.execute(sql, (current_user.id, ))
    db.commit()

    # Redireccionamos a logout
    return redirect(url_for("logout"))