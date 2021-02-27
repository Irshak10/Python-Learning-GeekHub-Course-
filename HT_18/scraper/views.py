from django.shortcuts import render

import requests
import re
from bs4 import BeautifulSoup
import time
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