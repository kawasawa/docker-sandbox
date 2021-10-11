import requests
from bs4 import BeautifulSoup

data = requests.get('https://google.com/')
html = BeautifulSoup(data.content, 'html.parser')

for element in html.find_all('a'):
  print(element.text)
