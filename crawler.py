# -*-coding:utf-8-*-

import requests
from bs4 import BeautifulSoup as bs
import pandas as pd


URL = 'https://weather.yahoo.co.jp/weather/amedas/1d/23232.html?m=temp'

def get_soup(url):
    r = requests.get(url)
    html = r.text
    return bs(html, "lxml")


def get_today(soup):
    found = soup.find('td',class_='td_title height2')
    return found.text.split("　")[0]

def get_tabel(url):
    dflist = pd.read_html(url)
    return dflist



def df_to_csv(url):
    df = get_tabel(url)
    df = pd.DataFrame(df)
    df.to_csv('data/data.csv')


#--------debug--------------------------------

df = get_tabel(URL)
# data = pd.read_csv('/Users/t4t3/Dropbox/tools/twomotor/data/data.csv', index_col= 0  )

print(df)
print("#"*100)