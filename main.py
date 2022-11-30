from bs4 import BeautifulSoup
import requests

url = "https://centralmosque.org.uk/"

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")

prayer_start = print(doc.find_all('div', {'class': 'prayer-start'}))

prayer_times_start = []
prayer_times_jamaat = []

for div in doc.find_all('div', {'class': 'prayer-start'}):
    prayer_times_start.append(div.text)
    
for div in doc.find_all('div', {'class': 'prayer-jamaat'}):
    prayer_times_jamaat.append(div.text)
    
print(prayer_times_start)
print(prayer_times_jamaat)

