import LoginApi
import GetStudentInfo
import GetSchedule
import GetExam
import GetRoom
 #  @author Longm
 #  @date 2020/6/23 16:34
 #  Blog https://Longm.top

#登录api调用时传入统一识别认证码与密码
#同一账号只需要登录一次 登录后会用配置文件的方式保存cookie
def Login(username,passwd):
    return LoginApi.getlogin(username, passwd)

#需要填入用户密码 在系统判断cookie失效时重新登录
#code=1 获取基本信息 code=2 获取扩展信息 code=3 #获取照片 base64格式
def GetStudentInfoService(username,passwd,code):
    if code=='1':
        return GetStudentInfo.getinfo1(username, passwd) #获取基本信息
    if code=='2':
        return GetStudentInfo.getinfo2(username, passwd) #获取扩展信息
    if code=='3':
        return GetStudentInfo.getinfo3(username, passwd) #获取照片 base64格式

#获取学生课表 /不需要登录/ 注意参数为学号 或 姓名 如果已经登录 可以获取学号 GetCookie.getStudentId()只传一个参数
def GetStudentSchedule(studentid=None,studentname=None):
    return  GetSchedule.get(studentid, studentname)
#需要填入用户密码 在系统判断cookie失效时重新登录

def GetStudentExam(username,passwd):
    return GetExam.GetExam(username,passwd)
#传入参数无需登录
#start 起始周 end 结束周 week 星期 time1：1-2节 time2：3-4节 ..... time6: 11-12节
def GetNullRoom(start,end,week,time1=False,time2=False,time3=False,time4=False,time5=False,time6=False):
    return GetRoom.get(start,end,week,time1,time2,time3,time4,time5,time6)
