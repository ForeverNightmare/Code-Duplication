
# -*- coding:utf-8 -*-

# @Author  : zhou_yaxiong_coder
# @Time    : 2021/3/7 20:03
# @File    : demo.py
# @Software: win10  python3.7.7


import requests
from lxml import etree
import fake_useragent
import os
import threading
import multiprocessing
import random
import time

basedir = os.path.dirname(os.path.abspath(__file__))
pic_path = os.path.join(basedir, 'storage')
if not os.path.exists(pic_path):
    os.mkdir(pic_path)

def github():
    resp = requests.get(url = "https://gist.github.com/anvaka/8e8fa57c7ee1350e3491#file-01-most-dependent-upon-md")

    html = etree.HTML(resp.text)
    body_html = html.xpath("//div[@id='file-01-most-dependent-upon-md-readme']")
    body_html = etree.tostring(body_html[0], encoding="utf-8").decode()
    # print(body_html)

    lis = etree.HTML(body_html).xpath(".//ol/li")
    keywords_list = []
    for li in lis:
        name = li.xpath(".//a/text()")[0]
        keywords_list.append(name)

    return keywords_list


def read_keywords():
    with open("name.txt", encoding="utf-8", mode="r") as fp:
        keywords_list = fp.read()
        return keywords_list

def second(keywords_list):
    # keywords_list = github()
    for key in keywords_list:
        package_list = []
        for i in range(6):
            url = f"https://www.npmjs.com/search?ranking=popularity&q={key}&page={i}&perPage=20"
            print(url)
            print("==========")
            time.sleep(1)
            resp = requests.get(url = url,
                                headers={
                                    # "cookie": "hubspotutk=7c0df75d2db9ea22894d08de075c43f3; __hs_opt_out=no; _ga=GA1.2.1536302193.1602569684; __hstc=72727564.7c0df75d2db9ea22894d08de075c43f3.1602569671304.1602569671304.1606785345424.2; __cfduid=d59f92819c52cb8b62e4d51e605c04ff31615118309",
                                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36"
                                },
                                #proxies={
                                    #"http": str(random.choice(get_socks5())),
                                    #"https": str(random.choice(get_socks5()))
                                #}
                                )
            body_html = etree.HTML(resp.text)
            h3 = body_html.xpath("//h3//text()")
            try:
                h3.remove("Support")
                h3.remove("Company")
                h3.remove("Terms & Policies")
            except:
                pass
            print(h3)
            for name in h3:
                package_list.append(name)
        with open(os.path.join(os.path.join(basedir, "storage"), "sum_result.txt"), encoding="utf-8", mode="a") as fp:
            for i in package_list:
                fp.write(i + "\n")
            #fp.writelines(f"{key}: {package_list} \n")

def get_socks5():
    socks5_list = ["socks5://10.20.1.211:1080", "socks5://10.20.1.211:1081", "socks5://10.20.1.211:1082",
                  "socks5://10.20.1.211:1083", "socks5://10.20.1.211:1084", "socks5://10.20.1.211:1085",
                  "socks5://10.20.1.211:1086"]
    return socks5_list

def thea():
    '''keywords_list = github()
    print(keywords_list)
    for i in range(9):
        keyword = list(keywords_list)[i*100: i*100+100]
        print(keyword)
        # threading.Thread(target=second, args=(keywords_list,)).start()
        multiprocessing.Process(target=second, args=(keyword,)).start()
        print(f"===================={i}=================")'''
    keyword = ["keywords:front-end", "keywords:backend", "keywords:cli", "keywords:documentation",
                "keywords:css", "keywords:testing", "keywords:iot", "keywords:coverage",
                "keywords:mobile", "keywords:framework", "keywords:robotics", "keywords:math"]

    multiprocessing.Process(target=second, args=(keyword,)).start()
if __name__ == '__main__':
    thea()