from flask import Blueprint, request, render_template, redirect, url_for, flash
from src.database.userDB import connUser

main = Blueprint("login_blueprint", __name__)

@main.route('', methods = ["GET", "POST"])
def login():
    if request.method == "POST" :
        user = request.form["userDB"]
        password = request.form["passwordDB"]
        date = (user, password)

        cursor = connUser.cursor()
        sql = "SELECT Usuario, Contraseña FROM usuarios WHERE Usuario = %s AND Contraseña = %s"
        cursor.execute(sql, (date))
        account = cursor.fetchall()

        if account :
            return redirect(url_for('statistic_blueprint.esp32'))
        
    else :
        return render_template('auth/login.html')