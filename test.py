import requests

url = "http://127.0.0.1:8000"

response = requests.get(url=url)
print(response.text)

data = {"count":3}

responsepost = requests.post(url, json=data)
print(responsepost)