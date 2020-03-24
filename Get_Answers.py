import requests
import re
import json
import os
import time
os.system("title U校园答案获取器")
os.system('@echo off')
os.system("color 0a")
headers = {
    #请从自己的浏览器中获取
}
while(1):
    url = input('请输入需要获取答案的页面网址。请注意！！没有答案的页面会出错。\n')
    url_deal = url.split('/')
    target_url = 'https://ucontent.unipus.cn/course/api/content/'+url_deal[5]+'/'+url_deal[-2]+'/default/'
    try : 
        rec = requests.get(target_url,headers = headers).text
        
    except  requests.exceptions.ConnectionError:
        print('网址输入错误')
    pos = 1
    word_2 = re.findall(r"answers.*?:.*?\"(.*?)\".*?,",rec)
    if word_2 :
        for word in word_2:
            word_3 = "".join(re.findall(r"[A-Z0-9a-z -]",word))    
            check_pos = word_3
            print(str(pos)+'题答案'+word_3)
            pos = pos + 1
    else:
        word_2 = re.findall(r"answer.*?:.*?\"(.*?)\".*?,",rec)
        if word_2 :
            for word in word_2:
                word_3 = "".join(re.findall(r"[A-Z0-9a-z -]",word))    
                check_pos = word_3
                print(str(pos)+'题答案'+word_3)
                pos = pos + 1
        else:
            os.system("color 04")
            print('网址错误或其他问题，未能获取答案。请注意无法获取单元测试答案！！\n')
            print("请检查网络，或稍后重试！！！\n")
            time.sleep(2)
            os.system("color 0a")
