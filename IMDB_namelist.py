import requests
from bs4 import BeautifulSoup

URL = 'http://www.imdb.com/list/ls062249377/'

class Imdb:

	def __init__(self, soup):
		self.soup = soup
		self.nameList = []
		self._getInfo(self.soup)

	def getNameList(self):
		return self.nameList

	def _getInfo(self,soup):
		list = soup.find_all('div', class_= ['lister-item', 'mode-detail'])
		for child in list:
			h3 = child.find('h3')
			self.nameList.append(h3.a.text)


def main():
	r = requests.get(URL, 'html.parser')
	soup = BeautifulSoup(r.content, 'html.parser')
	imdb = Imdb(soup)
	print(imdb.getNameList())



if __name__ == '__main__':
	main()