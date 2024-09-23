from werkzeug.security import generate_password_hash, check_password_hash

def hash_password(newPassword) :
    password = generate_password_hash(newPassword)
    return password

def check_password(encoded, password) :
    check_password_hash(encoded, password)