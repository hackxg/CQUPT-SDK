import requests
import GetCookie
import GetUrl
#  @author Longm
#  @date 2020/6/23 16:34
#  Blog https://Longm.top
def judge(username):
    try:
        cookie=GetCookie.get(username)
        if req(cookie)==True:
            return cookie
        else:
            return 'expire'
    except:
        return 'expire'
def req(cookies):
    try:
        jwzx = GetUrl.jwzx()
        URLus = jwzx+'/user.php'
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
        seesion = requests.session()
        seesion.cookies['PHPSESSID']=cookies
        r=seesion.get(URLus,headers=headers)
        try:
            if r.history==[]:
                print('cookie有效')
                return True
        except:
            return False
    except:return False
