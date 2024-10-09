from werkzeug.security import generate_password_hash, check_password_hash

def hash_password(newPassword) :
    return generate_password_hash(newPassword)

def check_password(encoded, password) :
    return check_password_hash(encoded, password)