# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window_qt.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtWidgets


class Ui_SMUreport(object):
    def setupUi(self, SMUreport):
        SMUreport.setObjectName("SMUreport")
        SMUreport.resize(419, 384)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SMUreport.sizePolicy().hasHeightForWidth())
        SMUreport.setSizePolicy(sizePolicy)
        SMUreport.setMinimumSize(QtCore.QSize(419, 384))
        self.centralwidget = QtWidgets.QWidget(SMUreport)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 1, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem2, 0, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem3, 4, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem4, 6, 1, 1, 1)
        self.btn_jiankang = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_jiankang.sizePolicy().hasHeightForWidth())
        self.btn_jiankang.setSizePolicy(sizePolicy)
        self.btn_jiankang.setObjectName("btn_jiankang")
        self.gridLayout_2.addWidget(self.btn_jiankang, 1, 1, 1, 1)
        self.btn_tiwen = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_tiwen.sizePolicy().hasHeightForWidth())
        self.btn_tiwen.setSizePolicy(sizePolicy)
        self.btn_tiwen.setObjectName("btn_tiwen")
        self.gridLayout_2.addWidget(self.btn_tiwen, 2, 1, 1, 1)
        self.btn_all = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_all.sizePolicy().hasHeightForWidth())
        self.btn_all.setSizePolicy(sizePolicy)
        self.btn_all.setObjectName("btn_all")
        self.gridLayout_2.addWidget(self.btn_all, 3, 1, 1, 1)
        self.name_lable = QtWidgets.QLabel(self.centralwidget)
        self.name_lable.setObjectName("name_lable")
        self.gridLayout_2.addWidget(self.name_lable, 5, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 1, 1, 1, 1)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem5, 4, 0, 1, 1)
        self.label_phone = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_phone.sizePolicy().hasHeightForWidth())
        self.label_phone.setSizePolicy(sizePolicy)
        self.label_phone.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_phone.setObjectName("label_phone")
        self.gridLayout.addWidget(self.label_phone, 0, 0, 1, 1)
        self.text_phone = QtWidgets.QLineEdit(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.text_phone.sizePolicy().hasHeightForWidth())
        self.text_phone.setSizePolicy(sizePolicy)
        self.text_phone.setInputMethodHints(QtCore.Qt.ImhNone)
        self.text_phone.setText("")
        self.text_phone.setMaxLength(11)
        self.text_phone.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.text_phone.setObjectName("text_phone")
        self.gridLayout.addWidget(self.text_phone, 0, 1, 1, 1)
        self.select_xiaoqu = QtWidgets.QComboBox(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.select_xiaoqu.sizePolicy().hasHeightForWidth())
        self.select_xiaoqu.setSizePolicy(sizePolicy)
        self.select_xiaoqu.setObjectName("select_xiaoqu")
        self.select_xiaoqu.addItem("")
        self.select_xiaoqu.addItem("")
        self.gridLayout.addWidget(self.select_xiaoqu, 1, 1, 1, 1)
        self.label_xiaoqu = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_xiaoqu.sizePolicy().hasHeightForWidth())
        self.label_xiaoqu.setSizePolicy(sizePolicy)
        self.label_xiaoqu.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_xiaoqu.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_xiaoqu.setObjectName("label_xiaoqu")
        self.gridLayout.addWidget(self.label_xiaoqu, 1, 0, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem6, 2, 1, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem7, 2, 0, 1, 1)
        self.jietu_box = QtWidgets.QGroupBox(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.jietu_box.sizePolicy().hasHeightForWidth())
        self.jietu_box.setSizePolicy(sizePolicy)
        self.jietu_box.setObjectName("jietu_box")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.jietu_box)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem8)
        self.jietu_yes = QtWidgets.QRadioButton(self.jietu_box)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.jietu_yes.sizePolicy().hasHeightForWidth())
        self.jietu_yes.setSizePolicy(sizePolicy)
        self.jietu_yes.setChecked(True)
        self.jietu_yes.setObjectName("jietu_yes")
        self.jietu_btngroup = QtWidgets.QButtonGroup(SMUreport)
        self.jietu_btngroup.setObjectName("jietu_btngroup")
        self.jietu_btngroup.addButton(self.jietu_yes)
        self.horizontalLayout.addWidget(self.jietu_yes)
        spacerItem9 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem9)
        self.jietu_no = QtWidgets.QRadioButton(self.jietu_box)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.jietu_no.sizePolicy().hasHeightForWidth())
        self.jietu_no.setSizePolicy(sizePolicy)
        self.jietu_no.setChecked(False)
        self.jietu_no.setObjectName("jietu_no")
        self.jietu_btngroup.addButton(self.jietu_no)
        self.horizontalLayout.addWidget(self.jietu_no)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem10)
        self.gridLayout.addWidget(self.jietu_box, 3, 0, 1, 2)
        self.gridLayout_3.addWidget(self.frame, 1, 0, 1, 1)
        self.text_log = QtWidgets.QTextBrowser(self.centralwidget)
        self.text_log.setInputMethodHints(QtCore.Qt.ImhNone)
        self.text_log.setReadOnly(False)
        self.text_log.setObjectName("text_log")
        self.gridLayout_3.addWidget(self.text_log, 2, 0, 1, 2)
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.title = QtWidgets.QLabel(self.splitter)
        self.title.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title.sizePolicy().hasHeightForWidth())
        self.title.setSizePolicy(sizePolicy)
        self.title.setTextFormat(QtCore.Qt.AutoText)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setWordWrap(False)
        self.title.setIndent(2)
        self.title.setObjectName("title")
        self.gridLayout_3.addWidget(self.splitter, 0, 0, 1, 2)
        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        SMUreport.setCentralWidget(self.centralwidget)

        self.retranslateUi(SMUreport)
        QtCore.QMetaObject.connectSlotsByName(SMUreport)

    def retranslateUi(self, SMUreport):
        _translate = QtCore.QCoreApplication.translate
        SMUreport.setWindowTitle(_translate("SMUreport", "SMU 填报工具"))
        self.btn_jiankang.setText(_translate("SMUreport", "每日健康"))
        self.btn_tiwen.setText(_translate("SMUreport", "体温填报"))
        self.btn_all.setText(_translate("SMUreport", "健康+体温"))
        self.name_lable.setText(_translate("SMUreport", "姓名："))
        self.label_phone.setText(_translate("SMUreport", "手机号码："))
        self.select_xiaoqu.setItemText(0, _translate("SMUreport", "本部校区"))
        self.select_xiaoqu.setItemText(1, _translate("SMUreport", "顺德校区"))
        self.label_xiaoqu.setText(_translate("SMUreport", "校区： "))
        self.jietu_box.setTitle(_translate("SMUreport", "是否生成体温截图"))
        self.jietu_yes.setText(_translate("SMUreport", "是"))
        self.jietu_no.setText(_translate("SMUreport", "否"))
        self.text_log.setHtml(_translate("SMUreport", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600;\">南方医科大学计算机协会</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">欢迎加入Q群：175446908</span></p></body></html>"))
        self.title.setText(_translate("SMUreport", "<html><head/><body><p align=\"center\"><span style=\" font-size:48pt; font-weight:600;\">SMU疫情填报系统</span></p></body></html>"))
