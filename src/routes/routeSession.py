from flask import Blueprint, request, render_template, redirect, url_for, flash
from src.models.modelsUser import init_user_db

main = Blueprint("session_blueprint", __name__)

@main.route('/')
def session():
    if request.method == "POST" :
        user = request.form["userDB"]
        password = request.form["passwordDB"]

        cursor = init_user_db.db.cursor()
        cursor.execute("SELECT Usuario from usuarios")
        userInDB = cursor.fetchall()

        cursor = init_user_db.db.cursor()
        cursor.execute("SELECT Contraseña from usuarios")
        passwordInDB = cursor.fetchall()

        if user in userInDB and password in passwordInDB :
            return redirect(url_for('statistic'))
        elif user not in userInDB and password in passwordInDB :
            flash("Usuario incorrecto")
        elif user in userInDB and password not in passwordInDB :
            flash("Contraseña incorrecta")
        else :
            flash("Error")

    return render_template('auth/session.html')