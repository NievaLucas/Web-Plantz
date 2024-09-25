from flask import Blueprint, request, render_template, redirect, url_for, flash
from src.database.userDB import connUser
# from src.utils.security import check_password

main = Blueprint("login_blueprint", __name__)

@main.route('', methods = ["GET", "POST"])
def login():
    if request.method == "POST" :
        user = request.form["userDB"]
        password = request.form["passwordDB"]
        infoTuple = (user, password)

        cursor = connUser.cursor()

        sql = "SELECT Usuario, Contraseña FROM usuarios WHERE Usuario = %s AND Contraseña = %s"
        cursor.execute(sql, (infoTuple))
        infoDB = cursor.fetchall()

        if infoDB :
                return redirect(url_for('statistic_blueprint.esp32'))  
        else :
            flash("Algun dato es incorrecto")
            return render_template('auth/login.html')
    else :
        return render_template('auth/login.html')