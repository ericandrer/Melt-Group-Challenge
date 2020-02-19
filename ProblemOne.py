from bs4 import BeautifulSoup
import requests

response = requests.get('https://www.meltgroup.com/en/')

soup = BeautifulSoup(response.text, 'html.parser')

for links in soup.find_all('a', href=True):
    print(links['href'])
