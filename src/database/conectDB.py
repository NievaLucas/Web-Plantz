# Modulo conector con MySQL
import mysql.connector

# Variable con las credenciales para conectarse a la BBDD en la nube
db = mysql.connector.connect(

    host = "sql10.freemysqlhosting.net",
    user = "sql10734546",
    password = "1BHCaGxmuw",
    port = "3306",
    database = "sql10734546"

)