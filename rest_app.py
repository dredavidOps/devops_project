from flask import Flask, request, jsonify
import db_connector

app = Flask(__name__)


# function to assign call functions to methods - POST, GET, PUT AND DELETE data
@app.route("/user/<user_id>", methods=["POST", "GET", "PUT", "DELETE"])
def route_reporter(user_id):
    try:
        if request.method == "POST":
            return user_add(user_id)
        elif request.method == "GET":
            return get_user(user_id)
        elif request.method == "PUT":
            return update_user(user_id)
        elif request.method == "DELETE":
            return delete_user(user_id)
    except Exception as e:
        return jsonify({"status": "error", "reason": str(e)}), 500


# POST method to add users to the database
@app.route("/add_user/", methods=["POST"])
def user_add(user_id):
    try:
        user_name = request.json.get("user_name")
        if not user_name:
            raise ValueError("id already exists")

        # adding user to the database
        db_connector.create_records(user_id, user_name)

        return jsonify({"status": "ok", "user_added": user_name}), 200
    except ValueError as e:
        return jsonify({"status": "error", "reason": str(e)}), 500


# GET method to pull user data from the database
@app.route("/get_user/<user_id>", methods=["GET"])
def get_user(user_id):
    try:
        result = db_connector.read_records(user_id)
        if result:
            # return jsonify({"status": "error", "reason": "user not found"}), 404
            return jsonify({"status": "ok", "user": user_id}), 200
        if not result:
            return jsonify({"status": "error", "reason": "user not found"}), 404
    except Exception as e:
        return jsonify({"status": "error", "reason": "no such id"}), 500


# PUT method to update user data
@app.route("/update_user/<user_id>", methods=["PUT"])
def update_user(user_id):
    try:
        user_name = request.json.get("user_name")
        if not user_name:
            raise ValueError("user_name is required")

        # updating user id and adding it to the database
        updated_result = (db_connector.update_records(user_id, user_name))
        if updated_result:
            return jsonify({"status": "ok", "user": user_id}), 200
    except Exception as e:
        return jsonify({"status": "error", "reason": str(e)}), 500


# DELETE method to delete user data
@app.route("/delete_user/<user_id>", methods=["DELETE"])
def delete_user(user_id):
    try:
        deleted = db_connector.delete_records(user_id)
        if not deleted:
            return jsonify({"status": "error", "reason": "user not found"}), 404
        return jsonify({"status": "ok", "user_deleted": user_id}), 200
    except Exception as e:
        return jsonify({"status": "error", "reason": str(e)}), 500


app.run(host='127.0.0.1', debug=True, port=5001)
