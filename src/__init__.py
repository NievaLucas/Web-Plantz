# Componentes que se utilizaran
from decouple import config
from flask import Flask, render_template
from flask_wtf import CSRFProtect
from src.routes import routeLogin, routeRegister, routeStatistic

# Declaracion de app
app = Flask(__name__, template_folder="templates")

# Componente con el cual protegeremos de ataques CSRF
csrf = CSRFProtect()

def createApp() :

    # Registro de blueprints de cada ruta    
    app.register_blueprint(routeRegister.main, url_prefix='/Registro')
    app.register_blueprint(routeLogin.main, url_prefix='/IniciarSesion')
    app.register_blueprint(routeStatistic.main, url_prefix='/Estadisticas')

    # Configuracion de llave secreta
    app.secret_key = config('SECRET_KEY')

    # Inicializador de la proteccion
    csrf.init_app(app)

    return app

# Renderizados que no necesitan de una ruta propia, ya que no necesitan logica por detras

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/Nosotros')
def us():
    return render_template('us.html')