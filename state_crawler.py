import requests
import sys
from bs4 import BeautifulSoup

URL = 'https://en.wikipedia.org/wiki/List_of_state_universities_in_the_United_States'

r = requests.get(URL, 'html.parser')
soup = BeautifulSoup(r.content, 'html.parser')

headerTwos = soup.find_all('h2')
mapping = {}

for h2 in headerTwos[1:-2]:
	state = h2.next_element.string
	mapping[state] = []
	schools = set()

	ul = h2.find_next_sibling('ul')
	li_s = ul.find_all('li')
	for li in li_s:
		if li.find('ul'):
			continue
		link = li.find('a')
		if link:
			schools.add(link.text)

	mapping[state] = list(schools)

sum = 0
for key in mapping:
	sum += len(mapping[key])


