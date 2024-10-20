# Componentes que se utilizaran
from flask_login import UserMixin

# Clase en la que almacenamos los datos del usuario activo con UserMixin
class User(UserMixin) :

    def __init__(self, id, nombre, usuario) -> None:
        
        self.id = id
        self.nombre = nombre
        self.usuario = usuario

    # Usamos classmethod para no necesitar instaciar la funcion cada vez que se use
    @classmethod
    # Funcion con la que obtenemos el id y datos del usuario activo
    def get_by_id(self, db, id):
        
        # Cursor para manejar la base de datos
        cursor = db.cursor()
        # Sentencia SQL
        sql = "SELECT id, Nombre, Usuario FROM usuarios WHERE id = %s"
        cursor.execute(sql, (id,)) 
        row = cursor.fetchone() # Obtenemos los datos pedidos
        # Si row no esta vacio
        if row != None :
            # Retornamos los datos en las posiciones que no pide el User
            return User(row[0], row[1], row[2])
        else :
            # Si row esta vacio, devolvemos un None
            return None            