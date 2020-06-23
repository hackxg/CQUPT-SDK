import GetUrl
import requests
from lxml import etree
def get(start,end,week,time1,time2,time3,time4,time5,time6):
    Link =GetUrl.jwzx()+'/kebiao/emptyRoomSearch.php?'+'zcStart='+start+'&zcEnd='+end+'&xq='+week
    if (time1 == True):
        Link=Link+'&sd[]=2'
    if (time2 == True):
        Link = Link + '&sd[]=4'
    if (time3== True):
        Link = Link + '&sd[]=6'
    if (time4 == True):
        Link = Link + '&sd[]=8'
    if (time5 == True):
        Link = Link + '&sd[]=10'
    if (time6 == True):
        Link = Link + '&sd[]=12'
    res=requests.get(Link)
    html=etree.HTML(res.text)
    room=html.xpath(r'/html/body/table/tbody//tr//text()')
    nullroom=[]
    for i in range(0,len(room),2):
        temp=str(room[i]).replace("\r\n\t","")
        nullroom.append(temp)
    return nullroom