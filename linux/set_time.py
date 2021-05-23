#!/usr/bin/env python
# coding=utf-8
import json
import urllib.request as request

# {"sysTime2":"2021-05-23 23:27:25","sysTime1":"20210523232725"}
def set_time():
    url = 'http://quan.suning.com/getSysTime.do'
    origin_bytes = request.urlopen(url).read()
    origin_string = origin_bytes.decode('utf-8')
    obj = json.loads(origin_string)
    now_time = obj['sysTime2'];
    cmd = 'date -s "%s"' % (now_time)
    print(cmd)

if __name__ == '__main__':
    set_time()

