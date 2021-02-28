from django.shortcuts import render
from scraper.models import Product

import requests
import re
from bs4 import BeautifulSoup
import time


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
