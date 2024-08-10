import requests
endpoint = requests.delete("http://127.0.0.1:5000/users/14")
print(endpoint.text)
