#!/usr/bin/env python
# coding=utf-8
import urllib.request as request
import datetime
from bs4 import BeautifulSoup

import requests

url = 'https://www.zhihu.com/people/guodongxiaren/'
header = {
    'Host': 'www.zhihu.com',
    'Accept-Encoding': 'gzip, deflate',
    'Accept': '*/*',
    'User-Agent': 'PostmanRuntime/7.17.1',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Cookie': '_zap=d8d61208-2d92-461e-ae7d-645f374aa419; _xsrf=eca9c5e4-62e6-45c6-86c9-faf922add43f; d_c0="APDiR5XfGA-PTqhxkZ9Ehxd97v7AzxPp10g=|1552147261"; KLBRSID=4843ceb2c0de43091e0ff7c22eadca8c|1590766567|1590765750'
}
cookie = {
    'xx':'xx'

}

s = requests.session()
s.cookies.update(cookie)
s.headers.update(header)

resp = s.get(url)
#print(type(res3.request.headers.get("Cookie").split("IRSSID=")[-1]))
print(resp.request._cookies)
origin_string = resp.text
print(origin_string)
soup = BeautifulSoup(origin_string, 'html.parser')

meta_list = soup.find_all('meta')
voteupCount, followerCount = 0,0
for meta in meta_list:
    if meta.get('itemprop') == 'zhihu:voteupCount':
        voteupCount = meta.get('content')
    elif meta.get('itemprop') == 'zhihu:followerCount':
        if meta.has_attr('content'):
            followerCount = meta.get('content')

date = datetime.datetime.now().strftime('%Y-%m-%d')
print('%s,%s,%s' % (date, voteupCount, followerCount))
