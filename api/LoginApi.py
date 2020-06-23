import Login
import json
#  @author Longm
#  @date 2020/6/23 16:34
#  Blog https://Longm.top
def getlogin(username,passwd):
    temp = Login.main(username, passwd)
    temp=json.dumps(temp)
    text = json.loads(temp)
    print(text)
    print(text['code'])
    if text['code'] == 2:
        filename = 'config/' + username + '.json'
        with open(filename, 'w') as file_object:
            file_object.write(temp)
        return '登录成功'
    elif text['code'] == 3:
        return '账号或密码错误'
    else:
        return '接口失效或繁忙！'