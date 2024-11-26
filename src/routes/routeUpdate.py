from flask import Blueprint ,render_template, redirect, url_for
from flask_login import login_required, current_user
from src.database.conectDB import db

main = Blueprint("update_blueprint", __name__)

@login_required
@main.route('', methods = ["GET", "POST"])
def update() :

    cursor = db.cursor()
    sql = "SELECT Nombre, Apellido, Gmail FROM usuarios WHERE id = %s"
    cursor.execute(sql, (current_user.id, ))
    row = cursor.fetchall()

    return render_template("auth/update.html", row = row)