#!/usr/bin/env python
# coding=utf-8
import datetime
import urllib
from bs4 import BeautifulSoup

url = 'https://www.zhihu.com/people/guodongxiaren/'
origin_bytes = urllib.urlopen(url).read()
origin_string = origin_bytes.decode('utf-8')
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
