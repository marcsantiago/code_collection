from bs4 import BeautifulSoup
import urllib

url = urllib.urlopen('http://en.wikipedia.org/wiki/Candy').read()
soup = BeautifulSoup(url)

for link in soup.find_all('a'):
	print link.get('href')
	
urllib.urlretrieve('http://upload.wikimedia.org/wikipedia/commons/thumb/1/10/Candy_in_Damascus.jpg/250px-Candy_in_Damascus.jpg', 'candy.jpg')