#!/usr/bin/env python
# coding=utf-8
import time
import threading
import multiprocessing
import requests
import sys
import wget
from urllib import parse
from queue import Queue

class M3U8(object):

    def __init__(self):
        self.ts_list = []
        self.ts_dict = {}
        self.q = Queue() 


    def get_ts_list(self, url):
        """
        url: m3u8资源url
        """
        response = requests.get(url)
        resp = response.text
        ts_list = []
        pr = parse.urlparse(url)
        base = '%s://%s' % (pr.scheme, pr.netloc)
        print(base)
        for line in resp.split('\n'):
            line = line.strip()
            if len(line) == 0 or line[0] == '#':
                continue
            ts_url = base + line
            ts_list.append(ts_url)
        self.ts_list = ts_list[:]
        return ts_list

    def build_ts_index(self, ts_list=None):
        if ts_list == None:
            ts_list = self.ts_list

        for i, value in enumerate(ts_list):
            self.ts_dict[value] = i

        print(self.ts_dict)

    def download(self, ts_url, dest_dir):
        index = self.ts_dict[ts_url]
        output = '%s/%s.mp4' % (dest_dir, index)
        print(ts_url, output)
        wget.download(ts_url, out=output)

    def download_all(self, dest_dir):
        for ts_url in self.ts_list:
            self.download(ts_url, dest_dir)

    def download_from_queue(self, dest_dir):
        while self.q.empty() == False:
            ts_url = self.q.get()
            self.download(ts_url, dest_dir)

    def download_parallel(self, dest_dir):
        for ts_url in self.ts_list:
            self.q.put(ts_url)

        t_num = 5
        p_list = []
        for j in range(t_num):
            p = multiprocessing.Process(target=self.download_from_queue, args=(dest_dir))
            p.start()
            p_list.append(p)
        
        map(lambda p:p.join(), p_list)


def main(*args):
    print(args)
    url = args[0]
    m = M3U8()
    m.get_ts_list(url)
    m.build_ts_index()
    start = time.time()
    m.download_parallel('tmp')
    end = time.time()
    print('end - start', end - start)

if __name__ == '__main__':
    main(*sys.argv[1:])
