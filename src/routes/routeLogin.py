from flask import Blueprint, request, render_template, redirect, url_for, flash

main = Blueprint("login_blueprint", __name__)

@main.route('', methods = ["GET", "POST"])
def login():
    if request.method == "POST" :
        user = request.form["userDB"]
        password = request.form["passwordDB"]

        return redirect(url_for('statistic_blueprint.esp32'))
    else :
        return render_template('auth/session.html')