from flask import Blueprint, request, render_template, redirect, url_for

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
    
        return redirect(url_for('statistic'))
    
    return render_template('/auth/register.html')