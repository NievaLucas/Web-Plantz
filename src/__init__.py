from flask import Flask, render_template

from src.routes import routeLogin, routeRegister, routeStatistic

app = Flask(__name__, template_folder="templates")

def createApp() :
    
    app.register_blueprint(routeRegister.main, url_prefix='/Registro')
    app.register_blueprint(routeLogin.main, url_prefix='/IniciarSesion')
    app.register_blueprint(routeStatistic.main, url_prefix='/Estadisticas')

    app.secret_key = "secret_key"

    return app

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/Nosotros')
def us():
    return render_template('us.html')