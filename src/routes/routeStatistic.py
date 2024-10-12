# Componentes que se utilizaran
from flask import Blueprint, render_template, request, flash
from src.database.conectDB import db

# Definicion del Blueprint
main = Blueprint("statistic_blueprint", __name__)

# Ruta y los metodos permitidos
@main.route('', methods = ["GET", "POST"],)
def esp32():
    # Si el metodo del formulario es POST
    if request.method == "POST" :    
        # Se obtienen los datos del formulario
        idProducto = request.form["idEsp32"] 
        # Cursor para manejar la base de datos
        cursor = db.cursor()
        # Sentencia SQL
        sql = "SELECT Hora, Temperatura, Humedad FROM esp32 WHERE idProducto = %s ORDER BY id DESC"    
        cursor.execute(sql, (idProducto, ))
        datosEsp32 = cursor.fetchall() # Obtenemos los datos pedidos
        # Si la id es existente y contiene los datos pedidos    
        if datosEsp32 :
            # Renderizamos la misma plantilla con los datos obtenidos
            return render_template('statistic.html', datosEsp32 = datosEsp32)
        else :
            # En caso de no existir el id notificamos el error
            flash("Id inexistente")
            return render_template('statistic.html')
    # Si el metodo es GET renderizamos la plantilla
    else :
        return render_template('statistic.html')