import requests
import json
import random
import threading

# 定义全局变量
my_num = 0

# 创建互斥锁
lock = threading.Lock()

###############################

def meiri(phone,xiaoqu):
    # 上锁
    lock.acquire()
    global my_num

    log = []

###############################



    mydata = {                                   #填报数据
        "xiaoqu": xiaoqu,                     # 校区


        'residence':'否',                        #境外旅行
        'shifoufanhui':'否',                     #返校
        'shentijiankang':'身体良好，无症状',       #身体状况
        'wenzhoulaifang':'否',                   #温州来访
        'fare':'否',                             #发热
        'yisi':'否',                             #疑似
        'quezhen':'否',                          #确诊
        'jiechu':'否',                           #接触

    
########以下不用填
        'laifang':'否',
        'laifangtime':'',
        'city':"",
        'muqian':'',
        'hesuan':'',
        'hesuanjieguo':'',
        'shifoufanhui':'',
        'shijidaoxiao':'',
        'fanxiaodidian':"",
        'openid':'',
        'country':'',
        'wenzhoufanhui':2,
        'wenzhouzhongzhuan':3,
        'wenzhoulaifangtime':'',
        'shisiwenzhoulaifang':'否',
        'shisiwenzhoulaifangtime':'',

    }

########################################


    sess = requests.Session()

    portal_url = "http://tougao.gdaw.net/Home2020/NanFangYiKe/xuebaomingyanzheng.html"
    r = sess.get(portal_url,params = {"phone":phone})                                                #登陆

    Tb_url = "http://tougao.gdaw.net/Home2020/NanFangYiKe/baomingInsert5.html"
    r = sess.post(Tb_url,data = mydata)                                                   #表单提交

    status = r.text.strip()
    if status == "1":
        #print("填报成功")
        log.append("每日健康填报成功")
    elif status == "2":
        #print("此手机号码主人，已经报名成功了，不能重复报名")
        log.append("此手机号码主人，已经报名成功了，不能重复报名")
    elif status =="3":
        #print("请填写完整表单")
        log.append("请填写完整表单")
    else:
        if "您今天已经填写过了" in status:
            #print("您今天已经填写过了")
            log.append("您今天已经填写过了")
        else:
            print('数据保存失败')
            log.append("数据保存失败")
    # 释放锁
    lock.release()
    return log

##体温填报
def tiwen(phone):
    log = []            #创建列表存放数据
    # 上锁
    lock.acquire()
    global my_num

    sess = requests.Session()
    portal_url = "http://tougao.gdaw.net/Home2020/NanFangYiKe/meiriwendu.html"
    r = sess.get(portal_url, params={"phone":phone})  # 温度填报get方法请求
    response = r.text.strip()

    idlocationhead = response.find("dataList:'") + 17
    idlocationend = idlocationhead + 7
    userid = response[idlocationhead:idlocationend]  # 获得id

    zaoshangwendu = random.random() + 36
    zaoshangwendu = round(zaoshangwendu, 1)
    zhongwuwendu = random.random() + 36
    zhongwuwendu = round(zhongwuwendu, 1)
    wanshangwendu = random.random() + 36
    wanshangwendu = round(wanshangwendu, 1)  # 生成随机温度数据
    wddata0 = {
        "id": userid,
        "zaoshangwendu": zaoshangwendu,
        "zhongwuwendu": 0,
        "wanshangwendu": 0}

    wddata1 = {
        "id": userid,
        "zaoshangwendu": zaoshangwendu,
        "zhongwuwendu": zhongwuwendu,
        "wanshangwendu": 0}

    wddata2 = {
        "id": userid,
        "zaoshangwendu": zaoshangwendu,
        "zhongwuwendu": zhongwuwendu,
        "wanshangwendu": wanshangwendu}
    log.append("随机早上温度：" + str(zaoshangwendu))
    log.append("随机中午温度：" + str(zhongwuwendu))
    log.append("随机晚上温度：" + str(wanshangwendu))

    Tb_url = "http://tougao.gdaw.net/Home2020/NanFangYiKe/wenduupdate.html"
    r = sess.post(Tb_url, json=wddata0)  # 温度填报表单提交（早上）

    status = r.text.strip()
    if status == "1":
        #print("早上温度：填报成功")
        log.append("早上温度：填报成功")
    else:
        #print("早上温度：数据保存失败")
        log.append("早上温度：数据保存失败")
    Tb_url = "http://tougao.gdaw.net/Home2020/NanFangYiKe/wenduupdate.html"
    r = sess.post(Tb_url, json=wddata1)  # 温度填报表单提交（中午）
    status = r.text.strip()
    if status == "1":
        #print("中午温度：填报成功")
        log.append("中午温度：填报成功")
    else:
        #print("中午温度：数据保存失败")
        log.append("中午温度：数据保存失败")

    Tb_url = "http://tougao.gdaw.net/Home2020/NanFangYiKe/wenduupdate.html"
    r = sess.post(Tb_url, json=wddata2)  # 温度填报表单提交（晚上）

    status = r.text.strip()
    if status == "1":
        #print("晚上温度：填报成功")
        log.append("晚上温度：填报成功")
    else:
        #print("晚上温度：数据保存失败")
        log.append("晚上温度：数据保存失败")
    # 释放锁
    lock.release()
    return log




