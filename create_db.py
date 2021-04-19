import sqlite3
DB_STUDENT = "D:\\Project\\Radicali\\py_api_assignment\\.data\\EQUIPMENTS.db"

def get_db():
    conn = sqlite3.connect(DB_STUDENT)
    return conn


def create_tables():
    tables = [
        """CREATE TABLE IF NOT EXISTS EQUIPMENTS(
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                NAME TEXT NOT NULL,
				STATUS TEXT NOT NULL,
                REQUEST TEXT
            )
            """
    ]
    db = get_db()
    cursor = db.cursor()
    for table in tables:
        cursor.execute(table)

