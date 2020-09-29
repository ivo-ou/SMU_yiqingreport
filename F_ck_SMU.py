import time
import requests
import random
import threading
from PyQt5.QtWidgets import QApplication


# 创建互斥锁
lock = threading.Lock()

###############################

def meiri(self,phone,xiaoqu):
    # 上锁
    if(len(phone) < 11):
        write_log_to_Text(self, "请输入正确的手机号码...")
    else:
        write_log_to_Text(self, "每日健康填报初始化中...")
        lock.acquire()
        mydata = {                                   #填报数据
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
        "xiaoqu": xiaoqu,
        "zhuangtai": "住校",
        "jutizhuangtai": xiaoqu,
        "wenzhoulaifangtime": ""

        }

        sess = requests.Session()
        portal_url = "http://tougao.gdaw.net/Home2020/NanFangYiKe/xuebaomingyanzheng.html"
        r = sess.get(portal_url,params = {"phone":phone})                                                #登陆
        write_log_to_Text(self, "每日健康填报中...")
        Tb_url = "http://tougao.gdaw.net/Home2020/NanFangYiKe/baomingInsert5.html"
        r = sess.post(Tb_url,data = mydata)                                                   #表单提交
        time.sleep(1)
        status = r.text.strip()
        write_log_to_Text(self,r.text.find('<h4>'))
        if status == "1":
            #print("填报成功")
            write_log_to_Text(self,"每日健康填报成功")
        elif status == "2":
            #print("此手机号码主人，已经报名成功了，不能重复报名")
            write_log_to_Text(self,"此手机号码主人，已经报名成功了，不能重复报名")
        elif status =="3":
            #print("请填写完整表单")
            write_log_to_Text(self,"请填写完整表单")
        else:
            if "您今天已经填写过了" in status:
                write_log_to_Text(self,"您今天已经填写过了")
            else:
                print('数据保存失败')
                write_log_to_Text(self,"数据保存失败")
        # 释放锁
        lock.release()

##体温填报
def tiwen(self,phone):
    # 上锁
    write_log_to_Text(self,"体温填报初始化中...")
    lock.acquire()

    sess = requests.Session()
    portal_url = "http://tougao.gdaw.net/Home2020/NanFangYiKe/meiriwendu.html"
    r = sess.get(portal_url, params={"phone":phone})  # 温度填报get方法请求
    response = r.text.strip()

    idlocationhead = response.find("dataList:'") + 17
    idlocationend = idlocationhead + 7
    userid = response[idlocationhead:idlocationend]  # 获得id

    [morn, noon, nigh] = temper()  # 生成随机温度
    listWD = [userid, morn, noon, nigh]
    list = ["id", 'zaoshangwendu', 'zhongwuwendu', 'wanshangwendu']
    write_log_to_Text(self, "体温填报中...")
    Tb_url = "http://tougao.gdaw.net/Home2020/NanFangYiKe/wenduupdate.html"
    # 分三次提交温度
    for num in range(1, 4):
        temp = listWD.copy()
        i = num - 3
        while i < 0:
            temp[i] = 0
            i = i + 1
        # temp[num::] = "0"
        temp = dict(zip(list, temp))  # 合并
        r = sess.post(Tb_url, json=temp)
        time.sleep(1)
        status = r.text.strip()
    if status == "1":
        write_log_to_Text(self,"早上温度:" + str(listWD[1]))
        write_log_to_Text(self,"中午温度:" + str(listWD[2]))
        write_log_to_Text(self,"晚上温度:" + str(listWD[3]))

    else:
        write_log_to_Text(self,"温度填报失败")

    # 释放锁
    lock.release()

def temper():
    # 生成随机温度
    morn = round((random.randint(3,7)/10 + 36), 1)
    noon = round((random.randint(3,7)/10 + 36), 1)
    nigh = round((random.randint(3,7)/10 + 36), 1)
    return morn, noon, nigh

def get_name(self,phone):
    sess = requests.Session()
    portal_url = "http://tougao.gdaw.net/Home2020/NanFangYiKe/meiriwendu.html"
    r = sess.get(portal_url, params={"phone": phone})  # 温度填报get方法请求
    response = r.text.strip()
    nameIndex = response.find('"name":')
    temp = response[nameIndex + 8:nameIndex + 50]
    name = temp.split('",')
    name = ''.join(name[0])
    name = name.encode('utf-8').decode('unicode_escape')
    print(name)
    self.name_lable.setText("姓名：" + name)
    QApplication.processEvents()


# 获取当前时间
def get_current_time():
    current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    return current_time

# 日志动态打印
def write_log_to_Text(self, logmsg):
    current_time = get_current_time()
    logmsg_in = str(current_time) + " " + str(logmsg) + "\n"  # 换行
    self.text_log.append(logmsg_in)
    QApplication.processEvents()



