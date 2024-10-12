# Componentes que se utilizaran
from flask import Blueprint, request, render_template, redirect, url_for, flash
from src.database.conectDB import db
from src.utils.security import check_password

# Definicion del Blueprint
main = Blueprint("login_blueprint", __name__)

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
        sql = "SELECT Usuario, Contraseña FROM usuarios WHERE Usuario = %s"
        cursor.execute(sql, (user,)) 
        infoDB = cursor.fetchall() #Obtenemos los datos pedidos
        # Comprobacion de si el usuario existe o es incorrecto
        if len(infoDB) > 0 and infoDB[0]:
            """
            Con la funcion "ckeck_password" verificamos si
            el hash guardado y la contraseña coinciden
            esta devuelve un True o un False
            """
            valuePassword = check_password(infoDB[0][1], password)
            # Si es verdadero
            if valuePassword :
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