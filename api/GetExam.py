import LoginApi
import GetUrl
import GetCookie
import requests
import json
from lxml import etree
def GetExam(username,password):
    if LoginApi.getlogin(username, password) == '登录成功':
        url = GetUrl.jwzx()
        cookies = GetCookie.get(username)
        seesion = requests.session()
        seesion.cookies['PHPSESSID'] = cookies
        try:
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:32.0) Gecko/20100101 Firefox/32.0",
                "Accept": "*/*",
                "Accept-Language": "zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3",
                "Accept-Encoding": "gzip, deflate",
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                "Referer": "https://ids.cqupt.edu.cn/authserver/login?service=http%3A%2F%2Fjwc.cqupt.edu.cn%2Ftysfrz%2Findex.php",
                "X-Requested-With": "XMLHttpRequest",
                "Connection": "keep-alive",
                "Pragma": "no-cache",
                "Cache-Control": "no-cache"
            }
            req = seesion.get(url + '/student/ksap.php', headers=headers)
            data=getdata(req.text)
            return data
        except:
            data = {
                "data": {},
                "code": "1"
            }
            return data
    else:
        data = {
            "data": {},
            "code": "1"
        }
        return data
def getdata(text):
    html=etree.HTML(text)
    exam=html.xpath('//*[@id="stuKsTab-ks"]/table/tbody//tr')
    task={}
    for i in range(len(exam)):
        test=html.xpath('//*[@id="stuKsTab-ks"]/table/tbody//tr['+str(i+1)+']//text()')
        task[str(i+1)]=test
    task["total"]=len(exam)
    return json.dumps(task,ensure_ascii=False)