# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_main_windows.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(554, 896)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        MainWindow.setFont(font)
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.centralwidget.setPalette(palette)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_start = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_start.setGeometry(QtCore.QRect(210, 670, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_start.setFont(font)
        self.pushButton_start.setStyleSheet("QPushButton{\n"
"background-color: rgb(217, 38, 38);\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255);}\n"
"QPushButton:pressed{\n"
"background-color: rgb(173, 31, 31);\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255);}")
        self.pushButton_start.setCheckable(False)
        self.pushButton_start.setAutoExclusive(False)
        self.pushButton_start.setObjectName("pushButton_start")
        self.textEdit_result_message = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_result_message.setGeometry(QtCore.QRect(30, 720, 491, 131))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.textEdit_result_message.setFont(font)
        self.textEdit_result_message.setObjectName("textEdit_result_message")
        self.checkBox_save_account = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_save_account.setGeometry(QtCore.QRect(50, 250, 421, 23))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.checkBox_save_account.setFont(font)
        self.checkBox_save_account.setObjectName("checkBox_save_account")
        self.widget_account = QtWidgets.QWidget(self.centralwidget)
        self.widget_account.setGeometry(QtCore.QRect(20, 100, 501, 81))
        self.widget_account.setObjectName("widget_account")
        self.lineEdit_account = QtWidgets.QLineEdit(self.widget_account)
        self.lineEdit_account.setGeometry(QtCore.QRect(30, 30, 441, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.lineEdit_account.setFont(font)
        self.lineEdit_account.setStyleSheet("background-color: rgb(214, 214, 214);\n"
"border-radius: 5px;\n"
"padding: 10px;")
        self.lineEdit_account.setObjectName("lineEdit_account")
        self.label_account = QtWidgets.QLabel(self.widget_account)
        self.label_account.setGeometry(QtCore.QRect(30, 5, 90, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_account.setFont(font)
        self.label_account.setObjectName("label_account")
        self.widget_password = QtWidgets.QWidget(self.centralwidget)
        self.widget_password.setGeometry(QtCore.QRect(20, 170, 501, 80))
        self.widget_password.setObjectName("widget_password")
        self.lineEdit_password = QtWidgets.QLineEdit(self.widget_password)
        self.lineEdit_password.setGeometry(QtCore.QRect(30, 30, 441, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.lineEdit_password.setFont(font)
        self.lineEdit_password.setStyleSheet("background-color: rgb(214, 214, 214);\n"
"border-radius: 5px;\n"
"padding: 10px;")
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.label_password = QtWidgets.QLabel(self.widget_password)
        self.label_password.setGeometry(QtCore.QRect(30, 5, 90, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_password.setFont(font)
        self.label_password.setObjectName("label_password")
        self.pushButton_hidden_password = QtWidgets.QPushButton(self.widget_password)
        self.pushButton_hidden_password.setGeometry(QtCore.QRect(430, 40, 21, 21))
        self.pushButton_hidden_password.setStyleSheet("QPushButton{\n"
"border-image: url(:/img/images/hidden-pw.png);\n"
"}\n"
"QPushButton:checked{\n"
"border-image: url(:/img/images/show-pw.png);\n"
"}")
        self.pushButton_hidden_password.setText("")
        self.pushButton_hidden_password.setCheckable(True)
        self.pushButton_hidden_password.setChecked(False)
        self.pushButton_hidden_password.setAutoDefault(False)
        self.pushButton_hidden_password.setObjectName("pushButton_hidden_password")
        self.widget_detail = QtWidgets.QWidget(self.centralwidget)
        self.widget_detail.setGeometry(QtCore.QRect(0, 300, 551, 361))
        self.widget_detail.setObjectName("widget_detail")
        self.widget_date = QtWidgets.QWidget(self.widget_detail)
        self.widget_date.setGeometry(QtCore.QRect(20, 60, 501, 61))
        self.widget_date.setObjectName("widget_date")
        self.label_date_time_title = QtWidgets.QLabel(self.widget_date)
        self.label_date_time_title.setGeometry(QtCore.QRect(30, 20, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_date_time_title.setFont(font)
        self.label_date_time_title.setObjectName("label_date_time_title")
        self.dateTimeEdit_start = QtWidgets.QDateTimeEdit(self.widget_date)
        self.dateTimeEdit_start.setGeometry(QtCore.QRect(100, 10, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.dateTimeEdit_start.setFont(font)
        self.dateTimeEdit_start.setProperty("showGroupSeparator", False)
        self.dateTimeEdit_start.setCalendarPopup(True)
        self.dateTimeEdit_start.setObjectName("dateTimeEdit_start")
        self.dateTimeEdit_end = QtWidgets.QDateTimeEdit(self.widget_date)
        self.dateTimeEdit_end.setGeometry(QtCore.QRect(305, 10, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.dateTimeEdit_end.setFont(font)
        self.dateTimeEdit_end.setProperty("showGroupSeparator", False)
        self.dateTimeEdit_end.setCalendarPopup(True)
        self.dateTimeEdit_end.setObjectName("dateTimeEdit_end")
        self.label_to = QtWidgets.QLabel(self.widget_date)
        self.label_to.setGeometry(QtCore.QRect(280, 20, 21, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_to.setFont(font)
        self.label_to.setObjectName("label_to")
        self.widget_project = QtWidgets.QWidget(self.widget_detail)
        self.widget_project.setGeometry(QtCore.QRect(20, 120, 501, 61))
        self.widget_project.setObjectName("widget_project")
        self.label_project_title = QtWidgets.QLabel(self.widget_project)
        self.label_project_title.setGeometry(QtCore.QRect(30, 20, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_project_title.setFont(font)
        self.label_project_title.setObjectName("label_project_title")
        self.lineEdit_project = QtWidgets.QLineEdit(self.widget_project)
        self.lineEdit_project.setGeometry(QtCore.QRect(100, 10, 371, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.lineEdit_project.setFont(font)
        self.lineEdit_project.setStyleSheet("background-color: rgb(214, 214, 214);\n"
"border-radius: 5px;\n"
"padding: 10px;")
        self.lineEdit_project.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_project.setObjectName("lineEdit_project")
        self.widget_test_plan = QtWidgets.QWidget(self.widget_detail)
        self.widget_test_plan.setGeometry(QtCore.QRect(20, 180, 501, 61))
        self.widget_test_plan.setObjectName("widget_test_plan")
        self.label_test_plan_title = QtWidgets.QLabel(self.widget_test_plan)
        self.label_test_plan_title.setGeometry(QtCore.QRect(30, 20, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_test_plan_title.setFont(font)
        self.label_test_plan_title.setObjectName("label_test_plan_title")
        self.lineEdit_test_plan = QtWidgets.QLineEdit(self.widget_test_plan)
        self.lineEdit_test_plan.setGeometry(QtCore.QRect(100, 10, 371, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.lineEdit_test_plan.setFont(font)
        self.lineEdit_test_plan.setStyleSheet("background-color: rgb(214, 214, 214);\n"
"border-radius: 5px;\n"
"padding: 10px;")
        self.lineEdit_test_plan.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_test_plan.setObjectName("lineEdit_test_plan")
        self.widget_start_date_time = QtWidgets.QWidget(self.widget_detail)
        self.widget_start_date_time.setGeometry(QtCore.QRect(20, 240, 501, 61))
        self.widget_start_date_time.setObjectName("widget_start_date_time")
        self.label_start_date_time_title = QtWidgets.QLabel(self.widget_start_date_time)
        self.label_start_date_time_title.setGeometry(QtCore.QRect(30, 20, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_start_date_time_title.setFont(font)
        self.label_start_date_time_title.setObjectName("label_start_date_time_title")
        self.dateTimeEdit_start_date_time = QtWidgets.QDateTimeEdit(self.widget_start_date_time)
        self.dateTimeEdit_start_date_time.setGeometry(QtCore.QRect(140, 10, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.dateTimeEdit_start_date_time.setFont(font)
        self.dateTimeEdit_start_date_time.setProperty("showGroupSeparator", False)
        self.dateTimeEdit_start_date_time.setCalendarPopup(True)
        self.dateTimeEdit_start_date_time.setObjectName("dateTimeEdit_start_date_time")
        self.widget_chamber_no = QtWidgets.QWidget(self.widget_detail)
        self.widget_chamber_no.setGeometry(QtCore.QRect(20, 0, 501, 61))
        self.widget_chamber_no.setObjectName("widget_chamber_no")
        self.label_chamber_no_title = QtWidgets.QLabel(self.widget_chamber_no)
        self.label_chamber_no_title.setGeometry(QtCore.QRect(30, 20, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_chamber_no_title.setFont(font)
        self.label_chamber_no_title.setObjectName("label_chamber_no_title")
        self.lineEdit_chamber_no = QtWidgets.QLineEdit(self.widget_chamber_no)
        self.lineEdit_chamber_no.setGeometry(QtCore.QRect(130, 10, 341, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.lineEdit_chamber_no.setFont(font)
        self.lineEdit_chamber_no.setStyleSheet("background-color: rgb(214, 214, 214);\n"
"border-radius: 5px;\n"
"padding: 10px;")
        self.lineEdit_chamber_no.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_chamber_no.setObjectName("lineEdit_chamber_no")
        self.widget_retry_times = QtWidgets.QWidget(self.widget_detail)
        self.widget_retry_times.setGeometry(QtCore.QRect(20, 300, 501, 61))
        self.widget_retry_times.setObjectName("widget_retry_times")
        self.label_retry_times_title = QtWidgets.QLabel(self.widget_retry_times)
        self.label_retry_times_title.setGeometry(QtCore.QRect(30, 20, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_retry_times_title.setFont(font)
        self.label_retry_times_title.setObjectName("label_retry_times_title")
        self.lineEdit_retry_times = QtWidgets.QLineEdit(self.widget_retry_times)
        self.lineEdit_retry_times.setGeometry(QtCore.QRect(120, 10, 351, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.lineEdit_retry_times.setFont(font)
        self.lineEdit_retry_times.setStyleSheet("background-color: rgb(214, 214, 214);\n"
"border-radius: 5px;\n"
"padding: 10px;")
        self.lineEdit_retry_times.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_retry_times.setObjectName("lineEdit_retry_times")
        self.widget_version = QtWidgets.QWidget(self.centralwidget)
        self.widget_version.setGeometry(QtCore.QRect(350, 0, 201, 31))
        self.widget_version.setStyleSheet("color: rgb(136, 138, 133);")
        self.widget_version.setObjectName("widget_version")
        self.label_version = QtWidgets.QLabel(self.widget_version)
        self.label_version.setGeometry(QtCore.QRect(30, 10, 161, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_version.setFont(font)
        self.label_version.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_version.setObjectName("label_version")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 10, 151, 91))
        self.label.setStyleSheet("image: url(:/img/images/msi-logo.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 554, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MSI Automatic Reserve"))
        self.pushButton_start.setText(_translate("MainWindow", "Start"))
        self.checkBox_save_account.setText(_translate("MainWindow", "Save account and password"))
        self.lineEdit_account.setPlaceholderText(_translate("MainWindow", "account"))
        self.label_account.setText(_translate("MainWindow", "Account"))
        self.lineEdit_password.setPlaceholderText(_translate("MainWindow", "password"))
        self.label_password.setText(_translate("MainWindow", "Password"))
        self.label_date_time_title.setText(_translate("MainWindow", "Date time : "))
        self.label_to.setText(_translate("MainWindow", "~"))
        self.label_project_title.setText(_translate("MainWindow", "Project : "))
        self.lineEdit_project.setPlaceholderText(_translate("MainWindow", "project"))
        self.label_test_plan_title.setText(_translate("MainWindow", "Test plan: "))
        self.lineEdit_test_plan.setPlaceholderText(_translate("MainWindow", "test plan"))
        self.label_start_date_time_title.setText(_translate("MainWindow", "Start date time: "))
        self.label_chamber_no_title.setText(_translate("MainWindow", "Chamber No."))
        self.lineEdit_chamber_no.setPlaceholderText(_translate("MainWindow", "chamber no."))
        self.label_retry_times_title.setText(_translate("MainWindow", "Retyr times: "))
        self.lineEdit_retry_times.setPlaceholderText(_translate("MainWindow", "retry times"))
        self.label_version.setText(_translate("MainWindow", "Version: 0.0.0.0"))
# import img_rc