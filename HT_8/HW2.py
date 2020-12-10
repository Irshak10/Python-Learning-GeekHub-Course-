import requests
import re
from bs4 import BeautifulSoup
import time
import csv


start = 'https://www.olx.ua/sitemap.xml'
start_info = requests.get(start)
soup_start = BeautifulSoup(start_info.text, 'lxml')
url_region = soup_start.find('loc').text.strip()

region_info = requests.get(url_region)
soup_goods = BeautifulSoup(region_info.text, 'lxml')
url_goods = soup_goods.find_all('loc')[2].text.strip()

info_finale = requests.get(url_goods)
soup_finale = BeautifulSoup(info_finale.text, 'lxml')
offer_wrappers = soup_finale.find_all('div', class_='offer-wrapper')


for offer_wrapper in offer_wrappers:
    session = requests.Session()
    finded_href = offer_wrapper.find('div', class_='space rel').find('a').get('href')

    response = session.get(finded_href)
    print('Status code:', response.status_code)

    token_re = r"var phoneToken = '(.*?)';"
    id_re = r"'id':'(.*?)',"

    token = re.findall(token_re, response.text)[0]
    site_id = re.findall(id_re, response.text)[0]
    print(f'Token: {token},\nSite_id: {site_id}')

    session.headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
        'referer': f'{finded_href}'
    }
    phone_num = f'https://www.olx.ua/ajax/misc/contact/phone/{site_id}/?pt={token}'

    pn_response = session.get(phone_num)
    phone_num_finale = pn_response.json()['value']

    soup_name = BeautifulSoup(response.text, 'lxml')
    name = soup_name.select_one('div[class*="offer-user__action"] a').text.strip()
    print(f'Name: {name}\nPhone number: {phone_num_finale}')
    print(f'{len(token)*"-"}\n')
    with open(f'data.csv', 'a', encoding='utf8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([f'Name: {name}\nPhone number: {phone_num_finale}\n\n', f])
    time.sleep(1)


if __name__ == '__main__':
	pass