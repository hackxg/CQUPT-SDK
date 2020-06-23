import json
#  @author Longm
#  @date 2020/6/23 16:34
#  Blog https://Longm.top
def ids():
    data = open('config/url.json').read()
    djson = json.loads(data)
    ids= djson['ids']
    return ids
def jwzx():
    data = open('config/url.json').read()
    djson = json.loads(data)
    jwzx = djson['jwzx']
    return jwzx