from bs4 import BeautifulSoup
import requests

var = input("Please enter something: ")

print("You entered: " + var)

response = requests.get('https://www.meltgroup.com/en/')

soup = BeautifulSoup(response.text, 'html.parser')

for i in range(int(var)):
    print(str(i) * i)
    for links in soup.find_all('a', href=True):
        print(links['href'])
        for j in range(int(var)):
            print(str(j) * j)
            print(links['href'])
