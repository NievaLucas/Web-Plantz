from flask import Blueprint, request, render_template, redirect, url_for, flash

main = Blueprint("session_blueprint", __name__)

@main.route('/')
def login():
    if request.method == "POST" :
        print(request.form["userDB"])
        print(request.form["passwordDB"])
        return render_template('auth/session.html')
    else :
        return render_template('auth/session.html')