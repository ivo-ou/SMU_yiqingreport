from F_ck_SMU import meiri,tiwen,get_name
import window_qt
from sys import exit, argv
from PyQt5.QtWidgets import QApplication, QMainWindow


class mywindow(QMainWindow, window_qt.Ui_SMUreport):
    def __init__(self):
        super(mywindow, self).__init__()
        self.setupUi(self)
        self.btn_jiankang.clicked.connect(self.meiri)
        self.btn_tiwen.clicked.connect(self.tiwen)
        self.btn_all.clicked.connect(self.jihe)
        self.text_phone.textChanged.connect(self.getname)
    def meiri(self):
        meiri(self,self.text_phone.text(),self.select_xiaoqu.currentText())
        print("每日健康填报")
    def tiwen(self):
        tiwen(self,self.text_phone.text())
        print("体温填报")
    def jihe(self):
        meiri(self, self.text_phone.text(), self.select_xiaoqu.currentText())
        tiwen(self, self.text_phone.text())
    def getname(self):
        if(len(self.text_phone.text())>10):
            get_name(self,self.text_phone.text())
        else:
            self.name_lable.setText("姓名：")





if __name__ == '__main__':
  app = QApplication(argv)
  MainWindow = mywindow()
  MainWindow.show()
  exit(app.exec_())