#!/usr/bin/env python
# coding=utf-8
import requests
from  decimal import Decimal

class StockApi(object):
    def __init__(self):
        pass
    def query_sum(self, code):
        pass

    def request(self, code, market):
        market, code = market.lower(), code.lower()
        if market == 'us':
            code = 'usr_%s' % (code)
        elif market in ('hk', 'sh', 'sz'):
            code = '%s%s' % (market, code)

        url = 'http://hq.sinajs.cn/list=%s' % (code)
        response = requests.get(url)
        res = response.text
        res_list = res.strip().split('=')
        data_list = res_list[1].split(',')

        if market == 'hk':
            price = data_list[4]
        elif market == 'us':
            price = data_list[1]
        elif market in ('sh', 'sz'):
            price = data_list[3]
        return price

    def query(self, code, market, equity):
        price = self.request(code, market)
        value = Decimal(price) * Decimal(equity) / 10000
        return value


def load_stock(filename):
    stock_dict = {}
    with open(filename, 'r') as f:
        for line in f.readlines():
            data = line.strip().split('\t')
            stock_dict[data[0]] = data[1:]

    return stock_dict


def main():
    stock_dict = load_stock('stock.txt')
    api = StockApi()
    value_dict = {}
    value_list = []
    for name, data in stock_dict.items():
        market, code, equity = data[0:3]
        # equity 单位：万股
        value = api.query(code, market, equity)
        if market in ('sh', 'sz'):
            # TODO 缺人民币兑换美元的汇率查询API
            continue
        # 港币盯紧美元
        if market == 'hk':
            value = value * Decimal(0.128)
        value = value.quantize(Decimal('0.00'))
        value = float(value)
        value_dict[value] = name
        value_list.append(value)

    value_list.sort(reverse=True)
    for value in value_list:
        name = value_dict[value]
        # 单位美元
        print("%s\t%s 亿" % (name, value))


if __name__ == '__main__':
    main()
