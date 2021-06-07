import requests
import re
from splinter import Browser
import time
import json
from bs4 import BeautifulSoup
import random
cookies='SINAGLOBAL=9401920004582.547.1594894306275; ALF=1653718349; SCF=AkNvIaGNl_WI14tIVwFcl-44I7tVWno2ASdRizT1K1Gh3ORd153zefs5Ni1tGHJEtCb7CvirWQW7yjRdy2MLk50.; SUB=_2A25Nt2Z0DeRhGeFM7VsZ8CjEyD2IHXVvWAo8rDV8PUJbkNAKLUOskW1NQKkVToxf-ANEJWEUwvcpZb9wic4VymSV; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9Wh.BsN_3sVZyfJ583nyNUlc5NHD95QNeoq41h5c1hepWs4DqcjPi--ci-zfiKnfi--4iKLsi-z0Sh-Ee0qt; wvr=6; _s_tentry=weibo.com; Apache=6766741162143.81.1622422459731; ULV=1622422459852:33:6:2:6766741162143.81.1622422459731:1622346239091; UOR=,,link.zhihu.com; webim_unReadCount=%7B%22time%22%3A1622438545446%2C%22dm_pub_total%22%3A2%2C%22chat_group_client%22%3A0%2C%22chat_group_notice%22%3A0%2C%22allcountNum%22%3A39%2C%22msgbox%22%3A0%7D'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36','cookie':cookies}

html = requests.get('https://s.weibo.com/weibo/%23%E7%94%98%E8%82%83%E5%B1%B1%E5%9C%B0%E9%A9%AC%E6%8B%89%E6%9D%BE%E4%BA%8B%E6%95%8521%E4%BA%BA%E9%81%87%E9%9A%BE%23?topnav=1&wvr=6&b=1',headers=headers).text
#print(html)
htmlTextl = re.findall('(//weibo\.com/[0-9]+/([0-9A-Za-z]+))',html)
print(htmlTextl)

i = 0
#commentNumlist = []
zhengwenlist=[]


for htmltmp in htmlTextl:
    # html = requests.get("https:"+htmltmp,headers=headers).text
    # print(html)
    browser = Browser(driver_name='chrome')

    browser.visit("https:"+htmltmp[0]+"?type=comment")
    time.sleep(10)
    htmlstr = browser.html
    browser.quit()
    soup = BeautifulSoup(htmlstr, 'lxml')

    #htmlzwl = soup.find_all("div",class_="WB_detail")
    htmlzwl = soup.find_all("div",class_='WB_text W_f14')
    zhengwenlist.append(htmlzwl)
    # commenttmpnum = soup.select('#Pl_Official_WeiboDetail__58 > div > div > div > div.WB_feed_handle > div > ul > li.curr > a > span > span > span > em:nth-child(2)')
    # for commentnum in commenttmpnum:
    #     #print(commentnum.get_text())
    #     commentNumlist.append(commentnum.get_text())
commentNumPointer=0

for comment in htmlTextl:
    commentlist = []
    #numOfpage = int(commentNumlist[commentNumPointer])/9+1
    for i in range(1,1300):#实际数据为1300
        url = 'https://m.weibo.cn/api/comments/show?id='+comment[1]+'&page='+str(i)
        print(url)
        jsonstr = requests.get(url=url,headers=headers).text
        time.sleep(random.random()*5+1)
        commentdic = json.loads(jsonstr)
        print(commentdic)
        if(commentdic['ok'] == 1):
            commentlist.append(commentdic)
        else:
            break

    outputweibofile = open('weibo'+str(commentNumPointer)+'.txt','w',encoding='utf-8')
    dictoutput = {'main':zhengwenlist[commentNumPointer],'comment':commentlist}
    outputweibofile.write(str(dictoutput))
    outputweibofile.close()
    commentNumPointer=commentNumPointer+1