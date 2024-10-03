from flask import Blueprint, request, render_template, redirect, url_for, flash
from src.database.conectDB import db

main = Blueprint("login_blueprint", __name__)

@main.route('', methods = ["GET", "POST"])
def login():
    if request.method == "POST" :
        user = request.form["userDB"]
        password = request.form["passwordDB"]
        infoTuple = (user, password)

        cursor = db.cursor()

        sql = "SELECT Usuario, Contraseña FROM usuarios WHERE Usuario = %s AND Contraseña = %s"
        cursor.execute(sql, (infoTuple))
        infoDB = cursor.fetchall()

        for i in infoTuple :
            if i in "" :
                flash("Los campos estan vacios")
                return render_template('auth/login.html')
            else :
                if infoDB :
                    return redirect(url_for('statistic_blueprint.esp32'))  
                else :
                    flash("Algun dato es incorrecto")
                    return render_template('auth/login.html')

    else :
        return render_template('auth/login.html')