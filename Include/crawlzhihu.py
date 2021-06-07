from splinter import Browser
import time
import random
import re
import requests

cookies = 'zap=171af4d3-5347-4906-a15d-6938340237f6; d_c0="AKDRF0GKkxGPTuV6cOQ-sl0P0nthWmBV3i0=|1594739021"; _ga=GA1.2.447576262.1594739021; _xsrf=pEGscxm2dTPWPE2srWqSag955X5aQsux; __snaker__id=bmytn8pIUXSed8DY; _9755xjdesxxd_=32; YD00517437729195%3AWM_TID=Dnp%2BDyM0o%2BRFUEAFEFYuahgHQFIlUYZ%2F; q_c1=5b10286b8015426db2b1d10c8825ce6b|1616725829000|1595211687000; capsion_ticket="2|1:0|10:1622344355|14:capsion_ticket|44:YWNmOWQ5YjFhOGFiNGIyNWFjZTU0NTJiYzk5MGI3ZjE=|9940be2ed32296fb2c7cc41ba8a6a8dd4825a78ad35aa000c4f71477ed088a01"; tst=r; SESSIONID=dILxKYuFBSDryyf249VQvSWPifyCb1mKPpGTUvsIFCz; JOID=U1AcB0KHhhLkkzDaYYJ3B5_Xv0h46s5TkdBgrirN3Feb50G1UsewpoGSONZhCisBI2hTlgoI0y3yZH7eMQvQvfI=; osd=UFkRAUyEjx_inTPTbIR5BJbauUZ748NVn9NpoyzD316W4U-2W8q2qIKbNdBvCSIMJWZQnwcO3S77aXjQMgLdu_w=; captcha_session_v2="2|1:0|10:1622424146|18:captcha_session_v2|88:OUwybkphdnpZa1F5V25mS3I2dnJkeWZWbTBxV0RMdS9Oa2Y5dDJSSXlvS0xFbHh1QTJkNm9zVFJEQXk1WFR6MA==|d7d5a72d5c79a6d08230f659f6f661440836354af721127f12cdc929487db3d4"; gdxidpyhxdE=wDXwXhqxYg%2Frd%2Bp%2BIfsXN3%5CYo1pOD2YsvNr0liA15v8mAsLkyVIdlzCocMb%2F0CCLE6WzU1IbzTUH7LEAtSrUasu%5C0YJr8vxziwKxHdNfj7Gm30Y1YXa%2Bf2Z0J2%5CJL0cHJ6xiu%2BqflH0HwilPfvP7b4XoOLuqpjGITYS%2B7i2feznlpp3m%3A1622425049064; YD00517437729195%3AWM_NI=5%2BSWR6Sb4bOVqCKpJwIuM9bWJszI%2Fc9S%2FB2VqhECXdUkRGyBkBJ%2BjWESYd2RE3u8yTKzdzez7mcBW7V%2BvbCErTPe8SkYbrHUnk7Dqs0JouWuChxZOKVcUw5eXTeQ61bkRXE%3D; YD00517437729195%3AWM_NIKE=9ca17ae2e6ffcda170e2e6eed1ae72b78ce5b5bb4689928aa7d45a939f9faef468f58b9aa6c17ef2af00acb12af0fea7c3b92af7f59db8d13e91befc83ce5eb39d8591c97d8bab83dae15d8aadb6aaae69fb8de1a3b15eb3b88ba4db7097b59ea8fc4aa99e86cce95d878d9785b15a87edbbd9fc6089a6ac9be872f5b3ada3d63d96f5ba83c24fb28ca086bb59a987ae93cb5faeb5f9a5f479f496a196d67f81b8b8bbce4196bd9b98b86f9c8cabb2b53ba2b59eb9c837e2a3; captcha_ticket_v2="2|1:0|10:1622424162|17:captcha_ticket_v2|704:eyJ2YWxpZGF0ZSI6IkNOMzFfVV80LldXRWpYZzJRS2NXbWVnV19wbHA1dUZmaE0tbXBiRGFtX1JyNldIaHJEY3JzaDFYT3Vfb2Flb3pkbll2QTFoQ2hqdG9Ienh4NWtsb0lWdkRSR3B0cFpLTUp2RlJwc2ZuYUV3UlZfOU9tQnNkX0gtSjl1N1JQbDZWeUxxMWZ2eU96dWswaFRQaWk3MFVWdjRJYmh0T2dKTnZsTzlIVC1OTlN0OHluR253bUJwcnlsU3prT0s3c0s2a3Fyal9td1pRN1BWci4uMlJGMVFRbkFlX2F5cTZaVUxmR2F3ai1KcDlrMEdRVGtMdURpNTBLYm45cldmUFBnY0Ixc1pDazFtdEFCb2pBQV9PeXZvYWR5ZG9saEo5alBkMi55d3M5dHNNd3VzNzRTTHVaUHBfNkd2LnB0dlBId0tTNEkxU1luYnBwaU5odDQxaDJCYkliaTZQclJhLTJhcWxiQ1BtbVdqTTk2X1FNZW94eG9yWW01UFpSV0JteFE2bVRLS0laWi5fYjdURnZCMm14NFdVc05rRGE3ekZaLU81SlB2LXMybzZuTml5MUlkYy1WNlp6a0lqTnVOR0gtWXhKTEN3dktNaE9BYm84Yy04RmlZa0xtbGZwbW80alBMUU1ubmNQSDZXc0V4ei1nbElYOGxBWklHYmFsNW82YWhhMyJ9|e359e5cdc4a671be2f4c6e705099243504675fc12ac0ca9ade177696aa75cb96"; z_c0="2|1:0|10:1622424162|4:z_c0|92:Mi4xNGFtb0NRQUFBQUFBb05FWFFZcVRFU1lBQUFCZ0FsVk5Zb2loWVFCNFRVXzEwcXpmN25TcDdTekZsTU85cnNJMEtn|d7572824389f234ac010b885f20b3bb10af875bb324c16facc4e99dffc314f1a"; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1622344796,1622349687,1622424133,1622428034; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1622428063; KLBRSID=dc02df4a8178e8c4dfd0a3c8cbd8c726|1622431261|1622424128'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36','cookie':cookies}
browser = Browser(driver_name='chrome')
browser.visit('https://www.zhihu.com/question/460921357')



for i in range(1,200):
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(random.random())
html = browser.html

browser.quit()
#https://www.zhihu.com/question/460921357/answer/1901765118
answerzwlist = re.findall(r'<span class="RichText ztext CopyrightRichText-richText" itemprop="text">(.*?)</span>',html)
answerlist = re.findall(r'https://www.zhihu.com/question/460921357/answer/([0-9]+)',html)
likes = re.findall(r'<button aria-label="赞同 ([^"]*?)"',html)
print(likes)
i=0



for answer in answerlist:
    urlstr = 'https://www.zhihu.com/api/v4/answers/'+answer+'/comments?order=normal&limit=50&offset=0&status=open'
    time.sleep((random.random()*10)+2)
    jsonanswer = requests.get(urlstr,headers=headers).text
    print(jsonanswer)
    resultDist = {}
    resultDist['ID'] = answer
    resultDist['Main']=answerzwlist[i]
    resultDist['Comments'] = jsonanswer
    resultDist['likes']=likes[i].replace(" ","")

    i = i+1
    filezhihu = open('zhihuAnswerAndComment'+str(i)+'.txt','w',encoding='utf-8')
    filezhihu.write(str(resultDist))
    filezhihu.close()

#splinter滑十下，拿到的数据作为总数据。

# ZhihuClient.create_cookies()

# client = ZhihuClient()
# client.login_in_terminal()
# answerc = ZhihuClient.answer('https://api.zhihu.com/v4/answers/124586328').latest_comments
# for comments in answerc:
#     print(comments)


