from werkzeug.security import generate_password_hash, check_password_hash

# Funcion con la que generamos un nuevo Hash
def hash_password(newPassword) :
    return generate_password_hash(newPassword)

# Funcion con la que verificamos que la contraseña hasheada y el texto plano son las mismas
def check_password(encoded, password) :
    return check_password_hash(encoded, password)