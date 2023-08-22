import requests

url = "http://127.0.0.1:5555/webhook"
r = requests.post(url)

print(r.content)