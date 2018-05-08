# -*- coding: utf-8 -*-
import requests



if __name__ == '__main__':
    r = requests.get('https://www.douban.com/')  # 豆瓣首页
    print r.status_code
