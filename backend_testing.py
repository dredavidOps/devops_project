import requests

# post a new user to the REST API using POST method
endpoint = requests.post("http://127.0.0.1:5000/users/17", json={"user_name": "Nate"})
if endpoint.ok:
    print(endpoint.json())

# checks if the posted user is in the database
endpoint = requests.get("http://127.0.0.1:5000/users/15")
if not endpoint.ok:
    print(endpoint.json())
else:
    print("something is wrong")
