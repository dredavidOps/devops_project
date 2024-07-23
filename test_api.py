import requests
endpoint = requests.get("http://127.0.0.1:5001/get_user/1")
print(endpoint.json())
