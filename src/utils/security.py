from werkzeug.security import generate_password_hash, check_password_hash

# Funcion con la que generamos un nuevo Hash
hash_password = lambda newPassword : generate_password_hash(newPassword)
    
# Funcion con la que verificamos que la contraseña hasheada y el texto plano son las mismas
check_password = lambda encoded, password : check_password_hash(encoded, password)