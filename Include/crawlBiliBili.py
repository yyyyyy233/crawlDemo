

import requests
from bs4 import BeautifulSoup
import re
import math
import biliBV
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
bvlist = []
for i  in range(1,4):
    htmlBili = requests.get(
        "https://search.bilibili.com/all?keyword=%E7%94%98%E8%82%83%E9%A9%AC%E6%8B%89%E6%9D%BE&from_source=webtop_search&spm_id_from=333.851&page="+str(i),
        headers=headers).text
    soup = BeautifulSoup(htmlBili, 'lxml')

    bvlisthtml = soup.select('#all-list > div.flow-loader > div.mixin-list > ul ')
    for bl in bvlisthtml:
        allinfo = bl.get_text
        print(str(allinfo))
        print(type(allinfo))
        lj = re.findall('href=\"//www.bilibili.com/video/(BV[0-9A-Za-z]+)\?from=search\"', str(allinfo))
        # print(lj)
    bvlist =bvlist+ list(set(lj))

print(bvlist)
print(len(bvlist))


i=1
for bv in bvlist:

    oid = biliBV.decode(bv)
    apiurl = 'http://api.bilibili.com/x/v2/reply?oid='+str(oid)+'&type=1'
    json = requests.get(apiurl,headers = headers).text
    file = open(str(i)+'bilibili.txt','w',encoding='utf-8')
    file.write(str(oid)+"\n")
    file.write(json)
    file.close()
    i= i+1
