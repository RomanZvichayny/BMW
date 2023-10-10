from bs4 import BeautifulSoup
import requests
import json

url = 'https://www.bmw.ua/uk/configurator.html'



headers = {
	'Accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
}

req = requests.get(url, headers=headers)
src = req.text
# print(src)
#
# with open('BMW.html', 'w', encoding='utf-8') as file:
# 	file.write(src)

def config():
	with open('BMW.html', encoding='utf-8') as file:
		file.read(src)

soup = BeautifulSoup(src, 'lxml')

links_bmw = []

hrefs = soup.find(id='container-a341afc382').find_all('a')
for h in hrefs:
	h_text = h.text
	h_url = h.get('href')
	link = {'Name': h_text, 'Url': h_url}
	links_bmw.append(link)
	print(f'{h_text}: {h_url}')

with open('C:/Users/TVOYO/Desktop/Python//tasks/Euler_project/data/links_bmw.json', 'w', encoding='utf-8', newline='') as file:
	json.dump(links_bmw, file, indent=4, ensure_ascii=False)
