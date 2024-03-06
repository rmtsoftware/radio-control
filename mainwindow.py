# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QStatusBar, QTextBrowser, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(477, 622)
        MainWindow.setStyleSheet(u"background-color: rgb(214, 214, 214);\n"
"color: black;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 320, 461, 271))
        self.verticalLayout_8 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.layoutWidget)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_8.addWidget(self.label_7)

        self.terminal_window = QTextBrowser(self.layoutWidget)
        self.terminal_window.setObjectName(u"terminal_window")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setKerning(True)
        self.terminal_window.setFont(font)
        self.terminal_window.setStyleSheet(u"background-color: white;")

        self.verticalLayout_8.addWidget(self.terminal_window)

        self.layoutWidget_2 = QWidget(self.centralwidget)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(20, 250, 142, 49))
        self.verticalLayout_5 = QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.lb_set_power = QLabel(self.layoutWidget_2)
        self.lb_set_power.setObjectName(u"lb_set_power")

        self.verticalLayout_5.addWidget(self.lb_set_power)

        self.le_pwr_mnl = QLineEdit(self.layoutWidget_2)
        self.le_pwr_mnl.setObjectName(u"le_pwr_mnl")
        self.le_pwr_mnl.setMinimumSize(QSize(0, 25))
        self.le_pwr_mnl.setMaximumSize(QSize(16777215, 16777215))
        self.le_pwr_mnl.setStyleSheet(u"background-color: white;")

        self.verticalLayout_5.addWidget(self.le_pwr_mnl)

        self.layoutWidget_3 = QWidget(self.centralwidget)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(20, 160, 141, 80))
        self.verticalLayout_4 = QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.lb_mtr_ctrl = QLabel(self.layoutWidget_3)
        self.lb_mtr_ctrl.setObjectName(u"lb_mtr_ctrl")

        self.verticalLayout_4.addWidget(self.lb_mtr_ctrl)

        self.btn_motor_start = QPushButton(self.layoutWidget_3)
        self.btn_motor_start.setObjectName(u"btn_motor_start")
        self.btn_motor_start.setMinimumSize(QSize(0, 25))
        self.btn_motor_start.setStyleSheet(u"")

        self.verticalLayout_4.addWidget(self.btn_motor_start)

        self.btn_motor_stop = QPushButton(self.layoutWidget_3)
        self.btn_motor_stop.setObjectName(u"btn_motor_stop")
        self.btn_motor_stop.setMinimumSize(QSize(0, 25))
        self.btn_motor_stop.setStyleSheet(u"")

        self.verticalLayout_4.addWidget(self.btn_motor_stop)

        self.layoutWidget_4 = QWidget(self.centralwidget)
        self.layoutWidget_4.setObjectName(u"layoutWidget_4")
        self.layoutWidget_4.setGeometry(QRect(20, 20, 141, 130))
        self.verticalLayout = QVBoxLayout(self.layoutWidget_4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.lb_connection_2 = QLabel(self.layoutWidget_4)
        self.lb_connection_2.setObjectName(u"lb_connection_2")

        self.verticalLayout.addWidget(self.lb_connection_2)

        self.btn_gps = QPushButton(self.layoutWidget_4)
        self.btn_gps.setObjectName(u"btn_gps")

        self.verticalLayout.addWidget(self.btn_gps)

        self.btn_imu = QPushButton(self.layoutWidget_4)
        self.btn_imu.setObjectName(u"btn_imu")

        self.verticalLayout.addWidget(self.btn_imu)

        self.cb_auto_gps = QCheckBox(self.layoutWidget_4)
        self.cb_auto_gps.setObjectName(u"cb_auto_gps")

        self.verticalLayout.addWidget(self.cb_auto_gps)

        self.cb_auto_imu = QCheckBox(self.layoutWidget_4)
        self.cb_auto_imu.setObjectName(u"cb_auto_imu")

        self.verticalLayout.addWidget(self.cb_auto_imu)

        self.layoutWidget_5 = QWidget(self.centralwidget)
        self.layoutWidget_5.setObjectName(u"layoutWidget_5")
        self.layoutWidget_5.setGeometry(QRect(180, 140, 141, 80))
        self.verticalLayout_7 = QVBoxLayout(self.layoutWidget_5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.lb_man_cmd = QLabel(self.layoutWidget_5)
        self.lb_man_cmd.setObjectName(u"lb_man_cmd")

        self.verticalLayout_7.addWidget(self.lb_man_cmd)

        self.le_mnl_cmd = QLineEdit(self.layoutWidget_5)
        self.le_mnl_cmd.setObjectName(u"le_mnl_cmd")
        self.le_mnl_cmd.setMinimumSize(QSize(0, 25))
        self.le_mnl_cmd.setMaximumSize(QSize(16777215, 16777215))
        self.le_mnl_cmd.setStyleSheet(u"background-color: white;")

        self.verticalLayout_7.addWidget(self.le_mnl_cmd)

        self.btn_mnl_cmd = QPushButton(self.layoutWidget_5)
        self.btn_mnl_cmd.setObjectName(u"btn_mnl_cmd")
        self.btn_mnl_cmd.setMinimumSize(QSize(0, 25))
        self.btn_mnl_cmd.setStyleSheet(u"")

        self.verticalLayout_7.addWidget(self.btn_mnl_cmd)

        self.layoutWidget_6 = QWidget(self.centralwidget)
        self.layoutWidget_6.setObjectName(u"layoutWidget_6")
        self.layoutWidget_6.setGeometry(QRect(180, 20, 141, 111))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget_6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.layoutWidget_6)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_3.addWidget(self.label_8)

        self.btn_mnl_mode = QPushButton(self.layoutWidget_6)
        self.btn_mnl_mode.setObjectName(u"btn_mnl_mode")
        self.btn_mnl_mode.setMinimumSize(QSize(0, 25))
        self.btn_mnl_mode.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.btn_mnl_mode)

        self.btn_rmt_mode = QPushButton(self.layoutWidget_6)
        self.btn_rmt_mode.setObjectName(u"btn_rmt_mode")
        self.btn_rmt_mode.setMinimumSize(QSize(0, 25))
        self.btn_rmt_mode.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.btn_rmt_mode)

        self.btn_auto_mode = QPushButton(self.layoutWidget_6)
        self.btn_auto_mode.setObjectName(u"btn_auto_mode")
        self.btn_auto_mode.setMinimumSize(QSize(0, 25))
        self.btn_auto_mode.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.btn_auto_mode)

        self.layoutWidget_7 = QWidget(self.centralwidget)
        self.layoutWidget_7.setObjectName(u"layoutWidget_7")
        self.layoutWidget_7.setGeometry(QRect(340, 20, 131, 184))
        self.verticalLayout_12 = QVBoxLayout(self.layoutWidget_7)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.lb_name_map_4 = QLabel(self.layoutWidget_7)
        self.lb_name_map_4.setObjectName(u"lb_name_map_4")
        self.lb_name_map_4.setMaximumSize(QSize(101, 16))
        self.lb_name_map_4.setStyleSheet(u"border: None;")

        self.verticalLayout_12.addWidget(self.lb_name_map_4)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.lb_latitude_2 = QLabel(self.layoutWidget_7)
        self.lb_latitude_2.setObjectName(u"lb_latitude_2")
        self.lb_latitude_2.setMinimumSize(QSize(58, 0))
        self.lb_latitude_2.setMaximumSize(QSize(58, 16777215))

        self.horizontalLayout_12.addWidget(self.lb_latitude_2)

        self.lb_latitude_val_2 = QLabel(self.layoutWidget_7)
        self.lb_latitude_val_2.setObjectName(u"lb_latitude_val_2")

        self.horizontalLayout_12.addWidget(self.lb_latitude_val_2)


        self.verticalLayout_12.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.lb_NS_2 = QLabel(self.layoutWidget_7)
        self.lb_NS_2.setObjectName(u"lb_NS_2")
        self.lb_NS_2.setMinimumSize(QSize(58, 0))
        self.lb_NS_2.setMaximumSize(QSize(58, 16777215))

        self.horizontalLayout_13.addWidget(self.lb_NS_2)

        self.lb_NS_val_2 = QLabel(self.layoutWidget_7)
        self.lb_NS_val_2.setObjectName(u"lb_NS_val_2")

        self.horizontalLayout_13.addWidget(self.lb_NS_val_2)


        self.verticalLayout_12.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.lb_longitude_2 = QLabel(self.layoutWidget_7)
        self.lb_longitude_2.setObjectName(u"lb_longitude_2")
        self.lb_longitude_2.setMinimumSize(QSize(58, 0))
        self.lb_longitude_2.setMaximumSize(QSize(58, 16777215))

        self.horizontalLayout_14.addWidget(self.lb_longitude_2)

        self.lb_longitude_val_2 = QLabel(self.layoutWidget_7)
        self.lb_longitude_val_2.setObjectName(u"lb_longitude_val_2")

        self.horizontalLayout_14.addWidget(self.lb_longitude_val_2)


        self.verticalLayout_12.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.lb_EW_2 = QLabel(self.layoutWidget_7)
        self.lb_EW_2.setObjectName(u"lb_EW_2")
        self.lb_EW_2.setMinimumSize(QSize(58, 0))
        self.lb_EW_2.setMaximumSize(QSize(58, 16777215))

        self.horizontalLayout_15.addWidget(self.lb_EW_2)

        self.lb_EW_val_2 = QLabel(self.layoutWidget_7)
        self.lb_EW_val_2.setObjectName(u"lb_EW_val_2")

        self.horizontalLayout_15.addWidget(self.lb_EW_val_2)


        self.verticalLayout_12.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.lb_altitude_2 = QLabel(self.layoutWidget_7)
        self.lb_altitude_2.setObjectName(u"lb_altitude_2")
        self.lb_altitude_2.setMinimumSize(QSize(58, 0))
        self.lb_altitude_2.setMaximumSize(QSize(58, 16777215))

        self.horizontalLayout_16.addWidget(self.lb_altitude_2)

        self.lb_altitude_val_2 = QLabel(self.layoutWidget_7)
        self.lb_altitude_val_2.setObjectName(u"lb_altitude_val_2")

        self.horizontalLayout_16.addWidget(self.lb_altitude_val_2)


        self.verticalLayout_12.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.lb_grndspeed_2 = QLabel(self.layoutWidget_7)
        self.lb_grndspeed_2.setObjectName(u"lb_grndspeed_2")
        self.lb_grndspeed_2.setMinimumSize(QSize(58, 0))
        self.lb_grndspeed_2.setMaximumSize(QSize(58, 16777215))

        self.horizontalLayout_17.addWidget(self.lb_grndspeed_2)

        self.lb_grndspeed_val_2 = QLabel(self.layoutWidget_7)
        self.lb_grndspeed_val_2.setObjectName(u"lb_grndspeed_val_2")

        self.horizontalLayout_17.addWidget(self.lb_grndspeed_val_2)


        self.verticalLayout_12.addLayout(self.horizontalLayout_17)

        self.layoutWidget_8 = QWidget(self.centralwidget)
        self.layoutWidget_8.setObjectName(u"layoutWidget_8")
        self.layoutWidget_8.setGeometry(QRect(340, 220, 131, 90))
        self.verticalLayout_13 = QVBoxLayout(self.layoutWidget_8)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.lb_name_map_5 = QLabel(self.layoutWidget_8)
        self.lb_name_map_5.setObjectName(u"lb_name_map_5")
        self.lb_name_map_5.setMaximumSize(QSize(101, 16))
        self.lb_name_map_5.setStyleSheet(u"border: None;")

        self.verticalLayout_13.addWidget(self.lb_name_map_5)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.lb_axl_x_2 = QLabel(self.layoutWidget_8)
        self.lb_axl_x_2.setObjectName(u"lb_axl_x_2")
        self.lb_axl_x_2.setMinimumSize(QSize(58, 0))
        self.lb_axl_x_2.setMaximumSize(QSize(58, 16777215))

        self.horizontalLayout_18.addWidget(self.lb_axl_x_2)

        self.lb_axl_x_val_2 = QLabel(self.layoutWidget_8)
        self.lb_axl_x_val_2.setObjectName(u"lb_axl_x_val_2")
        self.lb_axl_x_val_2.setMinimumSize(QSize(0, 0))
        self.lb_axl_x_val_2.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_18.addWidget(self.lb_axl_x_val_2)


        self.verticalLayout_13.addLayout(self.horizontalLayout_18)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.lb_axl_y_2 = QLabel(self.layoutWidget_8)
        self.lb_axl_y_2.setObjectName(u"lb_axl_y_2")
        self.lb_axl_y_2.setMinimumSize(QSize(58, 0))
        self.lb_axl_y_2.setMaximumSize(QSize(58, 16777215))

        self.horizontalLayout_19.addWidget(self.lb_axl_y_2)

        self.lb_axl_y_val_2 = QLabel(self.layoutWidget_8)
        self.lb_axl_y_val_2.setObjectName(u"lb_axl_y_val_2")
        self.lb_axl_y_val_2.setMinimumSize(QSize(0, 0))
        self.lb_axl_y_val_2.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_19.addWidget(self.lb_axl_y_val_2)


        self.verticalLayout_13.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.lb_axl_z_2 = QLabel(self.layoutWidget_8)
        self.lb_axl_z_2.setObjectName(u"lb_axl_z_2")
        self.lb_axl_z_2.setMinimumSize(QSize(58, 0))
        self.lb_axl_z_2.setMaximumSize(QSize(58, 16777215))

        self.horizontalLayout_20.addWidget(self.lb_axl_z_2)

        self.lb_axl_z_val_2 = QLabel(self.layoutWidget_8)
        self.lb_axl_z_val_2.setObjectName(u"lb_axl_z_val_2")
        self.lb_axl_z_val_2.setMinimumSize(QSize(0, 0))
        self.lb_axl_z_val_2.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_20.addWidget(self.lb_axl_z_val_2)


        self.verticalLayout_13.addLayout(self.horizontalLayout_20)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u0440\u043c\u0438\u043d\u0430\u043b", None))
        self.lb_set_power.setText(QCoreApplication.translate("MainWindow", u"\u041c\u043e\u0449\u043d\u043e\u0441\u0442\u044c \u0414\u0412\u0421", None))
        self.le_pwr_mnl.setText("")
        self.lb_mtr_ctrl.setText(QCoreApplication.translate("MainWindow", u"\u0423\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u0414\u0412\u0421", None))
        self.btn_motor_start.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0440\u0442", None))
        self.btn_motor_stop.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u043e\u043f", None))
        self.lb_connection_2.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0440\u043e\u0441 \u0442\u0435\u043b\u0435\u043c\u0435\u0442\u0440\u0438\u0438", None))
        self.btn_gps.setText(QCoreApplication.translate("MainWindow", u"GPS", None))
        self.btn_imu.setText(QCoreApplication.translate("MainWindow", u"IMU", None))
        self.cb_auto_gps.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0432\u0442\u043e \u0437\u0430\u043f\u0440\u043e\u0441 GPS", None))
        self.cb_auto_imu.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0432\u0442\u043e \u0437\u0430\u043f\u0440\u043e\u0441 IMU", None))
        self.lb_man_cmd.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0443\u0447 \u043a\u043c\u043d\u0434", None))
        self.le_mnl_cmd.setText("")
        self.btn_mnl_cmd.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u043e\u0440 \u0440\u0435\u0436\u0438\u043c\u0430", None))
        self.btn_mnl_mode.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0443\u0447\u043d\u043e\u0439", None))
        self.btn_rmt_mode.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0438\u0441\u0442\u0430\u043d\u0446\u0438\u043e\u043d\u043d\u044b\u0439", None))
        self.btn_auto_mode.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0432\u0442\u043e\u043d\u043e\u043c\u043d\u044b\u0439", None))
        self.lb_name_map_4.setText(QCoreApplication.translate("MainWindow", u"GPS", None))
        self.lb_latitude_2.setText(QCoreApplication.translate("MainWindow", u"Latitide", None))
        self.lb_latitude_val_2.setText(QCoreApplication.translate("MainWindow", u"Latitide", None))
        self.lb_NS_2.setText(QCoreApplication.translate("MainWindow", u"NS", None))
        self.lb_NS_val_2.setText(QCoreApplication.translate("MainWindow", u"NS", None))
        self.lb_longitude_2.setText(QCoreApplication.translate("MainWindow", u"Longitude", None))
        self.lb_longitude_val_2.setText(QCoreApplication.translate("MainWindow", u"Longitude", None))
        self.lb_EW_2.setText(QCoreApplication.translate("MainWindow", u"EW", None))
        self.lb_EW_val_2.setText(QCoreApplication.translate("MainWindow", u"EW", None))
        self.lb_altitude_2.setText(QCoreApplication.translate("MainWindow", u"Altitude", None))
        self.lb_altitude_val_2.setText(QCoreApplication.translate("MainWindow", u"Altitude", None))
        self.lb_grndspeed_2.setText(QCoreApplication.translate("MainWindow", u"GrndSpeed", None))
        self.lb_grndspeed_val_2.setText(QCoreApplication.translate("MainWindow", u"GrndSpeed", None))
        self.lb_name_map_5.setText(QCoreApplication.translate("MainWindow", u"IMU", None))
        self.lb_axl_x_2.setText(QCoreApplication.translate("MainWindow", u"Pitch", None))
        self.lb_axl_x_val_2.setText(QCoreApplication.translate("MainWindow", u"AXL_x", None))
        self.lb_axl_y_2.setText(QCoreApplication.translate("MainWindow", u"Roll", None))
        self.lb_axl_y_val_2.setText(QCoreApplication.translate("MainWindow", u"AXL_y", None))
        self.lb_axl_z_2.setText(QCoreApplication.translate("MainWindow", u"Yaw", None))
        self.lb_axl_z_val_2.setText(QCoreApplication.translate("MainWindow", u"AXL_z", None))
    # retranslateUi

