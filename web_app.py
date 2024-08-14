from flask import Flask
import os
import signal
import db_connector

app = Flask(__name__)


@app.route('/stop_server')
def stop_server():
    os.kill(os.getpid(), signal.SIGINT)
    return 'Server Stopped'


@app.route('/hello')
def hello_user():
    return "<H1 id='welcome'>Welcome!</H1>"


@app.route('/users/<user_id>')
def get_user_name(user_id):
    user_name = db_connector.read_records(user_id)
    if not user_name:
        return "<H1 id='error'>" + 'no such user' + user_id + "</H1>"
    else:
        return "<H1 id='user'>" + user_name + "</H1>"


if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True, port=5001)
