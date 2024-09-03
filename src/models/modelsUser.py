from src.database.userDB import get_infoUsers_db

cursorUsers = get_infoUsers_db().cursor()

commitUsers = get_infoUsers_db().commit()