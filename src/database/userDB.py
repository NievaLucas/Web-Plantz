import sqlite3
from flask import g, current_app

def get_infoUsers_db() :
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('/data/infoUser.db')
    return db

@current_app.teardown_appcontext
def close_infoUsers_db() :
    with current_app().app_context():
        db = getattr(g, '_database', None)
        if db is not None:
            db.close()