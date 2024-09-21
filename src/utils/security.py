from werkzeug.security import generate_password_hash

def hash_password(newPassword) :
    password = generate_password_hash(newPassword)
    return password