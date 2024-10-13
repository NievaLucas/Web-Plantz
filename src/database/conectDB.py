from decouple import config
# Modulo conector con MySQL
import mysql.connector

# Variable con las credenciales para conectarse a la BBDD en la nube
db = mysql.connector.connect(

    host = config('MYSQL_HOST'),
    user = config('MYSQL_USER'),
    password = config('MYSQL_PASSWORD'),
    port = config('MYSQL_PORT'),
    database = config('MYSQL_DATABASE')

)