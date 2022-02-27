#!/usr/bin/env python
# coding=utf-8
import datetime
import requests
header = {
        'Host': 'api.bilibili.com',
        'Accept-Encoding': 'gzip, deflate',
        'Accept': '*/*',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Mobile Safari/537.36',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
}
url = 'https://api.bilibili.com/x/relation/stat?vmid=46421125'
resp = requests.get(url, headers=header)
json_data = resp.json()
data = json_data['data']
follower_cnt = data['follower']

date = datetime.datetime.now().strftime('%Y-%m-%d')
line = '%s,%s' % (date, follower_cnt)
print(line)
