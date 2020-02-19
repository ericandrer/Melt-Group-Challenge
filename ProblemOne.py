from bs4 import BeautifulSoup
import requests

url = 'https://www.meltgroup.com/en/'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

counter = 0

for links in soup.find_all('a', href=True):
    print(links['href'])
    counter = counter + 1

print("En la pagina " + url + "hay un total de " + str(counter) + " links encontrados.")
