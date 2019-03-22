# coding: utf-8
from urllib import request
import json

class Spider(object):
    def get(self, url, param={}):
        if isinstance(param, dict) == True:
            kv_list = []
            for key,value in param.items():
                kv = '%s=%s' % (key, value)
                kv_list.append(kv)

            query_string = '&'.join(kv_list)
            url = url.rstrip('?') + '?' + query_string
        try:
            req_obj = request.Request(url=url)
            resp_obj = request.urlopen(req_obj)
            body = resp_obj.read().decode('utf-8')
            return body
        except Exception as e:
            print(Exception, e)
            return None

class BaiduIndex(Spider):
    def __init__(self):
        Spider.__init__(self)

    def get_keyword(self):
        url = 'https://index.baidu.com/Interface/homePage/wiseConfig'
        try:
            body = self.get(url)
            json_obj = json.loads(body, encoding='utf-8')
            kw_list = json_obj['data']['result']['keyword']
            return kw_list
        except Exception as e:
            print(Exception, e)
            return None

class BaiduRank(Spider):
    def __init__(self):
        Spider.__init__(self)

    def get_topword(self):
        url = 'http://top.baidu.com/mobile_v2/buzz?b=1&c=515'
        try:
            body = self.get(url)
            json_obj = json.loads(body, encoding='utf-8')
            topword_list = json_obj['result']['topwords']
            word_list = []
            for topword in topword_list:
                word_list.append(topword['keyword'])

            return word_list
        except Exception as e:
            print(Exception, e)
            return None
        
if __name__ == '__main__':
    index = BaiduIndex()
    kw_list = index.get_keyword()
    print(kw_list[:10])
    rank = BaiduRank()
    rank_list = rank.get_topword()
    print(rank_list)
