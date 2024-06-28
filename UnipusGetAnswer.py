import requests
import re
import json
import os
import time
import random
import jwt
import fake_useragent


Ua_list = fake_useragent.UserAgent()
seed_list = ['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q',"R",'S','T','U','V','W','X','Y','Z']
def Xtoken_create():
    global token_create
    fake_id = ''.join(random.sample(seed_list, 32))
    fake_iss = ''.join(random.sample(seed_list, 20))
    token_body = {
        "open_id":fake_id,"name":"","email":"","administrator":'false',"exp":1902970157000,"iss":fake_iss,"aud":"edx.unipus.cn"
    }
    token_header = {"typ":"JWT","alg":"HS256"}

    jwt_token = jwt.encode(token_body,'',algorithm="HS256",headers=token_header).decode("utf-8")
    return jwt_token

requests_headers = {
    'Host': 'ucontent.unipus.cn',
    'User-Agent':Ua_list.random,
    'Accept':'*/*',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'X-CSRFTOKEN': ''.join(random.sample(seed_list, 32)),
    'X-ANNOTATOR-AUTH-TOKEN': Xtoken_create(),
    'Content-type': 'application/json',
    'Connection': 'keep-alive',
    'TE': 'Trailers'

}

def extract_qa(question_obj):
    if "answer" in question_obj.keys():
        return (question_obj["content"]["html"], question_obj["answer"])
    elif "answers" in question_obj.keys():
        return (question_obj["content"]["html"], question_obj["answers"])

def Request_get(requests_header,input_url):
    try:
        url_deal = input_url.split('/')
        target_url = 'https://ucontent.unipus.cn/course/api/content/'+url_deal[5]+'/'+url_deal[-2]+'/default/'
        try : 
            rec_text = requests.get(target_url,headers = requests_header).text
            answer_sort = re.findall(r'content_(.*?):scoopquestions',rec_text)
            answer_show(rec_text,answer_sort)
        except:
            print('网址输入错误')
            return
    except:
        if content_obj:
            print(json.dumps(content_obj, indent=2))
        print('网址输入错误')
        return

def answer_show(answers_text,sort):
    if len(sort) > 1:
        print('\t该页有两题及以上答案，顺序为')
        for i in sort:
            print('\t    第'+i+'题')
        print('\n请自行判断答案顺序！\n')
    pos = 1
    text_deal = re.findall(r"\\\"answers\\\":\[\\\"(.*?)\\\"\]",answers_text)
    if text_deal :
        print("\t----获取成功！----\n")
        for word in text_deal:
            word = word.replace('"','')
            answers = "".join(re.findall(r"[A-Z0-9a-z -,]",word))    
            print('\t    '+str(pos)+'题答案 '+answers)
            pos = pos + 1
    else:
        text_deal = re.findall(r"\\\"answer\\\":\\\"(.*?)\\\",",answers_text)
        if text_deal :
            print("\t  ----获取成功！---- \n")
            for word in text_deal:
                word = word.replace('"','')
                answers = "".join(re.findall(r"[A-Z0-9a-z -,]",word))    
                print('\t    '+str(pos)+'题答案 '+answers)
                pos = pos + 1
        else:
            #os.system("color 04")
            print("\t----获取失败！----\n")
            print('当前页面似乎没有答案或请求失效。请注意无法获取单元测试答案！！\n')
            print("请检查网址是否正确，或稍后重试！！！\n")
            time.sleep(3)
            #os.system("color 0a")

def input_check(url):
    result_check = re.findall(r"courseware",url)
    result_check_2 = re.findall(r"ucontent.unipus.cn",url)
    if result_check:
        if result_check_2:
            return 1    
        else:
            return -1    
    else:
        return -1
        

if __name__ == "__main__":
    answer_url = input('\n请输入需要获取答案的页面网址。请注意！！没有答案的页面会出错。\n')
    while(1):
        if input_check(answer_url) == 1 :
            #os.system("cls")
            print("---------------------开始获取，请稍等！！-------------------------")
            time.sleep(0.5)
            Request_get(requests_headers,answer_url)
            time.sleep(1)
        else:
            print("输入网址有误！请重新输入！")
            time.sleep(0.2)
            #os.system("cls")
        answer_url = input('\n请输入需要获取答案的页面网址。请注意！！没有答案的页面会出错。\n')
        
        
