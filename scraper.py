import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}
html = requests.get("https://oddball.io/jobs/", headers=headers)
doc = BeautifulSoup(html.text, 'html.parser')

print(doc)





