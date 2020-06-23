import GetUrl
import requests
import json
#  @author Longm
#  @date 2020/6/23 16:34
#  Blog https://Longm.top
from lxml import etree
def get(studentid=None,studentname=None):
    if studentname!=None:
        jwzx=GetUrl.jwzx()
        url=jwzx+'/data/json_StudentSearch.php?searchKey='+studentname
        res=requests.get(url)
        cx=json.loads(res.text)
        data=cx['returnData'][0]
        return data
    if studentid!=None:
        jwzx = GetUrl.jwzx()
        url = jwzx + '/kebiao/kb_stu.php?xh=' + studentid
        res = requests.get(url)
        html=etree.HTML(res.text)
        tbody=html.xpath(r'//*[@id="kbStuTabs-list"]/div/table//tr') #10个title
        kb={}
        for i in range(len(tbody)-1):
            temp = html.xpath(r'//*[@id="kbStuTabs-list"]/div/table//tbody//tr['+str(i+1)+']//td/text()')  # 10个title
            if len(temp)<4:
                templist=list(kb[str(i)])
                templist[5]=temp[0]
                templist[6]=temp[1]
                templist[7]=temp[2]
                kb[str(i + 1)] = templist
            else:
                kb[str(i + 1)] = temp
        kb["total"]=len(tbody)-1
        return json.dumps(kb,ensure_ascii=False)