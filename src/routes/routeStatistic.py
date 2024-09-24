from flask import Blueprint, render_template, request
from src.database.infoEspDB import connEsp32

main = Blueprint("statistic_blueprint", __name__)

@main.route('', methods = ["GET", "POST"],)
def esp32():

    if request.method == "POST" :    

        idProducto = request.form["idEsp32"] 
    
        cursorEsp32 = connEsp32.cursor()
        sql = "SELECT Hora, Temperatura, Humedad FROM esp32 WHERE idProducto = %s"    
        cursorEsp32.execute(sql, (idProducto, ))
        datosEsp32 = cursorEsp32.fetchall()
        
        datoslal = ("sas", "sas", "sas")
        if idProducto == "sas" :
            return render_template('statistic.html', datosEsp32 = datoslal)
    
    else :
        return render_template('statistic.html')