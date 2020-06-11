#!/usr/bin/env python
# -*- coding: utf-8 -*-


from tkinter import *
import hashlib
import time
import os
from tkinter import ttk

import F_ck_SMU
import threading

LOG_LINE_NUM = 0


class MY_GUI():
    def __init__(self, init_window_name):
        self.init_window_name = init_window_name

    # 设置窗口
    def set_init_window(self):
        phone, xiaoqu = self.fileread()
        self.init_window_name.title("SMU每日健康填报")  # 窗口名
        # self.init_window_name.geometry('320x160+10+10')                         #290 160为窗口大小，+10 +10 定义窗口弹出时的默认展示位置
        self.init_window_name.geometry('480x300+10+10')
        # self.init_window_name["bg"] = "pink"                                    #窗口背景色，其他背景色见
        # self.init_window_name.attributes("-alpha",0.9)                          #虚化，值越小虚化程度越高
        # 标签
        self.init_data_label = ttk.Label(self.init_window_name, text="操作命令")
        self.init_data_label.grid(row=3, column=0)
        self.init_data_label = ttk.Label(self.init_window_name, text="手机号：")
        self.init_data_label.grid(row=0, column=0, sticky=E)
        self.init_data_label = ttk.Label(self.init_window_name, text="校区：")
        self.init_data_label.grid(row=1, column=0, sticky=E)
        self.log_label = ttk.Label(self.init_window_name, text="日志")
        self.log_label.grid(row=9, column=0)
        # 文本框
        self.init_phone_Text = Text(self.init_window_name, width=13, height=1, relief=RIDGE, bd=1)  # 手机号录入框
        self.init_phone_Text.grid(row=0, column=1, sticky=N + E + W + S)
        self.init_phone_Text.insert('0.0', phone)  # 填入默认号码
        self.init_xiaoqu_Text = Text(self.init_window_name, width=13, height=1, relief=RIDGE, bd=1)  # 校区录入框
        self.init_xiaoqu_Text.grid(row=1, column=1, sticky=N + E + W + S)
        self.init_xiaoqu_Text.insert('0.0', xiaoqu)  # 填入默认校区
        self.log_data_Text = Text(self.init_window_name, width=66, height=9,
                                  relief=RIDGE)  # , state=DISABLED, bd=1)  # 日志框
        self.log_data_Text.grid(row=13, column=0, columnspan=10)
        # 按钮
        self.str_save_button = Button(self.init_window_name, text="保存", bg="lightblue", width=10,
                                      command=self.filewrite)  # 保存基本信息
        self.str_save_button.grid(row=0, column=3)
        self.str_meirijiankang_button = Button(self.init_window_name, text="每日健康", bg="lightblue", width=10,
                                               command=self.meirijiankang)  # 填报每日健康
        self.str_meirijiankang_button.grid(row=4, column=0)
        self.str_tiwentianbao_button = Button(self.init_window_name, text="体温填报", bg="lightblue", width=10,
                                              command=self.tiwentianbao)  # 填报体温信息
        self.str_tiwentianbao_button.grid(row=4, column=1)
        self.str_jihe_button = Button(self.init_window_name, text="每日健康+体温填报", bg="lightblue", width=20,
                                      command=self.jihe)  # 填报每日健康+体温信息
        self.str_jihe_button.grid(row=5, column=0, columnspan=2)

    # 功能函数
    def fileread(self):

        with open(os.path.join(os.path.dirname(sys.argv[0]), 'data.txt'), mode='r+', encoding='utf-8') as f:  # 设置文件对象
            data = f.read().split(",")
            phone = data[0]  # 将txt文件的所有内容读入到字符串str中
            xiaoqu = data[1]
        return phone, xiaoqu

    def filewrite(self):
        f = open(os.path.join(os.path.dirname(sys.argv[0]), 'data.txt'), "w")  # 设置文件对象
        f.write(self.init_phone_Text.get("0.0", END).strip() + "," + self.init_xiaoqu_Text.get("0.0",
                                                                                               END).strip())  # 将字符串写入文件中
        f.close()

    def meirijiankang(self):
        # p = os.system("python3 F_ck_SMU.py")
        p = F_ck_SMU.meiri(self.init_phone_Text.get("0.0", END).strip(), self.init_xiaoqu_Text.get("0.0", END).strip())
        self.write_log_to_Text(str(p))

    # 体温填报
    def tiwentianbao(self):
        # w = os.system("python3 SMU_tiwen.py")
        w = F_ck_SMU.tiwen(self.init_phone_Text.get("0.0", END).strip())
        self.write_log_to_Text(str(w))

    # 每日健康+体温填报
    def jihe(self):
        # 创建两个子线程
        first_thread = threading.Thread(target=self.meirijiankang)
        second_thread = threading.Thread(target=self.tiwentianbao)

        # 启动线程执行对应的任务
        second_thread.start()
        first_thread.start()

    # 获取当前时间
    def get_current_time(self):
        current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        return current_time

    # 日志动态打印
    def write_log_to_Text(self, logmsg):
        global LOG_LINE_NUM
        current_time = self.get_current_time()
        logmsg_in = str(current_time) + " " + str(logmsg) + "\n"  # 换行
        if LOG_LINE_NUM <= 7:
            self.log_data_Text.insert(END, logmsg_in)
            LOG_LINE_NUM = LOG_LINE_NUM + 1
        else:
            self.log_data_Text.delete(1.0, 2.0)
            self.log_data_Text.insert(END, logmsg_in)


def gui_start():
    init_window = Tk()  # 实例化出一个父窗口
    ZMJ_PORTAL = MY_GUI(init_window)
    # 设置根窗口默认属性
    ZMJ_PORTAL.set_init_window()

    init_window.mainloop()  # 父窗口进入事件循环，可以理解为保持窗口运行，否则界面不展示


gui_start()
