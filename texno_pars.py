import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os


def pars_texno(category):
    load_dotenv()
    list_texno = []
    URL = os.getenv('URL')
    HOST = os.getenv('HOST')
    HEADERS = {
        'USER-AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
    }

    html = requests.get(URL + category, headers=HEADERS).text
    soup = BeautifulSoup(html, 'html.parser')

    blocks = soup.find_all('div', class_='col-3')

    for block in blocks:
        images = block.find('img', class_='product-image').get('src')
        credit_price = block.find('div', class_='installment-price mb-6').get_text()
        price = block.find('div', class_='product-price__current').get_text()
        content = HOST + block.find('a').get('href')

        list_texno.append({
            'images': images,
            'credit_price': credit_price,
            'price': price,
            'content': content
        })
    return list_texno


pars_texno('katalog/smartfony-apple/')
