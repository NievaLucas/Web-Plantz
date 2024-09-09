from flask import Flask, render_template

from src.routes import routeRegister, routeSession, routeStatistic
from src.models.modelsUser import init_user_db

app = Flask(__name__, template_folder="templates")

def createApp() :
    
<<<<<<< HEAD
    app.register_blueprint(routeRegister.main, method = ["POST"], url_prefix='/Registro')
    app.register_blueprint(routeSession.main, method = ["POST"], url_prefix='/IniciarSesion')
    app.register_blueprint(routeStatistic.main, method = ["GET", "POST"], url_prefix='/Estadisticas')
=======
    app.register_blueprint(routeRegister.main,  method = ["POST"], url_prefix='/Registro')
    app.register_blueprint(routeSession.main,  method = ["POST"], url_prefix='/IniciarSesion')
    app.register_blueprint(routeStatistic.main, method = ["POST", "GET"], url_prefix='/Estadisticas')
>>>>>>> 20c76b4339c488769f6c68371b0d0d30937801d8
    init_user_db(app)

    return app

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/Nosotros')
def us():
    return render_template('us.html')