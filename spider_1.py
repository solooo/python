# -*- coding: utf-8 -*-

import urllib.request

try:
    url = 'http://www.baidu.com'
    user_agent = 'Mozilla/4.0(compatible; MSIE 5.5; Windows NT)'
    headers = {'User-agent' : user_agent}
    req = urllib.request.Request(url,headers=headers)
    response = urllib.request.urlopen(req)
    page = response.read()
    print(page.decode('UTF-8'))
except urllib.URLError as e:
    print (e)
