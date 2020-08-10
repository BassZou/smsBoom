# coding: utf-8

import urllib.request
import requests
import json
import random
import time
import hashlib

'''
短信验证码 - smsCodeTask
'''
headers={"Content-Type":"text/plain"}


'''
App 迪士尼 photopass
curl 'https://api.disneyphotopass.com.cn/userMsg/sendSMSValidateCode'  
-H 'Host: api.disneyphotopass.com.cn'  
-H 'Content-Type: application/json'  
-H 'Connection: keep-alive'  
-H 'Accept: */*'  
-H 'User-Agent: PhotoPass/3.2.7 (iPhone; iOS 13.2.3; Scale/2.00)'  
-H 'Accept-Language: zh-Hans-CN;q=1'  
-H 'Content-Length: 112'  
-H 'Accept-Encoding: gzip, deflate, br'   

--data '{"language":"CN","phone":"+8617891938144","msgType":"register","tokenId":"5d0826a0-dac1-11ea-a565-87c149987f88"}'
'''
def disneyphotopass(users):
    val = 'App 迪士尼 photopass'
    id = str(random.randint(72111,78111))
    mtime = str(int(time.time() * 1000)) # 毫秒时间戳
    browser_id = hashlib.md5(mtime.encode('utf-8')).hexdigest()
    url = ' https://api.disneyphotopass.com.cn/userMsg/sendSMSValidateCode'
    headers = {
        'Host':'api.disneyphotopass.com.cn',
        'Content-Type':'application/json',
        'Connection': 'keep-alive',
        'Accept': '*/*',
        'User-Agent': 'PhotoPass/3.2.7 (iPhone; iOS 13.2.3; Scale/2.00)',
        'Accept-Language': 'zh-Hans-CN;q=1',
        'Content-Length': '112',
        'Accept-Encoding': 'gzip, deflate, br'
    }
    # print(url)
    data = {
            "language":"CN",
            "phone":"+86"+users['phone'],
            "msgType":"register",
            "tokenId":"5d0826a0-dac1-11ea-a565-87c149987f88"
            # "tokenId": browser_id
        }
    # res=requests.post(url=url,data = data,headers=headers)
    res=requests.post(url=url,headers=headers,data= json.dumps(data))
    if(res.status_code == 200):
        print(val,'发送成功',res.encoding,res.apparent_encoding,res.content.decode('utf-8'))
    else:
        print(val,'发送失败','状态码：',res.status_code)