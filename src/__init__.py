# Componentes que se utilizaran
from decouple import config
from flask import Flask, render_template
from src.routes import routeLogin, routeRegister, routeStatistic

# Declaracion de app
app = Flask(__name__, template_folder="templates")

# Funcion donde se registraran todos los blueprints
def createApp() :
    
    app.register_blueprint(routeRegister.main, url_prefix='/Registro')
    app.register_blueprint(routeLogin.main, url_prefix='/IniciarSesion')
    app.register_blueprint(routeStatistic.main, url_prefix='/Estadisticas')

    app.secret_key = config('SECRET_KEY')

    return app

# Renderizados que no necesitan de una ruta propia, ya que no necesitan logica por detras

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/Nosotros')
def us():
    return render_template('us.html')