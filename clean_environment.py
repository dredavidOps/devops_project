from flask import Flask
import requests

app = Flask(__name__)

users = {}

requests.get('http://127.0.0.1:5000/stop_server')
requests.get('http://127.0.0.1:5001/stop_server')
