from flask import Blueprint, render_template

main = Blueprint("statistic_blueprint", __name__)

@main.route('')
def esp32():
    return render_template('statistic.html')