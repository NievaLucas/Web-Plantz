from flask import Blueprint, request, render_template

main = Blueprint("statistic_blueprint", __name__)

@main.route('/')
def statistic():
    return render_template('statistic.html')