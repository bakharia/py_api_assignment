from create_db import get_db


def insert_eq(name, status, request):
    db = get_db()
    cursor = db.cursor()
    statement = "INSERT INTO EQUIPMENTS(NAME, STATUS, REQUEST) VALUES (?, ?, ?)"
    cursor.execute(statement, [name, status, request])
    db.commit()
    return True

def search_student(name):
    db = get_db()
    cursor = db.cursor()
    like = f'%{name}%'
    statement = "SELECT ID, NAME FROM EQUIPMENTS WHERE NAME LIKE ? AND REQUEST IS NULL"
    cursor.execute(statement, [like]) 
    return cursor.fetchall()

def search_manager(name):
    db = get_db()
    cursor = db.cursor()
    like = f'%{name}%'
    statement = "SELECT * FROM EQUIPMENTS WHERE NAME LIKE ? "
    cursor.execute(statement, [like]) 
    return cursor.fetchall()

def update_eq_student(id, status, request):
    db = get_db()
    cursor = db.cursor()
    statement = "UPDATE EQUIPMENTS SET STATUS = ?, REQUEST = ? WHERE ID = ?"
    cursor.execute(statement, [status, request, id])
    db.commit()
    if request == None:
        return "Equipment Returned" 
    return "Equipment Requested"

def update_eq_manager(id, status, request):
    db = get_db()
    cursor = db.cursor()
    statement = "UPDATE EQUIPMENTS SET STATUS = ?, REQUEST = ? WHERE ID = ?"
    cursor.execute(statement, [status, request, id])
    db.commit()
    return True


def delete_eq(name):
    db = get_db()
    cursor = db.cursor()
    statement = "DELETE FROM EQUIPMENTS WHERE NAME =  ?"
    cursor.execute(statement, [name])
    db.commit()
    return True


def get_by_id(id):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT * FROM EQUIPMENTS WHERE ID = ?"
    cursor.execute(statement, [id])
    return cursor.fetchone()


def get_eq_student():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT ID, NAME FROM EQUIPMENTS WHERE REQUEST IS NULL"
    cursor.execute(query)
    return cursor.fetchall()

def get_eq_manager():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT ID, NAME, STATUS, REQUEST FROM EQUIPMENTS"
    cursor.execute(query)
    return cursor.fetchall()

def get_eq_manager_req():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT ID, NAME, STATUS, REQUEST FROM EQUIPMENTS WHERE REQUEST IS NOT NULL"
    cursor.execute(query)
    return cursor.fetchall()