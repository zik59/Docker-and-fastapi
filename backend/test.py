import requests

url = "http://127.0.0.1:8000"

data = {"count":10}

responsepost = requests.post(url, json=data)
print(responsepost.text)