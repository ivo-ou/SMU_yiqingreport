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
        'xiaoqu': "校本部",  # 校区

        'residence': '否',  # 境外旅行
        'shifoufanhui': '否',  # 返校
        'shentijiankang': '身体良好，无症状',  # 身体状况
        'wenzhoulaifang': '否',  # 温州来访
        'fare': '否',  # 发热
        'yisi': '否',  # 疑似
        'quezhen': '否',  # 确诊
        'jiechu': '否',  # 接触

        ########以下不用填
        'laifang': '否',
        'laifangtime': '',
        'city': "",
        'muqian': '',
        'hesuan': '',
        'hesuanjieguo': '',
        'shifoufanhui': '',
        'shijidaoxiao': '',
        'fanxiaodidian': "",
        'openid': '',
        'country': '',
        'wenzhoufanhui': 2,
        'wenzhouzhongzhuan': 3,
        'wenzhoulaifangtime': '',
        'shisiwenzhoulaifang': '否',
        'shisiwenzhoulaifangtime': '',
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




def report1(phonenum):      #已返校

    log.append("手机号码"+str(phonenum))
    params = {
        "phone": phonenum
    }

    ###############################


    mydata = {  # 填报数据
        'xiaoqu': "校本部",  # 校区

        'residence': '否',  # 境外旅行
        'shifoufanhui': '是',  # 返校
        'shentijiankang': '身体良好，无症状',  # 身体状况
        'wenzhoulaifang': '否',  # 温州来访
        'fare': '否',  # 发热
        'yisi': '否',  # 疑似
        'quezhen': '否',  # 确诊
        'jiechu': '否',  # 接触

        ########以下不用填
        'laifang': '否',
        'laifangtime': '',
        'city': "",
        'muqian': '',
        'hesuan': '',
        'hesuanjieguo': '',
        'shifoufanhui': '',
        'shijidaoxiao': '',
        'fanxiaodidian': "",
        'openid': '',
        'country': '',
        'wenzhoufanhui': 2,
        'wenzhouzhongzhuan': 3,
        'wenzhoulaifangtime': '',
        'shisiwenzhoulaifang': '否',
        'shisiwenzhoulaifangtime': '',
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
    # 失败重发3次
    if status != "1":
        for i in range(num):
            r = sess.post(Tb_url, data=mydata)  # 每日填报表单提交
            time.sleep(2)
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
    # 这里填报了两个人的数据，一个已经返校，一个未返校，如果只有一个人，请把不符合的注释掉（在前面新增 # 注释）
    # 例：我只需要填写未返校，则在 second_thread 前面添加 # 注释即可，反之亦然
    first_thread = threading.Thread(target=report(phone1))       # 未返校
    second_thread = threading.Thread(target=report1(phone2))     # 已返校

    print(str(log))         # 在命令行显示结果
    # server酱（自行百度http://sc.ftqq.com/3.version）
    api = "https://sc.ftqq.com/{SCKEY}.send"  # 填写自己的key
    title = u"每日填报"

    data = {
       "text":title,
       "desp":str(log)
    }
    req = requests.post(api, data = data)