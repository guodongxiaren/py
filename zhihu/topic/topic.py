#!/usr/bin/env python
# coding=utf-8
"""
python 3
"""
from bs4 import BeautifulSoup
from urllib import request
from urllib import parse
import datetime
import json
import sys
import time


def get_main_topic():
    url = 'https://www.zhihu.com/topics'
    origin_bytes = request.urlopen(url).read()
    origin_string = origin_bytes.decode('utf-8')
    soup = BeautifulSoup(origin_string, 'html.parser')

    # <li class="zm-topic-cat-item" data-id="1761"><a href="#生活方式">生活方式</a></li>
    main_topic_li = soup.find_all('li', class_='zm-topic-cat-item')
    main_topic = {}
    for li in main_topic_li:
        topic_id = li.get('data-id')
        topic_name = li.text
        main_topic[int(topic_id)] = topic_name

    return main_topic

def get_sub_topic(main_topic_id, size=20):
    url = 'https://www.zhihu.com/node/TopicsPlazzaListV2'
    offset = 0
    topic_list = {}
    while True:
        offset += size
        data = {
            'method': 'next',
            'params': '{"topic_id":%d,"offset":%d,"hash_id":""}' % (main_topic_id, offset),
        }
        # requests.post(url, data=data) wrong, I don't know why
        params = parse.urlencode(data).encode('utf-8')
        req = request.Request(url, params)
        resp = request.urlopen(req)
        resp_text = resp.read()
        resp_json = json.loads(resp_text)
        html_list = resp_json.get("msg", "")

        for origin_string in html_list: 
            soup = BeautifulSoup(origin_string, 'html.parser')
            a_list = soup.find_all('a')
            for a in a_list:
                href = a.get('href')
                if href == 'javascript:;':
                    continue
                name = a.text.strip()
                topic_list[href] = name
        if len(html_list) < size:
            break;
    return topic_list

def get_all_topic_list():
    main_topic = get_main_topic()
    all_topic_list = []
    for main_topic_id, main_topic_name in main_topic.items():
        topic_list = get_sub_topic(main_topic_id)
        all_topic_list.extend(topic_list)
        time.sleep(1)
        print('%s done:has %d sub topic' % (main_topic_name, len(topic_list)))
    return all_topic_list

def get_topic_top_writer(topic_href):
    url = 'https://zhihu.com%s/top-writer' % (topic_href)
    print(url)
    origin_bytes = request.urlopen(url).read()
    origin_string = origin_bytes.decode('utf-8')
    soup = BeautifulSoup(origin_string, 'html.parser')
    print(origin_string)
    author_link_list = soup.find_all('a', class_='zg-link')
    author_list = []
    for author_link in author_link_list:
        print(author_link)
        href = author_link.get('href')
        href = 'https://www.zhihu.com/' + href
        name = author_link.text
        author_list.append({'name': name, 'href': href})
    return author_list


if __name__ == '__main__':
    #topic_list = get_sub_topic(1761) # for test
    #all_topic_list = get_all_topic_list()
    top = get_topic_top_writer('/topic/19584970')
    print(top)

