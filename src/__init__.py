from flask import Flask, render_template

from src.routes import routeRegister, routeSession, routeStatistic
from src.models.modelsUser import init_user_db

app = Flask(__name__, template_folder="templates")

def createApp() :
    
    app.register_blueprint(routeRegister.main, methods = ["POST"], url_prefix='/Registro')
    app.register_blueprint(routeSession.main, methods = ["POST"], url_prefix='/IniciarSesion')
    app.register_blueprint(routeStatistic.main, methods = ["GET", "POST"], url_prefix='/Estadisticas')
    init_user_db(app)

    return app

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/Nosotros')
def us():
    return render_template('us.html')