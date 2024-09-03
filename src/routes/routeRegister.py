from flask import Blueprint, request, render_template, redirect, url_for
# from models.modelsUser import cursorUsers, commitUsers

main = Blueprint("registers_blueprint", __name__)

@main.route('/')
def registers() :
    if request.method == "POST":
        #name = request.form["name"]
        #surname = request.form["surname"]
        #gmail = request.form["gmail"]
        #user = request.form["user"]
        #password = request.form["password"]
        #insertToBD = {name, surname, gmail, user, password}
    
        return redirect(url_for('statistic'))
    
    return render_template('/auth/register.html')