from src.database.userDB import get_infoUsers_db, close_infoUsers_db

def init_user_db(app):
    with app.app_context():
        db = get_infoUsers_db()
        
        close_infoUsers_db()