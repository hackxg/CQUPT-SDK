import requests
import GetCookie
import LoginApi
import GetUrl
#  @author Longm
#  @date 2020/6/23 16:34
#  Blog https://Longm.top
from lxml import etree
def getinfo1(username,password):#学生基本信息
    if LoginApi.getlogin(username, password)== '登录成功':
        url=GetUrl.jwzx()
        cookies=GetCookie.get(username)
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
            req=seesion.get(url+'/user.php',headers=headers)
            json = getdata1(req.text)
            return json
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

def getinfo2(username,password):
    if LoginApi.getlogin(username, password)== '登录成功':
        url=GetUrl.jwzx()
        cookies=GetCookie.get(username)
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
            req=seesion.get(url+'/student/xj.php',headers=headers)
            json = getdata2(req.text)
            return json
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

def getinfo3(username,password):
    if LoginApi.getlogin(username, password)== '登录成功':
        StudentId=GetCookie.getStudentId(username)
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
            req = seesion.get(url + '/showstupic.php?xh='+StudentId, headers=headers)
            base64_data = req.content # 使用base64进行加密
            return base64_data
        except:
            pass
def getdata1(text):
    html = etree.HTML(text)
    temp = html.xpath(r'//tbody//tr//td/text()')
    stuNumber = temp[1]
    realName = temp[3]
    grade = temp[5]
    academy = temp[9]
    data = {"data":{
            "stuNumber": stuNumber,
            "realName": realName,
            "grade": grade,
            "academy": academy},
        "code":"0"
        }
    return data
def getdata2(text):
    html = etree.HTML(text)
    idtemp = html.xpath(r'//*[@id="xjTabs-xjInfo"]/table/tr[8]//text()') #身份证号 2 出生年月 4
    colleg = html.xpath(r'//*[@id="xjTabs-xjInfo"]/table/tr[14]//text()')  # 考生号 2 通知书号 4
    id=idtemp[2]
    Bdate=idtemp[5]
    ksh=colleg[2]
    tzsh=colleg[5]
    data = {
        "data":{
            "id": id,
            "Bdate": Bdate,
            "ksh": ksh,
            "tzsh": tzsh
        },
        "code":"0"
        }
    return data
