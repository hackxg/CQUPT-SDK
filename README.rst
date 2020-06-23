=========
CQUPT-SDK
=========
LongM
^^^^^^^^
- 简介
   +
    这是一个爬取重庆邮电大学教务在线数据的工具库，灵感来源于@juzi,他开发一个在Java可以运行的CQUPT-SDK，所以我开发了Python版本。
    这个库可以支撑你开发属于你自己的校园应用，不再让项目终止于无法获取校园数据这个问题上。

   *
    我设置了cookie保留机制与cookie有效性判断机制，避免重复访问导致并发量过高。
    
   *
    如果你需要内外网入修改config中对应地址即可
   *
    安装方式： pip install CQUPT-SDK

- Login登录
    + Login(username,passwd)你需要提供 **统一识别认证码** **对应的密码**

    + 登录后会在本地保存Cookie信息

- GetStudentInfoService获取信息
    + GetStudentInfoService(username,passwd,code)

    + 同样需要提供 **统一识别认证码** **对应的密码** 会首先判断cookie是否有效，无效时重拨

    + code代表信息类别

    - code=1 获取基本信息

    - code=2 获取扩展信息

    - code=3 #获取照片 返回base64格式

- GetStudentSchedule获取学生课表
    + GetStudentSchedule(studentid=None,studentname=None)

    + 此接口无需登录你需要提供 studenid：学号 或者 studentname：学生姓名

    + 对应的是通过学号直接查询课表 通过姓名查询课表（返回学生列表与学号 自行处理）

- GetStudentExam获取考试安排
    + GetStudentExam(username,passwd)
    + 提供 **统一识别认证码** **对应的密码**
    + 返回json格式 自行处理

- GetNullRoom获取空教室
    + GetNullRoom(start,end,week,time1=False,time2=False,time3=False,time4=False,time5=False,time6=False)
    + start 起始周 end 结束周 week 星期 time1：1-2节 time2：3-4节 ..... time6: 11-12节
    + 返回列表 [‘2115’,‘2116’,‘2117’] 自行处理


2020/6/23
---------
