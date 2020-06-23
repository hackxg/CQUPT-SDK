import json
#  @author Longm
#  @date 2020/6/23 16:34
#  Blog https://Longm.top
def get(username):
    data = open('config/' + username + '.json').read()
    djson = json.loads(data)
    cookie = djson['cookies']
    return cookie
def getStudentId(username):
    data = open('config/' + username + '.json').read()
    djson = json.loads(data)
    getStudentId= djson['data'][0]['stuNumber']
    return getStudentId