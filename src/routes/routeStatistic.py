from flask import Blueprint, render_template, request, flash
from src.database.conectDB import db

main = Blueprint("statistic_blueprint", __name__)

@main.route('', methods = ["GET", "POST"],)
def esp32():

    if request.method == "POST" :    

        idProducto = request.form["idEsp32"] 
    
        cursor = db.cursor()
        sql = "SELECT Hora, Temperatura, Humedad FROM esp32 WHERE idProducto = %s ORDER BY id DESC"    
        cursor.execute(sql, (idProducto, ))
        datosEsp32 = cursor.fetchall()
    
        if datosEsp32 :
            return render_template('statistic.html', datosEsp32 = datosEsp32)
        else :
            flash("Id inexistente")
            return render_template('statistic.html')
        
    else :
        return render_template('statistic.html')