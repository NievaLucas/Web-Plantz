from flask import Blueprint, request, render_template, redirect, url_for, flash
from src.database.conectDB import db
from src.utils.security import hash_password

main = Blueprint("registers_blueprint", __name__)

@main.route('', methods = ["GET", "POST"])
def registers() :
    if request.method == "POST":
        name = request.form["name"]
        surname = request.form["surname"]
        gmail = request.form["gmail"]
        newUser = request.form["user"]
        newPassword = request.form["password"]
        insertToBD = (name, surname, gmail, newUser, hash_password(newPassword))
        
        for i in insertToBD :
            if i == "" :
                flash("Llenar todos los campos")
                return render_template('/auth/register.html')
            else :
                sql = "INSERT INTO usuarios (Nombre, Apellido, Gmail, Usuario, Contraseña) VALUES (%s, %s, %s, %s, %s)"
                cursor = db.cursor()
                cursor.execute(sql, (insertToBD))
                db.commit()
                return redirect(url_for('statistic_blueprint.esp32'))
        
    return render_template('/auth/register.html')