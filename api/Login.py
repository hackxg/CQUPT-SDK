import requests
from lxml import etree
import time
import GetUrl
import Judge
import json
#  @author Longm
#  @date 2020/6/23 16:34
#  Blog https://Longm.top
def main(username,passwd):
    ids=GetUrl.ids()  #获取配置中设置内外网入链接
    jwzx=GetUrl.jwzx()
    data=Judge.judge(username)#判断配置中账号cookie是否有效避免重复登录
    if data=='expire':
        print('cookie无效，再次登录')
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:32.0) Gecko/20100101 Firefox/32.0",
            "Accept": "*/*",
            "Accept-Language": "zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3",
            "Accept-Encoding": "gzip, deflate",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Referer": "https://ids.cqupt.edu.cn/authserver/login?service=http%3A%2F%2Fjwzx.cqupt.edu.cn%2Ftysfrz%2Findex.php",
            "X-Requested-With": "XMLHttpRequest",
            "Connection": "keep-alive",
            "Pragma": "no-cache",
            "Cache-Control": "no-cache"
        }
        URL = ids+'/authserver/login?service=http%3A%2F%2Fjwzx.cqupt.edu.cn%2Ftysfrz%2Findex.php'
        URLin = jwzx+'/index.php'
        URLus = jwzx+'/user.php'
        seesion = requests.session()  # cookie 共用
        try:
            reqlt = seesion.get(URL, headers=headers)
            if "lt" not in reqlt.text:
                data = {
                    "data":
                        "接口失效或繁忙！"
                    ,
                    "code": 1
                }
                return str(data)
            html = etree.HTML(reqlt.text)
            lt = html.xpath('//*[@name="lt"]/@value')[0]
            data = "username=" + username + "&password=" + passwd + "&lt=" + lt + "&execution=e1s1&_eventId=submit&rmShown=1"
            reqck = seesion.post(URL, data=data, headers=headers, allow_redirects=False)
            # 判断登陆是否成功
            if 'Location' in reqck.headers.keys():
                Location = reqck.headers["Location"]  # 登陆成功 获取重定向地址
                seesion.get(Location, headers=headers)
                seesion.get(URLin, headers=headers)
                r = seesion.get(URLus, headers=headers)
                data=getdata(r.text,str(seesion.cookies['PHPSESSID']))
                return data
            else:
                data = {
                    "data":
                        "账号或密码错误！",
                    "code": 3
                }
            return str(data)
        except:
            data = {
                "data":
                    "接口失效或繁忙！"
                ,
                "code": 1
            }
            return str(data)
    else:
        data = open('config/' + username + '.json').read()
        return json.loads(data)
def getdata(text,cookies):
    html = etree.HTML(text)
    temp = html.xpath(r'//tbody//tr//td/text()')
    stuNumber = temp[1]
    realName = temp[3]
    grade = temp[5]
    academy = temp[9]
    data = {
        "data": [{
            'lastTime': time.time(),
            "stuNumber": stuNumber,
            "realName": realName,
            "grade": grade,
            "academy": academy
        }],
        "code": 2
        , "cookies":cookies
    }
    return data
