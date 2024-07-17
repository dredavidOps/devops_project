import requests
endpoint = requests.get("http://127.0.0.1:5001/get_user/1", json={"user_id":1, "user_name":"Pumba"})
print(endpoint.text)