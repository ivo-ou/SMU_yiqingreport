# -*- coding: utf-8 -*-

import os
import sys
import time
import requests
from random import randint
import threading
from cv2 import imwrite, imread, cvtColor, COLOR_BGR2RGB, COLOR_RGB2BGR
from PyQt5.QtWidgets import QApplication
from PIL import Image, ImageDraw, ImageFont
from numpy import asarray


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
    if (len(phone) < 11):
        write_log_to_Text(self, "请输入正确的手机号码...")
    else:
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
        text = ["早上温度:", "中午温度:", "晚上温度:"]
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
                write_log_to_Text(self,text[num-1] + str(listWD[1]))
                QApplication.processEvents()
            else:
                write_log_to_Text(self, text[num-1] + "填报失败")
        # 判断是否生成截图
        if(self.jietu_btngroup.checkedId() == -2):   # 选择 是
            print("当前选项为生成截图")
            path = dealpic(self.name_lable.text()[3:],listWD)
            write_log_to_Text(self, "截图保存成功 " + path)
        else:
            print("当前选项为不生成截图")



        # 释放锁
        lock.release()

def temper():
    # 生成随机温度
    morn = round((randint(3,7)/10 + 36), 1)
    noon = round((randint(3,7)/10 + 36), 1)
    nigh = round((randint(3,7)/10 + 36), 1)
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
    if (len(name) < 10):
        print("获取的姓名："  + name)
        self.name_lable.setText("姓名：" + name)
        write_log_to_Text(self, name + "，欢迎使用SMU填报工具")
    else:
        self.name_lable.setText("姓名：无法识别")
        write_log_to_Text(self,"姓名无法识别，请检查手机号码！")
    QApplication.processEvents()
    return name


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

def dealpic(name,tiwen):
    #pic = "/Users/chestnuta/Documents/PycharmProjects/F_ck_SMU/img/tiwen.png"
    #img = cv2.imread(os.path.dirname(sys.argv[0]) + "/tiwen.png")
    pic = resource_path(os.path.join("res", "tiwen.png"))
    img = imread(pic)
    img_PIL = Image.fromarray(cvtColor(img, COLOR_BGR2RGB))
    font = ImageFont.truetype(resource_path(os.path.join("res", "msyh.ttf")),14)
    # 需要先把输出的中文字符转换成Unicode编码形式
    if not isinstance(name, str):
        name = name.decode('utf8')
    draw = ImageDraw.Draw(img_PIL)
    draw.text((20,76),name,font = font,fill = (0,0,0))
    font = ImageFont.truetype(resource_path(os.path.join("res", "Helvetica.ttf")), 14)
    draw.text((34, 192), str(tiwen[1]), font=font, fill=(0, 0, 0))
    draw.text((34, 282), str(tiwen[2]), font=font, fill=(0, 0, 0))
    draw.text((34, 372), str(tiwen[3]), font=font, fill=(0, 0, 0))

    # 转换回OpenCV格式
    img_OpenCV = cvtColor(asarray(img_PIL), COLOR_RGB2BGR)
    #cv2.imshow("print chinese to image", img_OpenCV)
    temppath = os.path.dirname(os.path.realpath(sys.argv[0]))
    print(temppath)
    path = temppath +'/'+ time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime(time.time()))+'.png'
    imwrite(path, img_OpenCV)
    QApplication.processEvents()
    return path

#生成资源文件目录访问路径
def resource_path(relative_path):
    if getattr(sys, 'frozen', False): #是否Bundle Resource
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)







