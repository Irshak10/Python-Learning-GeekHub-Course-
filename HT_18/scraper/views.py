from django.shortcuts import render
<<<<<<< HEAD
=======
from scraper.models import Product
>>>>>>> 1a6a5611d133c9ea51ed92d815af7073528d5d36

import requests
import re
from bs4 import BeautifulSoup
import time
<<<<<<< HEAD
import csv


def view(request):
    category = 80087
    data = []
    session = requests.Session()

    start = f'https://hard.rozetka.com.ua/videocards/c{category}'
    start_info = session.get(start)
    soup_start = BeautifulSoup(start_info.text, 'lxml')
    regularka = f'&q;id&q;:(\d+),&q;title'

    id_finale = []
    id_re = re.findall(regularka, start_info.text)
    id_set = set(id_re)

    for i in id_set:
        if len(i) > 6:
            id_finale.append(i)

    for finded_id in id_finale:
        final_url = f'https://search.rozetka.com.ua/search/api/v4/autocomplete?text={finded_id}'
        session.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
            'Remote Address': '78.27.198.50:443',
            'Referer': f'{final_url}'
        }
        final_info = session.get(final_url)
        soup_final = BeautifulSoup(final_info.text, 'lxml')

        category_1 = re.findall(r'parent\":\"(.+?)\"', final_info.text)[0]
        title = re.findall(r'title\":\"(.+?)\"', final_info.text)[0]
        price = re.findall(r'price\":(.+?)\",', final_info.text)[0]
        href = re.findall(r'href\":\"(.+?)\"', final_info.text)[0]
        image = re.findall(r'image\":\"(.+?)\"', final_info.text)[0]

        print(f'Category: {category_1}\nTitle: {title}\nPrice: {price}\nHref: {href}\nImage: {image}\n')
        print()
        time.sleep(0.1)
        product = {'category': category_1, 'title': title, 'price': price, 'href': href, 'image': image}
        data.append(product)

    print(data)
    template = 'scraper/home.html'
    return render(request, template, {'data': []})
=======


def view(request):
    template = 'scraper/home.html'
    category = request.POST.get('category', False)
    pages = request.POST.get('pages', False)
    # TODO: add scrapper
    data = []

    for page in range(1, int(pages)+1):

        start = f'https://www.olx.ua/{category}/?page={pages}'

        info_finale = requests.get(start)
        soup_finale = BeautifulSoup(info_finale.text, 'lxml')
        offer_wrappers = soup_finale.find_all('div', class_='offer-wrapper')

        for offer_wrapper in offer_wrappers:
            session = requests.Session()
            finded_href = offer_wrapper.find('div', class_='space rel').find('a').get('href')

            response = session.get(finded_href)
            print('Url:', finded_href)

            token_re = r"var phoneToken = '(.*?)';"
            id_re = r"'id':'(.*?)',"
            token_search = re.findall(token_re, response.text)
            site_id_search = re.findall(id_re, response.text)
            if len(site_id_search) == 0:
                print('site id is missed')
            elif len(token_search) == 0:
                print('-')
            else:
                site_id = re.findall(id_re, response.text)[0]
                token = re.findall(token_re, response.text)[0]
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
                print(f'{len(token) * "-"}\n')
                time.sleep(0.1)
                data = [finded_href, name, phone_num_finale]
                Product.objects.create(url=f'{finded_href}', discription='', name=f'{name}', phone_number=f'{phone_num_finale}')
                message = 'Scraper is done'
                print(message)
    return render(request, template, {'data': data})
>>>>>>> 1a6a5611d133c9ea51ed92d815af7073528d5d36
