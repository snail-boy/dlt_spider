import re
import ast
from urllib import parse
from datetime import datetime

import time
from apscheduler.schedulers.blocking import BlockingScheduler

import requests
from scrapy import Selector

from models import *

def parse_list(url):
    print(url, 'url')
    res_text = requests.get(url)
    res_text.encoding = 'gb2312'
    res_text = res_text.text
    sel = Selector(text=res_text)

    all_list = sel.xpath(".//tbody[@id='tdata']/tr[@class='t_tr1']")
   

    # index = len(all_list.extract())

    for item in all_list:
        periods = Periods()
        no = item.xpath("string(.//td[@class='t_tr1'][1])").extract()[0]
        one = item.xpath("string(.//td[@class='cfont2'][1])").extract()[0]
        two = item.xpath("string(.//td[@class='cfont2'][2])").extract()[0]
        three = item.xpath("string(.//td[@class='cfont2'][3])").extract()[0]
        four = item.xpath("string(.//td[@class='cfont2'][4])").extract()[0]
        five = item.xpath("string(.//td[@class='cfont2'][5])").extract()[0]

        six = item.xpath("string(.//td[@class='cfont4'][1])").extract()[0]
        seven = item.xpath("string(.//td[@class='cfont4'][2])").extract()[0]


        # periods.id = index
        periods.no = no
        periods.one = one
        periods.two = two
        periods.three = three
        periods.four = four
        periods.five = five
        periods.six = six
        periods.seven = seven

        print(no, one, two, three, four, five, six, seven, 'seven')

        # existed_periods = Periods.select().where(Periods.no != no)
        # if existed_periods:
        #     periods.save(force_insert=True)
        # else:
        #     return
            # periods.save(force_insert=True)

        # index = index - 1

def job():
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    last_urls = 'http://datachart.500.com/dlt/history/newinc/history.php?limit=1&sort=0'
    parse_list(last_urls)
    
if __name__ == "__main__":
    # last_urls = 'http://datachart.500.com/dlt/history/newinc/history.php?limit=1&sort=0'
    # last_urls = 'http://172.16.20.30:8080'
    # parse_list(last_urls)
    # print(last_urls, 'last_urls')

     # 该示例代码生成了一个BlockingScheduler调度器，使用了默认的任务存储MemoryJobStore，以及默认的执行器ThreadPoolExecutor，并且最大线程数为10。
    
    # BlockingScheduler：在进程中运行单个任务，调度器是唯一运行的东西
    scheduler = BlockingScheduler()
    # 采用阻塞的方式

    # 采用固定时间间隔（interval）的方式，每隔5秒钟执行一次
    # scheduler.add_job(job, 'interval', seconds=5)

    scheduler .add_job(job, 'cron', day_of_week='1, 3, 5', hour='23')
    
    scheduler.start()



