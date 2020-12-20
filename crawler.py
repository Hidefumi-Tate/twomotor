# --coding:utf-8--

import requests
from bs4 import BeautifulSoup as bs
import pandas as pd


DOMEIN = 'https://www.jma.go.jp/jp/amedas_h/today-23232.html'


def get_soup(url):
    r = requests.get(url)
    html = r.text
    return bs(html, "lxml")


def get_today(soup):
    found = soup.find('td',class_='td_title height2')
    return found.text.split("　")[0]

def get_tabel(url):
    dflist = pd.read_html(url)
    return dflist[4]



def main():
    soup = get_soup(DOMEIN)    
    today = get_today(soup)
    df = get_tabel(DOMEIN)
    return df


for i in main():
    print(i)