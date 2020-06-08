import requests
import json
#import datetime

###############################


params={
    "phone" : ""         #手机号码
}


###############################



mydata = {                                   #填报数据
    "xiaoqu": "本部校区",                     # 校区


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
r=sess.get(portal_url,params=params)                                                #登陆

Tb_url = "http://tougao.gdaw.net/Home2020/NanFangYiKe/baomingInsert5.html"
r = sess.post(Tb_url,data=mydata)                                                   #表单提交

if r.text == 1:
    print("填报成功")
elif r.text == 2:
    print("此手机号码主人，已经报名成功了，不能重复报名")
elif r.text ==3:
    print("请填写完整表单")
else:
    print('数据保存失败（垃圾设计，理论上成功了，但是不会提醒已经报名成功，可以去每日修改看看')
