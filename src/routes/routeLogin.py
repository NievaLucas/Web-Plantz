from flask import Blueprint, request, render_template, redirect, url_for, flash
from src.database.conectDB import db
from src.utils.security import check_password

main = Blueprint("login_blueprint", __name__)

@main.route('', methods = ["GET", "POST"])
def login():
    if request.method == "POST" :

        user = request.form["userDB"]
        password = request.form["passwordDB"]

        cursor = db.cursor()

        sql = "SELECT Usuario, Contraseña FROM usuarios WHERE Usuario = %s"
        cursor.execute(sql, (user,))
        infoDB = cursor.fetchall()

        if len(infoDB) > 0 and infoDB[0]:

            valuePassword = check_password(infoDB[0][1], password)

            if valuePassword : 
                return redirect(url_for('statistic_blueprint.esp32'))  
            else : 
                flash("Contraseña incorrecta")
                return render_template('auth/login.html')
        
        else : 
            flash("Usuario incorrecto")
            return render_template('auth/login.html')

    else :
        return render_template('auth/login.html')