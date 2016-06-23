# -*- coding:utf-8 -*-

import requests
import re
import os



def get_page_html(url):
    response = requests.get(url)
    response.encoding = 'utf-8'
    return response.text

def get_imgurl(html):
    pattern = re.compile(r'"objURL":"(http://.+)"')
    return pattern.findall(html)

def save_image(img_url_list):
    img_dir = 'D:\\images'
    if not os.path.exists(img_dir):
        os.mkdir(img_dir)
    i = 1
    for u in img_url_list:
        print('正在下载第%s张 %s' % (i, u))
        resp = requests.get(u)
        file_name = os.path.split(u)[1]
        file = os.path.join(img_dir, file_name)
        i = i + 1
        with open(file, 'wb') as f:
            f.write(resp.content)
            f.close()
        

if __name__ == '__main__':
    print('开始下载...')
    url = 'http://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fr=&sf=1&fmq=1461833981476_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E5%A3%81%E7%BA%B8'
    html_text = get_page_html(url)
    imgs = get_imgurl(html_text)
    save_image(imgs)
    print('下载完成！')

#soup = BeautifulSoup(response.text, 'html.parser')

#print(soup)
#for x in soup.select('img'):
#    print(x.src)

