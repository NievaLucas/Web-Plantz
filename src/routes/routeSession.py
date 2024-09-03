from flask import Blueprint, request, render_template, redirect, url_for

main = Blueprint("session_blueprint", __name__)

@main.route('/')
def session():
    if request.method == "POST" :
        return redirect(url_for('statistic'))


    return render_template('auth/session.html')