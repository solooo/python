# -*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup
import re



def get_page_html(url):
    response = requests.get(url)
    response.encoding = 'utf-8'
    return response.text

def get_imgurl(html):
    pattern = re.compile(r'.+"middleURL":"(http://.+)".+')
    return pattern.match(html)

if __name__ == '__main__':
    url = 'http://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fr=&sf=1&fmq=1461833981476_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E5%A3%81%E7%BA%B8'
    html_text = get_page_html(url)
    imgs = get_imgurl(html_text)
    print(html_text)
    print(imgs.goups())

#soup = BeautifulSoup(response.text, 'html.parser')

#print(soup)
#for x in soup.select('img'):
#    print(x.src)

