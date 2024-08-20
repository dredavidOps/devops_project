from flask import Flask, jsonify
import os
import signal
import db_connector

app = Flask(__name__)

users = {}


@app.route('/stop_server')
def stop_server():
    os.kill(os.getpid(), signal.SIGINT)
    return 'Server Stopped'


@app.route('/hello')
def hello_user():
    return "<H1 id='welcome'>Welcome!</H1>"


@app.route('/users/<user_id>', methods=["GET"])
def get_user_name(user_id):
    user_name = db_connector.read_records(user_id)

    if user_name:
        return f"<h1 id='user'>{user_name}</h1>", 200
    else:
        return "<h1 id='error'>User ID not found</h1>", 400


if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True, port=5001)
