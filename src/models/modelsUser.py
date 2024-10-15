from flask_login import UserMixin

class User(UserMixin) :

    def __init__(self, id, nombre, usuario) -> None:
        
        self.id = id
        self.nombre = nombre
        self.usuario = usuario

    @classmethod
    def get_by_id(self, db, id):
        
        # Cursor para manejar la base de datos
        cursor = db.cursor()
        # Sentencia SQL
        sql = "SELECT id, Nombre, Usuario FROM usuarios WHERE id = %s"
        cursor.execute(sql, (id,)) 
        row = cursor.fetchone() #Obtenemos los datos pedidos

        if row != None :
            return User(row[0], row[1], row[2])
        else :
            return None            