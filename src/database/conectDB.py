from decouple import config
from flask import abort
# Modulo conector con MySQL
import mysql.connector

# Variable con las credenciales para conectarse a la BBDD en la nube

try : 
    db = mysql.connector.connect(

        host = config('MYSQL_HOST'),
        user = config('MYSQL_USER'),
        password = config('MYSQL_PASSWORD'),
        port = config('MYSQL_PORT'),
        database = config('MYSQL_DATABASE')
    )
# En caso de perder conexion con la BBDD, lanzamos un error HTTP 500
except :
    abort(500)