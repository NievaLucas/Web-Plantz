from flask import Blueprint, request, render_template, redirect, url_for
from src.database.userDB import connUser

main = Blueprint("registers_blueprint", __name__)

@main.route('', methods = ["GET", "POST"])
def registers() :
    if request.method == "POST":
        name = request.form["name"]
        surname = request.form["surname"]
        gmail = request.form["gmail"]
        newUser = request.form["user"]
        newPassword = request.form["password"]
        insertToBD = (name, surname, gmail, newUser, newPassword)
        
        #sql = "INSERT INTO usuarios (Nombre, Apellido, Gmail, Usuario, Contraseña) VALUES (?, ?, ?, ?, ?)"

        #cursor = connUser.cursor()
        #cursor.execute(sql, insertToBD)
        #connUser.commit()
        
        return redirect(url_for('statistic_blueprint.esp32'))
    
    return render_template('/auth/register.html')