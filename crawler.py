# -*-coding:utf-8-*-

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



def df_to_csv():
    df = get_tabel(DOMEIN)
    df.to_csv('data/data.csv')


#----------------------------------------

df = get_tabel(DOMEIN)
data = pd.read_csv('/Users/t4t3/Dropbox/tools/twomotor/data/data.csv', index_col= 0  )


print(df)
print("#"*100)
print(data)