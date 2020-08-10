# coding: utf-8

import urllib.request
import requests
import json
import random
import time
import hashlib

'''
留言板-人工电话 - mesCallTask
'''


headers={"Content-Type":"text/plain"}


'''
.	curl 'https://schoolsbak.idp.cn/index.php?m=formguide&c=index&a=show&formid=24&siteid=1' \
.	  -H 'authority: schoolsbak.idp.cn' \
.	  -H 'sec-ch-ua: "\\Not;A\"Brand";v="99", "Google Chrome";v="85", "Chromium";v="85"' \
.	  -H 'accept: application/json, text/javascript, */*; q=0.01' \
.	  -H 'sec-ch-ua-mobile: ?1' \
.	  -H 'user-agent: Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.59 Mobile Safari/537.36' \
.	  -H 'content-type: application/x-www-form-urlencoded; charset=UTF-8' \
.	  -H 'origin: https://www.idp.cn' \
.	  -H 'sec-fetch-site: same-site' \
.	  -H 'sec-fetch-mode: cors' \
.	  -H 'sec-fetch-dest: empty' \
.	  -H 'referer: https://www.idp.cn/' \
.	  -H 'accept-language: zh-CN,zh;q=0.9,ja;q=0.8' \
.	  --data-raw 
.	
.	info[name]: 周先生
.	info[mobile]: 17892948475
.	info[major]: 语言类
.	info[country]: 美国
.	info[stitle]: 世界各国留学申请条件大盘点_pc
.	info[time]: 2020-08 09 23: 29: 42
.	success_msg: 亲爱的同学，您的信息已成功提交！留学咨询热线：400-697-9728
.	dosubmit: 提交
.	info[source]: https://www.idp.cn/special/event/applicationOfTheFiveCountries/?utm_source=baidu&utm_medium=cpc&utm_content=TONGYONG_SH&utm_term=Baidu20181033486&utm_campaign=ns_04
'''
def schoolsbak(users):
    val = 'idp留学 https://www.idp.cn/'
    id = str(random.randint(72111,78111))
    mtime = str(int(time.time() * 1000)) # 毫秒时间戳
    browser_id = hashlib.md5(mtime.encode('utf-8')).hexdigest()
    url = 'https://schoolsbak.idp.cn/index.php?m=formguide&c=index&a=show&formid=24&siteid=1'
    headers = {
        'authority': 'schoolsbak.idp.cn' ,
        'sec-ch-ua': '\\Not;A\"Brand";v="99", "Google Chrome";v="85", "Chromium";v="85"' ,
        'accept': 'application/json, text/javascript, */*; q=0.01' ,
        'sec-ch-ua-mobile': '?1' ,
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.59 Mobile Safari/537.36' ,
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8' ,
        'origin': 'https://www.idp.cn' ,
        'sec-fetch-site': 'same-site' ,
        'sec-fetch-mode': 'cors' ,
        'sec-fetch-dest': 'empty' ,
        'referer': 'https://www.idp.cn/' ,
        'accept-language': 'zh-CN,zh;q=0.9,ja;q=0.8' 
    }
    # print(url)
    data = {
        'info[name]': users['name'],
        'info[mobile]': users['phone'],
        'info[major]': users['major'],
        'info[country]': '美国',
        'info[stitle]': '世界各国留学申请条件大盘点_pc',
        # 'info[time]': 2020-08 09 23: 29: 42
        'info[time]': mtime,
        'success_msg': '亲爱的同学，您的信息已成功提交！留学咨询热线：400-697-9728',
        'dosubmit': '提交',
        'info[source]': 'https://www.idp.cn/special/event/applicationOfTheFiveCountries/?utm_source=baidu&utm_medium=cpc&utm_content=TONGYONG_SH&utm_term=Baidu20181033486&utm_campaign=ns_04'
    }
    res=requests.post(url=url,data = data,headers=headers)

    if(res.status_code == 200):
        # res_json = json.loads(res.text)
        # xxx = res_json['']
        print(val,'发送成功',res.encoding,res.apparent_encoding,res.content.decode('utf-8'))
    else:
        print(val,'发送失败','状态码：',res.status_code)


'''
curl 'https://new-api.meiqia.com/client/attrs_jsonp?ent_id=72111&track_id=1frTe5RBJVdW7nMwSXsvVjc5gSs&visit_id=1frTgDUOSlKQY5TN2FL3Szo6qwq&browser_id=f2c7a6db20972b864deb7f2e0d0b7faf&attrs={"tel":"17891938142"}&v=1596980639204&jsonp_cb=jsonp_cb' \
  -H 'Connection: keep-alive' \
  -H 'sec-ch-ua: "\\Not;A\"Brand";v="99", "Google Chrome";v="85", "Chromium";v="85"' \
  -H 'sec-ch-ua-mobile: ?1' \
  -H 'User-Agent: Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.59 Mobile Safari/537.36' \
  -H 'Accept: */*' \
  -H 'Sec-Fetch-Site: cross-site' \
  -H 'Sec-Fetch-Mode: no-cors' \
  -H 'Sec-Fetch-Dest: script' \
  -H 'Referer: https://www.liuxue.com/' \
  -H 'Accept-Language: zh-CN,zh;q=0.9,ja;q=0.8' \
  -H 'Cookie: MEIQIA_TRACK_ID=1frTe5RBJVdW7nMwSXsvVjc5gSs' \
  --compressed
'''
def liuxue(users):
    val = '顺顺留学 https://www.liuxue.com/'
    id = str(random.randint(72111,78111))
    mtime = str(int(time.time() * 1000)) # 毫秒时间戳
    browser_id = hashlib.md5(mtime.encode('utf-8')).hexdigest()
    url = 'https://new-api.meiqia.com/client/attrs_jsonp?ent_id=72111&track_id=1frTe5RBJVdW7nMwSXsvVjc5gSs&visit_id=1frTgDUOSlKQY5TN2FL3Szo6qwq&browser_id='+ browser_id +'&attrs={"tel":"'+ users['phone'] +'"}&v='+mtime+'&jsonp_cb=jsonp_cb'
    # print(url)
    res=requests.get(url=url,headers=headers)
    if(res.status_code == 200):
        # res_json = json.loads(res.text)
        # xxx = res_json['']
        print(val,'发送成功',res.text)
    else:
        print(val,'发送失败','状态码：',res.status_code)