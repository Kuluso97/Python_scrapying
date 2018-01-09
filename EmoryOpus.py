import requests
from bs4 import BeautifulSoup

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'
}

URL = 'https://saprod9.emory.edu/psp/saprod9/?cmd=login'

PAYLOAD = {'userid': "****", "pwd":"****"}

with requests.Session() as session:
	r = session.get(URL, headers=headers)
	r = session.post(URL, data=PAYLOAD, headers=headers)

	print(r.content)
	soup = BeautifulSoup(r.content, 'lxml')
