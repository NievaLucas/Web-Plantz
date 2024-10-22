# Componentes que se utilizaran
from decouple import config
from flask import Flask, render_template, redirect, url_for
from flask_login import logout_user
from flask_wtf import CSRFProtect
from src.routes import routeLogin, routeRegister, routeStatistic
from src.routes.routeLogin import LoginManagerApp

# Declaracion de app
app = Flask(__name__, template_folder="templates")

# Componente con el cual protegeremos de ataques CSRF
csrf = CSRFProtect()

# Renderizado de error HTTP 401
def status_401(error) :
    return render_template('error_401.html')

# Renderizado de error HTTP 404
def status_404(error) :
    return render_template('error_404.html')

# Funcion con todos los inicializadores necesarios
def createApp() :

    # Registro de blueprints de cada ruta    
    app.register_blueprint(routeRegister.main, url_prefix='/Registro')
    app.register_blueprint(routeLogin.main, url_prefix='/IniciarSesion')
    app.register_blueprint(routeStatistic.main, url_prefix='/Estadisticas')

    # Configuracion de llave secreta
    app.secret_key = config('SECRET_KEY')

    # Inicializador de la proteccion
    csrf.init_app(app)

    # Inicializamos el login
    LoginManagerApp.init_app(app)

    # Registro de error HTTP 401
    app.register_error_handler(401, status_401)

    # Registro de error HTTP 404
    app.register_error_handler(404, status_404)

    return app

# Renderizados que no necesitan de una ruta propia, ya que no necesitan logica por detras

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/Nosotros')
def us():
    return render_template('us.html')

@app.route('/')
def logout() :
    # Funcion con la que cerraremos sesion
    logout_user()
    return redirect(url_for('home'))