# Заходите на ось цей сайт https://www.expireddomains.net/register-deleted-domains/ (з ним будьте обережні) вибираєте будь-яку на ваш вибір доменну зону і парсите список  доменів - їх там буде десятки тисяч (звичайно ураховуючи пагінацію)
# Всі отримані значення зберігти в CSV файл.

#Моя відповідь: 
import requests
from bs4 import BeautifulSoup
import time
import csv

for number_page in range (0,301,25):
    if number_page != 0:
        s = f'start={number_page}'
    else:
        s = ''
    session = requests.Session()
    start = f'https://www.expireddomains.net/deleted-domains/?{s}&ftlds[]=242#listing'
    session.headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
        'Remote Address': '116.202.172.96:443',
        'Referrer Policy': 'same-origin',
        'referer': f'{start}'
    }

    start_info = session.get(start)
    soup_start = BeautifulSoup(start_info.text, 'lxml')
    tr = soup_start.find('table',class_="base1")

    for i in tr.find_all('tbody'):
        rows = i.find_all('tr')
        for row in rows:
            domain = row.select_one('td[class="field_domain"] a').text
            bl = row.select_one('td[class="field_bl"] a').text
            domainpop = row.select_one('td[class="field_domainpop"] a').text
            abirth = row.select_one('td[class="field_abirth"]').text
            aentries = row.select_one('td[class="field_aentries"] a').text
            alexa = row.select_one('td[class="field_alexa"] a').text
            dmoz = row.select_one('td[class="field_dmoz"] a')
            if dmoz == None:
                dmoz = "-"
            statuscom = row.select_one('td[class="field_statuscom"] a').text
            statusnet = row.select_one('td[class="field_statusnet"] a').text
            statusorg = row.select_one('td[class="field_statusorg"] a').text
            statusde = row.select_one('td[class="field_statusde"] a').text
            statustld_registered = row.select_one('td[class="field_statustld_registered"] a').text
            related_cnobi = row.select_one('td[class="field_related_cnobi"]').text
            changes = row.select_one('td[class="field_changes"]').text
            whois = row.select_one('td[class="field_whois"] a').text

            print(f'Domain: {domain}| BL: {bl}| DP: {domainpop}| ABY: {abirth}| ARC: {aentries}| Alexa: {alexa}| Dmoz: {dmoz}|'
                f' C: .com {statuscom}| N: .net {statusnet}| O: .org {statusorg}| D: .de {statusde}| Reg: {statustld_registered}|'
                f' RDT: {related_cnobi}| Dropped: {changes}| Status: {whois}')
            print()
            with open(f'data_from_deleted.csv', 'a', encoding='utf8', newline='') as f:
                writer = csv.writer(f)
                writer.writerow([f'Domain: {domain}| BL: {bl}| DP: {domainpop}| ABY: {abirth}| ARC: {aentries}| Alexa: {alexa}| Dmoz: {dmoz}|'
                f' C: .com {statuscom}| N: .net {statusnet}| O: .org {statusorg}| D: .de {statusde}| Reg: {statustld_registered}|'
                f' RDT: {related_cnobi}| Dropped: {changes}| Status: {whois}\n\n', f])
            time.sleep(1)