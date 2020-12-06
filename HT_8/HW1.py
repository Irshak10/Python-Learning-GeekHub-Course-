import requests
from bs4 import BeautifulSoup
import time

for i in range(1, 11):
	print(f'Information from page №{i}\n')

	url = f'http://quotes.toscrape.com/page/{i}'

	info = requests.get(url)
	info.text

	if info.status_code == 200:
		soup = BeautifulSoup(info.text, 'lxml')
		quotes = soup.select('div[class="quote"]')

		for quote in quotes:

			text = ''
			finded_text = quote. select_one('span[class = "text"]')
			if finded_text:
				text = finded_text.text.strip().replace('“', '').replace('”', '')

			author = ''
			finded_author = quote.select_one('small[class = "author"]')
			if finded_author:
				author = finded_author.text

			href = ''
			finded_href = quote.select_one('a')
			if finded_href:
				href = finded_href.get('href', '')
			if href:
				href = url.replace(f'/page/{i}', '') + href

			author_info = requests.get(href)
			author_soup = BeautifulSoup(author_info.text, 'lxml')

			author_birthday = ''
			finded_author_birthday = author_soup.select_one('span[class = "author-born-date"]')
			if finded_author_birthday:
				author_birthday = finded_author_birthday.text

			author_location = ''
			finded_author_location = author_soup.select_one('span[class = "author-born-location"]')
			if finded_author_location:
				author_location = finded_author_location.text


			print(f'Text: {text}\nAuthor: {author}\nHref about: {href}\nAuthor birthday: {author_birthday}\nAuthor Birthday Location: {author_location}')
			print()
			time.sleep(1)

if __name__ == '__main__':
	pass