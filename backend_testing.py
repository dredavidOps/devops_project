import requests

# post a new user to the REST API using POST method
endpoint = requests.put("http://127.0.0.1:5001/update_user/12", json={"user_id": 12, "user_name": "Ian"})
if endpoint.ok:
    print(endpoint.text)

endpoint = requests.get("http://127.0.0.1:5001/get_user/12")
if not endpoint.ok:
    print(endpoint.json())
else:
    print("something is wrong")
