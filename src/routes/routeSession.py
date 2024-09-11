from flask import Blueprint, request, render_template, redirect, url_for, flash

main = Blueprint("session_blueprint", __name__)

@main.route('/')
def session():
    if request.method == "POST" :
        user = request.form["userDB"]
        password = request.form["passwordDB"]

    return render_template('auth/session.html')