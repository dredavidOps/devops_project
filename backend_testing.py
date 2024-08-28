import requests

# post a new user to the REST API using POST method
endpoint = requests.post("http://127.0.0.1:5000/users/1", json={"user_name": "Klein"})
if endpoint.ok:
    print(endpoint.json())

# checks if the posted user is in the database
endpoint = requests.get("http://127.0.0.1:5000/users/10")
if not endpoint.ok:
    print("something is wrong")
else:
    print(endpoint.json())
