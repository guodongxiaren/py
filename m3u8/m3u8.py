#!/usr/bin/env python
# coding=utf-8
import time
import threading
import multiprocessing
import os
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
        self.failed_list = []
        self.base_url = ''

    def extract_key(self, line):
        """
        提出出key的路径
        """
        for data in line.split(','):
            data = data.replace('"', '')
            index = data.find("URI=")
            if index == -1:
                continue
            key_path = data[index+5:]
            return key_path
        return None

    def get_ts_list(self, url):
        """
        url: m3u8资源url
        """
        filename = url.split('/')[-1]
        tmp_dir = url.split('/')[-2]
        filename = 'tmp/'+tmp_dir +'/' + filename
        response = requests.get(url)
        resp = response.text
        f = open(filename, 'w')
        f.write(resp)
        ts_list = []
        pr = parse.urlparse(url)
        base = '%s://%s' % (pr.scheme, pr.netloc)
        self.base_url = base
        for line in open(filename, 'r'):
            line = line.strip()
            if (line.startswith('#EXT-X-KEY')):
                key_path = self.extract_key(line)
            if len(line) == 0 or line[0] == '#':
                continue
            ts_url = base + line
            ts_list.append(ts_url)
        self.ts_list = ts_list[:]
        return ts_list

    def build_ts_index(self, ts_list=None):
        if ts_list is None:
            ts_list = self.ts_list

        max_char_len = len(str(len(ts_list)))

        for i, value in enumerate(ts_list):
            index = str(i)
            index = index.zfill(max_char_len)
            self.ts_dict[value] = index

    def download(self, ts_url, dest_dir):
        index = self.ts_dict[ts_url]
        output = '%s/%s.ts' % (dest_dir, index)
        print(ts_url, output, '\n')
        #wget.download(ts_url, out=output)
        with open(output, 'wb') as f:
            response = requests.get(ts_url, timeout=30)
            f.write(response.content)

    def download_all(self, dest_dir):
        for ts_url in self.ts_list:
            self.download(ts_url, dest_dir)

    def download_from_queue(self, dest_dir):
        while self.q.empty() == False:
            ts_url = self.q.get()
            self.download(ts_url, dest_dir)

    def download_from_list(self, ts_list, dest_dir):
        for ts_url in ts_list:
            try:
                self.download(ts_url, dest_dir)
            except Exception as e:
                self.failed_list.append(ts_url)

    def download_parallel(self, dest_dir):
        list_file = open(f'{dest_dir}/list.txt', 'w')
        for ts_url in self.ts_list:
            index = self.ts_dict[ts_url]
            self.q.put(ts_url)
            list_file.write(f'file {index}.ts\n')
        list_file.close()

        num = 10
        p_list = []
        ts_size = len(self.ts_list)
        size = int(ts_size / num)
        for j in range(num):
            begin, end = j * size, (j + 1) * size
            if j + 1 == num:
                end = None

            print(begin, end, size)
            sub_ts_list = self.ts_list[begin:end]
            p = multiprocessing.Process(
                target=self.download_from_list, args=(
                    sub_ts_list, dest_dir))
            p.start()
            p_list.append(p)

        #map(lambda p:p.join(), p_list)
        for p in p_list:
            p.join()

    def retry_failed_ts(self, dest_dir):
        if len(self.failed_list) == 0:
            return
        print('retry failed:')
        print(m.failed_list)
        self.download_from_list(self.failed_list, dest_dir)


def main(*args):
    url = args[0]
    tmp_dir = url.split('/')[-2]
    print(url, tmp_dir)
    tmp_path = f'tmp/{tmp_dir}'
    if not os.path.exists(tmp_path):
        os.makedirs(tmp_path)
    m = M3U8()
    m.get_ts_list(url)
    m.build_ts_index()
    start = time.time()
    m.download_parallel(tmp_path)
    m.retry_failed_ts(tmp_path)
    end = time.time()
    print('end - start', end - start)


if __name__ == '__main__':
    main(*sys.argv[1:])
