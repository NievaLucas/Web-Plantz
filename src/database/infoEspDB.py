import sqlite3
from flask import g, current_app

def get_infoESP32_db() :
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('/data/infoESP32.db')
    return db

@current_app.teardown_appcontext
def close_infoESP32_db() :
    with current_app().app_context():
        db = getattr(g, '_database', None)
        if db is not None:
            db.close()