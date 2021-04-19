from flask import Flask, jsonify, request,render_template
import db_controller
from create_db import create_tables


app = Flask(__name__)
app.config["DEBUG"] = True

TOKEN = 1234 #Unique ID of the user

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

#List of all available softwares
@app.route(f'/student', methods=["GET"])
def get_eq_student():
    if int(request.args['key']) == TOKEN:
        eq = db_controller.get_eq_student()
        return jsonify(eq)

@app.route(f'/manager', methods=["GET"])
def get_eq_manager():
    if int(request.args['key']) == TOKEN:
        eq = db_controller.get_eq_manager()
        return jsonify(eq)

#Inserting values
@app.route(f"/manager/<name>", methods=["GET"])
def insert_eq(name):
    if int(request.args['key']) == TOKEN:
        result = db_controller.insert_eq(name, "Available", None)
        return jsonify(result)

#Student requesting
@app.route(f"/student/request/<id>", methods=["GET"])
def update_eq_student_request(id):
    print(request.args )
    if int(request.args['key']) == TOKEN:
        #print(request.args['id'])
        eq = db_controller.get_by_id(id)
        if eq[3] == None:
            status = "Requested"
            req = f"{TOKEN}"
            result = db_controller.update_eq_student(id, status, req)
            print(db_controller.get_by_id(id))
            return result
        else:
            return 'Not available'

#Student returning
@app.route(f"/student/return/<id>", methods=["GET"])
def update_eq_student_return(id):
    if int(request.args['key']) == TOKEN:
        eq = db_controller.get_by_id(id)
        if eq[2] == 'Available':
            return 'Equipment has not been issued.'
        elif eq[3] != f'{TOKEN}':
            return 'Not issued by the user.'
        status = "Available"
        req = None
        result = db_controller.update_eq_student(id, status, req)
        print(db_controller.get_by_id(id))
        return result
    return 'Invalid Token'

#Manager Approving Request
@app.route(f"/manager/request/<id>", methods=["GET"])
def update_eq_manager(id):
    if int(request.args['key']) == TOKEN:
        eq = db_controller.get_by_id(id)
        print(eq[3])
        if eq[3] == None:
            return 'Not requested'
        result = db_controller.update_eq_manager(int(id), "Issued", f"{TOKEN}")
        return jsonify(db_controller.get_by_id(id))

#Deleting values
@app.route(f"/delete/<id>", methods=["GET"])
def delete_eq(id):
    if int(request.args['key']) == TOKEN:
        result = db_controller.delete_eq(int(id))
        return jsonify(result)

#Get values by ID
@app.route(f"/<id>", methods=["GET"])
def get_eq_by_id(id):
    if int(request.args['key']) == TOKEN:
        eq = db_controller.get_by_id(int(id))
        return jsonify(eq)


@app.after_request
def after_request(response):
    response.headers["Access-Control-Allow-Origin"] = "*" # <- You can change "*" for a domain for example "http://localhost"
    response.headers["Access-Control-Allow-Credentials"] = "true"
    response.headers["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS, PUT, DELETE"
    response.headers["Access-Control-Allow-Headers"] = "Accept, Content-Type, Content-Length, Accept-Encoding, X-CSRF-Token, Authorization"
    return response


if __name__ == "__main__":
    create_tables()
    app.run(host='0.0.0.0', port=9000)