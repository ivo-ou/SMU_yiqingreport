##############
# auto_demo 建议放在服务器自动运行
# 或者在windows系统新建任务计划，设置定时
# 完全解放双手

import requests
import json
import random
import threading
import time

phone1 = ""
phone2 = ""



# 重发次数
num = 3

log = []
def report(phonenum):           #未返校

    log.append("手机号码"+str(phonenum))
    params = {
        "phone": phonenum
    }

    ###############################


    mydata = {  # 填报数据
    "shentijiankang": "身体良好，无症状",
	"laifang": "否",
	"residence": "否",
	"zhonggao": "无",
	"fare": "否",
	"yisi": "否",
	"quezhen": "否",
	"jiechu": "否",
	"openid": "",
	"wenzhoulaifang": 2,
	"xiaoqu": "本部校区",       # 本部校区/顺德校区
	"zhuangtai": "非住校",     # 住校/非住校
	"jutizhuangtai": "住家",  # 非住校时：住培养单位/住实习单位/住家/其他  住校时：顺德校区/本部校区
	"wenzhoulaifangtime": ""
    }

    ########################################


    sess = requests.Session()

    portal_url = "http://tougao.gdaw.net/Home2020/NanFangYiKe/baomingyanzheng.html"
    r = sess.get(portal_url, params=params)  # 每日填报登录

    Tb_url = "http://tougao.gdaw.net/Home2020/NanFangYiKe/baomingInsert5.html"
    r = sess.post(Tb_url, data=mydata)  # 每日填报表单提交
    time.sleep(1)
    #print("----------------------------------")
    status = r.text.strip()


    status = r.text.strip()

    if status == "1":
        # print("填报成功")
        log.append("每日健康:填报成功")
    elif status == "2":
        # print("此手机号码主人，已经报名成功了，不能重复报名")
        log.append("每日健康:此手机号码主人，已经报名成功了，不能重复报名")
    elif status == "3":
        # print("请填写完整表单")
        log.append("每日健康:请填写完整表单")
    else:
        if "您今天已经填写过了" in status:
            # print("您今天已经填写过了")
            log.append("每日健康:您今天已经填写过了")
        else:
            print('数据保存失败')
            log.append("每日健康:数据保存失败")
    #print("----------------------------------")
    ########################################

    portal_url = "http://tougao.gdaw.net/Home2020/NanFangYiKe/meiriwendu.html"
    r = sess.get(portal_url, params=params)  # 温度填报get方法请求
    response = r.text.strip()
    idlocationhead = response.find("dataList:'") + 17
    idlocationend = idlocationhead + 7
    userid = response[idlocationhead:idlocationend]  # 获得id
    #print("您的手机号码是：" + str(phonenum))
    #print("您的id是：" + userid)
    zaoshangwendu = random.random() + 36
    zaoshangwendu = round(zaoshangwendu, 1)
    zhongwuwendu = random.random() + 36
    zhongwuwendu = round(zhongwuwendu, 1)
    wanshangwendu = random.random() + 36
    wanshangwendu = round(wanshangwendu, 1)  # 生成随机温度数据
    ########################################
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

    #print("随机早上温度：" + str(zaoshangwendu))
    #print("随机中午温度：" + str(zhongwuwendu))
    #print("随机晚上温度：" + str(wanshangwendu))
    #print("----------------------------------")
    ########################################

    Tb_url = "http://tougao.gdaw.net/Home2020/NanFangYiKe/wenduupdate.html"
    r = sess.post(Tb_url, json=wddata0)  # 温度填报表单提交（早上）
    time.sleep(1)
    status = r.text.strip()

    # 失败重发3次
    if status != "1":
        for i in range(num):
            r = sess.post(Tb_url, json=wddata0)  # 温度填报表单提交（早上）
            time.sleep(2)
    status = r.text.strip()

    if status == "1":
        #print("早上温度：填报成功")
        log.append("早上温度：填报成功 "+ str(zaoshangwendu) + "度")
    else:
        #print("早上温度：数据保存失败")
        log.append("早上温度：数据保存失败")

    Tb_url = "http://tougao.gdaw.net/Home2020/NanFangYiKe/wenduupdate.html"
    r = sess.post(Tb_url, json=wddata1)  # 温度填报表单提交（中午）
    time.sleep(1)
    status = r.text.strip()

    # 失败重发3次
    if status != "1":
        for i in range(num):
            r = sess.post(Tb_url, json=wddata1)  # 温度填报表单提交（中午）
            time.sleep(2)
    status = r.text.strip()

    if status == "1":
        #print("中午温度：填报成功")
        log.append("中午温度：填报成功 "+ str(zhongwuwendu) + "度")
    else:
        #print("中午温度：数据保存失败")
        log.append("中午温度：数据保存失败")

    Tb_url = "http://tougao.gdaw.net/Home2020/NanFangYiKe/wenduupdate.html"
    r = sess.post(Tb_url, json=wddata2)  # 温度填报表单提交（晚上）
    time.sleep(1)

    status = r.text.strip()
    # 失败重发3次
    if status != "1":
        for i in range(num):
            r = sess.post(Tb_url, json=wddata2)  # 温度填报表单提交（晚上）
            time.sleep(2)
    status = r.text.strip()

    if status == "1":
        #print("晚上温度：填报成功")
        log.append("晚上温度：填报成功 "+ str(wanshangwendu) + "度")
    else:
        #print("晚上温度：数据保存失败")
        log.append("晚上温度：数据保存失败")
    log.append("    ")
    log.append("    ")





if __name__ == '__main__':

    report(phone1)      # 未住校 住家

    print(str(log))         # 在命令行显示结果
    # server酱（自行百度http://sc.ftqq.com/3.version）
    api = "https://sc.ftqq.com/{SCKEY}.send"  # 填写自己的key
    title = u"每日填报"

    data = {
       "text":title,
       "desp":str(log)
    }
    req = requests.post(api, data = data)