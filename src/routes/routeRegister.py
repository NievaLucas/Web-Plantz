from flask import Blueprint, request, render_template, redirect, url_for
from src.models.modelsUser import init_user_db

main = Blueprint("registers_blueprint", __name__)

@main.route('/')
def registers() :
    if request.method == "POST":
        name = request.form["name"]
        surname = request.form["surname"]
        gmail = request.form["gmail"]
        newUser = request.form["user"]
        newPassword = request.form["password"]
        insertToBD = (name, surname, gmail, newUser, newPassword)
        cursor = init_user_db().db.cursor()
        cursor.execute("INSERT INTO usuarios (Nombre, Apellido, Gmail, Usuario, Contraseña) VALUES (?, ?, ?, ?, ?)", insertToBD)
        init_user_db().db.commit()
        return redirect(url_for('statistic'))
    
    return render_template('/auth/register.html')