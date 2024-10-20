# Componentes que se utilizaran
from flask import Blueprint, request, render_template, redirect, url_for, flash
from flask_login import LoginManager, login_user
from src.database.conectDB import db
from src.models.modelsUser import User
from src.utils.security import check_password

# Definicion del Blueprint
main = Blueprint("login_blueprint", __name__)

# Variable que contiene el inicializador del login
LoginManagerApp = LoginManager()

# Funcion con la que cargamos los datos del usuario
@LoginManagerApp.user_loader
def load_user(id) :
    return User.get_by_id(db, id)

# Ruta y los metodos permitidos
@main.route('', methods = ["GET", "POST"])
def login():
    # Si el metodo del formulario es POST
    if request.method == "POST" :
        # Se obtienen los datos del formulario
        user = request.form["userDB"]
        password = request.form["passwordDB"]
        # Cursor para manejar la base de datos
        cursor = db.cursor()
        # Sentencia SQL
        sql = "SELECT id, Nombre, Usuario, Contraseña FROM usuarios WHERE Usuario = %s"
        cursor.execute(sql, (user,)) 
        row = cursor.fetchone() #Obtenemos los datos pedidos
        # Comprobacion de si obtuvimos datos
        if row :
            # A User le entregamos los datos que va a contener momentaneamente
            user = User(id = row[0], nombre = row[1], usuario = row[2])            
            """
            Con la funcion "ckeck_password" verificamos si
            el hash guardado y la contraseña coinciden
            esta devuelve un True o un False
            """
            valuePassword = check_password(row[3], password)
            # Si es verdadero
            if valuePassword :
                login_user(user)
                # Redireccionamos a la ruta de estadisticas si el loggin fue exitoso 
                return redirect(url_for('statistic_blueprint.esp32'))  
            else : 
                # En caso de no coincidir notificamos el error
                flash("Contraseña incorrecta")
                return render_template('auth/login.html')
        # En caso de no existir notificamos el error
        else : 
            flash("Usuario incorrecto")
            return render_template('auth/login.html')
    # Si el metodo es GET renderizamos la plantilla
    else :
        return render_template('auth/login.html')