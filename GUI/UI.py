# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_MainWindow1600x900_0225.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1600, 900)
        MainWindow.setMinimumSize(QtCore.QSize(0, 2))
        MainWindow.setMaximumSize(QtCore.QSize(1600, 900))
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(62, 62, 62, 255), stop:1 rgba(114, 114, 114, 255));")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMaximumSize(QtCore.QSize(1600, 1024))
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox_Plot = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_Plot.setGeometry(QtCore.QRect(10, 10, 1571, 851))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_Plot.sizePolicy().hasHeightForWidth())
        self.groupBox_Plot.setSizePolicy(sizePolicy)
        self.groupBox_Plot.setMaximumSize(QtCore.QSize(2880, 1800))
        self.groupBox_Plot.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(86, 170, 255, 125), stop:1 rgba(255, 255, 255, 50));\n"
"border-radius: 5px;\n"
"font: 20pt \"Avenir\";\n"
"")
        self.groupBox_Plot.setTitle("")
        self.groupBox_Plot.setObjectName("groupBox_Plot")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.groupBox_Plot)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 50, 931, 801))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(980, 10, 591, 471))
        self.tabWidget.setAutoFillBackground(True)
        self.tabWidget.setStyleSheet("font: 30pt \"Avenir\";")
        self.tabWidget.setObjectName("tabWidget")
        self.globalControlTab = QtWidgets.QWidget()
        self.globalControlTab.setObjectName("globalControlTab")
        self.groupBox_valveControl = QtWidgets.QGroupBox(self.globalControlTab)
        self.groupBox_valveControl.setGeometry(QtCore.QRect(0, 0, 601, 421))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_valveControl.sizePolicy().hasHeightForWidth())
        self.groupBox_valveControl.setSizePolicy(sizePolicy)
        self.groupBox_valveControl.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(85, 170, 255, 125), stop:1 rgba(255, 255, 255, 50));\n"
"border-radius: 5px;\n"
"")
        self.groupBox_valveControl.setTitle("")
        self.groupBox_valveControl.setObjectName("groupBox_valveControl")
        self.groupBox_MassFlowValve_2 = QtWidgets.QGroupBox(self.groupBox_valveControl)
        self.groupBox_MassFlowValve_2.setGeometry(QtCore.QRect(0, 210, 621, 211))
        self.groupBox_MassFlowValve_2.setObjectName("groupBox_MassFlowValve_2")
        self.spinBox_MassFlowValve_2 = QtWidgets.QSpinBox(self.groupBox_MassFlowValve_2)
        self.spinBox_MassFlowValve_2.setGeometry(QtCore.QRect(470, 70, 101, 81))
        self.spinBox_MassFlowValve_2.setStyleSheet("background-color: rgb(200,200,200);\n"
"border-radius: 1px;")
        self.spinBox_MassFlowValve_2.setMaximum(255)
        self.spinBox_MassFlowValve_2.setObjectName("spinBox_MassFlowValve_2")
        self.horizontalSlider_MassFlowValve_2 = QtWidgets.QSlider(self.groupBox_MassFlowValve_2)
        self.horizontalSlider_MassFlowValve_2.setGeometry(QtCore.QRect(10, 70, 441, 81))
        self.horizontalSlider_MassFlowValve_2.setStyleSheet("background-color: rgb(200,200,200);\n"
"border-radius: 10px;")
        self.horizontalSlider_MassFlowValve_2.setMaximum(255)
        self.horizontalSlider_MassFlowValve_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_MassFlowValve_2.setObjectName("horizontalSlider_MassFlowValve_2")
        self.groupBox_3WayValve_2 = QtWidgets.QGroupBox(self.groupBox_valveControl)
        self.groupBox_3WayValve_2.setGeometry(QtCore.QRect(0, 0, 621, 201))
        self.groupBox_3WayValve_2.setObjectName("groupBox_3WayValve_2")
        self.horizontalSlider_3WayValve_2 = QtWidgets.QSlider(self.groupBox_3WayValve_2)
        self.horizontalSlider_3WayValve_2.setGeometry(QtCore.QRect(10, 80, 441, 81))
        self.horizontalSlider_3WayValve_2.setStyleSheet("background-color: rgb(200,200,200);\n"
"border-radius: 10px;")
        self.horizontalSlider_3WayValve_2.setMaximum(255)
        self.horizontalSlider_3WayValve_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_3WayValve_2.setObjectName("horizontalSlider_3WayValve_2")
        self.spinBox_3WayValve_2 = QtWidgets.QSpinBox(self.groupBox_3WayValve_2)
        self.spinBox_3WayValve_2.setGeometry(QtCore.QRect(470, 80, 91, 81))
        self.spinBox_3WayValve_2.setStyleSheet("background-color: rgb(200,200,200);\n"
"border-radius: 1px;")
        self.spinBox_3WayValve_2.setMaximum(255)
        self.spinBox_3WayValve_2.setObjectName("spinBox_3WayValve_2")
        self.tabWidget.addTab(self.globalControlTab, "")
        self.automationTab = QtWidgets.QWidget()
        self.automationTab.setObjectName("automationTab")
        self.groupBox_Automation = QtWidgets.QGroupBox(self.automationTab)
        self.groupBox_Automation.setGeometry(QtCore.QRect(0, 0, 601, 431))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_Automation.sizePolicy().hasHeightForWidth())
        self.groupBox_Automation.setSizePolicy(sizePolicy)
        self.groupBox_Automation.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(85, 170, 255, 125), stop:1 rgba(255, 255, 255, 50));\n"
"border-radius: 5px;\n"
"font: 18pt \"Avenir\";\n"
"")
        self.groupBox_Automation.setTitle("")
        self.groupBox_Automation.setObjectName("groupBox_Automation")
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.groupBox_Automation)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(10, 20, 551, 261))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.tableWidget = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.tableWidget.setContentsMargins(0, 0, 0, 0)
        self.tableWidget.setObjectName("tableWidget")
        self.pushButton_StartAutomation = QtWidgets.QPushButton(self.groupBox_Automation)
        self.pushButton_StartAutomation.setGeometry(QtCore.QRect(10, 310, 171, 91))
        self.pushButton_StartAutomation.setStyleSheet("background-color:rgb(28, 255, 13);\n"
"border-radius: 10px;\n"
"font: 30pt \"Avenir\";")
        self.pushButton_StartAutomation.setObjectName("pushButton_StartAutomation")
        self.pushButton_StopAutomation = QtWidgets.QPushButton(self.groupBox_Automation)
        self.pushButton_StopAutomation.setGeometry(QtCore.QRect(220, 310, 161, 91))
        self.pushButton_StopAutomation.setStyleSheet("background-color: rgb(252, 52, 80);\n"
"border-radius: 10px;\n"
"font: 30pt \"Avenir\";")
        self.pushButton_StopAutomation.setObjectName("pushButton_StopAutomation")
        self.pushButton_OpenAutomationButton = QtWidgets.QPushButton(self.groupBox_Automation)
        self.pushButton_OpenAutomationButton.setGeometry(QtCore.QRect(402, 310, 161, 91))
        self.pushButton_OpenAutomationButton.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(200,200,200, 100), stop:1 rgba(255, 255, 255, 80));\n"
"border-radius: 10px;\n"
"font: 30pt \"Avenir\";")
        self.pushButton_OpenAutomationButton.setObjectName("pushButton_OpenAutomationButton")
        self.tabWidget.addTab(self.automationTab, "")
        self.mqttConnectiontab = QtWidgets.QWidget()
        self.mqttConnectiontab.setObjectName("mqttConnectiontab")
        self.groupBox_MQTT_Settings = QtWidgets.QGroupBox(self.mqttConnectiontab)
        self.groupBox_MQTT_Settings.setGeometry(QtCore.QRect(0, 0, 621, 441))
        self.groupBox_MQTT_Settings.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(85, 170, 255, 125), stop:1 rgba(255, 255, 255, 50));\n"
"border-radius: 5px;\n"
"font: 20pt \"Avenir\";\n"
"")
        self.groupBox_MQTT_Settings.setTitle("")
        self.groupBox_MQTT_Settings.setObjectName("groupBox_MQTT_Settings")
        self.lineEdit_MqttBroker = QtWidgets.QLineEdit(self.groupBox_MQTT_Settings)
        self.lineEdit_MqttBroker.setGeometry(QtCore.QRect(220, 20, 351, 51))
        self.lineEdit_MqttBroker.setStyleSheet("")
        self.lineEdit_MqttBroker.setObjectName("lineEdit_MqttBroker")
        self.lineEdit_Port = QtWidgets.QLineEdit(self.groupBox_MQTT_Settings)
        self.lineEdit_Port.setGeometry(QtCore.QRect(220, 90, 351, 51))
        self.lineEdit_Port.setObjectName("lineEdit_Port")
        self.lineEdit_Topic = QtWidgets.QLineEdit(self.groupBox_MQTT_Settings)
        self.lineEdit_Topic.setGeometry(QtCore.QRect(220, 160, 351, 51))
        self.lineEdit_Topic.setObjectName("lineEdit_Topic")
        self.label_MqttBroker = QtWidgets.QLabel(self.groupBox_MQTT_Settings)
        self.label_MqttBroker.setGeometry(QtCore.QRect(10, 20, 211, 51))
        self.label_MqttBroker.setObjectName("label_MqttBroker")
        self.label_Port = QtWidgets.QLabel(self.groupBox_MQTT_Settings)
        self.label_Port.setGeometry(QtCore.QRect(10, 90, 211, 51))
        self.label_Port.setObjectName("label_Port")
        self.label_Topic = QtWidgets.QLabel(self.groupBox_MQTT_Settings)
        self.label_Topic.setGeometry(QtCore.QRect(10, 160, 211, 51))
        self.label_Topic.setObjectName("label_Topic")
        self.pushButton_ConnectMQTT = QtWidgets.QPushButton(self.groupBox_MQTT_Settings)
        self.pushButton_ConnectMQTT.setGeometry(QtCore.QRect(10, 310, 261, 91))
        self.pushButton_ConnectMQTT.setStyleSheet("background-color:rgb(28, 255, 13);\n"
"font: 30pt \"Avenir\";\n"
"border-radius: 10px;")
        self.pushButton_ConnectMQTT.setObjectName("pushButton_ConnectMQTT")
        self.pushButton_DisconnectMQTT = QtWidgets.QPushButton(self.groupBox_MQTT_Settings)
        self.pushButton_DisconnectMQTT.setGeometry(QtCore.QRect(310, 310, 251, 91))
        self.pushButton_DisconnectMQTT.setStyleSheet("background-color: rgb(252, 52, 80);\n"
"font: 30pt \"Avenir\";\n"
"border-radius: 10px;")
        self.pushButton_DisconnectMQTT.setObjectName("pushButton_DisconnectMQTT")
        self.label_State = QtWidgets.QLabel(self.groupBox_MQTT_Settings)
        self.label_State.setGeometry(QtCore.QRect(10, 230, 211, 51))
        self.label_State.setObjectName("label_State")
        self.label_ConnectionState = QtWidgets.QLabel(self.groupBox_MQTT_Settings)
        self.label_ConnectionState.setGeometry(QtCore.QRect(220, 230, 351, 51))
        self.label_ConnectionState.setObjectName("label_ConnectionState")
        self.tabWidget.addTab(self.mqttConnectiontab, "")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(980, 490, 591, 361))
        self.groupBox.setMaximumSize(QtCore.QSize(1024, 600))
        self.groupBox.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(85, 170, 255, 125), stop:1 rgba(255, 255, 255, 50));\n"
"border-radius: 5px;\n"
"font: 30pt \"Avenir\";\n"
"")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.groupBox_CropPlot = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_CropPlot.setGeometry(QtCore.QRect(0, 180, 601, 181))
        self.groupBox_CropPlot.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBox_CropPlot.setObjectName("groupBox_CropPlot")
        self.spinBox_CropPlot = QtWidgets.QSpinBox(self.groupBox_CropPlot)
        self.spinBox_CropPlot.setGeometry(QtCore.QRect(310, 60, 71, 101))
        self.spinBox_CropPlot.setStyleSheet("background-color: rgba(200,200,200,125);\n"
"border-radius: 1px;")
        self.spinBox_CropPlot.setMinimum(10)
        self.spinBox_CropPlot.setObjectName("spinBox_CropPlot")
        self.horizontalSlider_CropPlot = QtWidgets.QSlider(self.groupBox_CropPlot)
        self.horizontalSlider_CropPlot.setGeometry(QtCore.QRect(10, 60, 281, 101))
        self.horizontalSlider_CropPlot.setStyleSheet("background-color: rgba(200,200,200,125);\n"
"border-radius: 10px;\n"
"")
        self.horizontalSlider_CropPlot.setMinimum(10)
        self.horizontalSlider_CropPlot.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_CropPlot.setObjectName("horizontalSlider_CropPlot")
        self.pushButton_CropPlot = QtWidgets.QPushButton(self.groupBox_CropPlot)
        self.pushButton_CropPlot.setGeometry(QtCore.QRect(400, 60, 171, 101))
        self.pushButton_CropPlot.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(200,200,200, 100), stop:1 rgba(255, 255, 255, 80));\n"
"border-radius: 10px;")
        self.pushButton_CropPlot.setObjectName("pushButton_CropPlot")
        self.groupBox_PlotSwitch = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_PlotSwitch.setGeometry(QtCore.QRect(0, 0, 601, 171))
        self.groupBox_PlotSwitch.setStyleSheet("")
        self.groupBox_PlotSwitch.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBox_PlotSwitch.setObjectName("groupBox_PlotSwitch")
        self.radioButton_PlotSwitchPower = QtWidgets.QRadioButton(self.groupBox_PlotSwitch)
        self.radioButton_PlotSwitchPower.setGeometry(QtCore.QRect(20, 50, 171, 101))
        self.radioButton_PlotSwitchPower.setStyleSheet("background-color: rgba(200,200,200,125);\n"
"border-radius: 10px;")
        self.radioButton_PlotSwitchPower.setChecked(True)
        self.radioButton_PlotSwitchPower.setObjectName("radioButton_PlotSwitchPower")
        self.radioButton_PlotSwitchTemperatur = QtWidgets.QRadioButton(self.groupBox_PlotSwitch)
        self.radioButton_PlotSwitchTemperatur.setGeometry(QtCore.QRect(220, 50, 161, 101))
        self.radioButton_PlotSwitchTemperatur.setStyleSheet("background-color: rgba(200,200,200,125);\n"
"border-radius: 10px;\n"
"")
        self.radioButton_PlotSwitchTemperatur.setObjectName("radioButton_PlotSwitchTemperatur")
        self.pushButton_SavePlotButton = QtWidgets.QPushButton(self.groupBox_PlotSwitch)
        self.pushButton_SavePlotButton.setGeometry(QtCore.QRect(400, 51, 171, 101))
        self.pushButton_SavePlotButton.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(200,200,200, 100), stop:1 rgba(255, 255, 255, 80));\n"
"border-radius: 10px;")
        self.pushButton_SavePlotButton.setObjectName("pushButton_SavePlotButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionLoad_Automation = QtWidgets.QAction(MainWindow)
        self.actionLoad_Automation.setObjectName("actionLoad_Automation")
        self.actionSave_Data = QtWidgets.QAction(MainWindow)
        self.actionSave_Data.setObjectName("actionSave_Data")
        self.actionScreenshot = QtWidgets.QAction(MainWindow)
        self.actionScreenshot.setObjectName("actionScreenshot")
        self.actionReset = QtWidgets.QAction(MainWindow)
        self.actionReset.setObjectName("actionReset")

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "etaLab Consumer Monitoring"))
        self.groupBox_MassFlowValve_2.setTitle(_translate("MainWindow", "Mass Flow Valve"))
        self.groupBox_3WayValve_2.setTitle(_translate("MainWindow", "3-Way-Valve"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.globalControlTab), _translate("MainWindow", "Global"))
        self.pushButton_StartAutomation.setText(_translate("MainWindow", "Start"))
        self.pushButton_StopAutomation.setText(_translate("MainWindow", "Stop "))
        self.pushButton_OpenAutomationButton.setText(_translate("MainWindow", "Open"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.automationTab), _translate("MainWindow", "Automation"))
        self.lineEdit_MqttBroker.setText(_translate("MainWindow", "myBroker"))
        self.lineEdit_Port.setText(_translate("MainWindow", "myPort"))
        self.lineEdit_Topic.setText(_translate("MainWindow", "myTopic"))
        self.label_MqttBroker.setText(_translate("MainWindow", "MQTT-Broker:"))
        self.label_Port.setText(_translate("MainWindow", "Port:"))
        self.label_Topic.setText(_translate("MainWindow", "Topic:"))
        self.pushButton_ConnectMQTT.setText(_translate("MainWindow", "Connect"))
        self.pushButton_DisconnectMQTT.setText(_translate("MainWindow", "Disconnect"))
        self.label_State.setText(_translate("MainWindow", "State:"))
        self.label_ConnectionState.setText(_translate("MainWindow", "Connection State"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.mqttConnectiontab), _translate("MainWindow", "MQTT"))
        self.groupBox_CropPlot.setTitle(_translate("MainWindow", "Crop Plot"))
        self.pushButton_CropPlot.setText(_translate("MainWindow", "Crop"))
        self.groupBox_PlotSwitch.setTitle(_translate("MainWindow", "Plot Selection"))
        self.radioButton_PlotSwitchPower.setText(_translate("MainWindow", "Power"))
        self.radioButton_PlotSwitchTemperatur.setText(_translate("MainWindow", "Temp"))
        self.pushButton_SavePlotButton.setText(_translate("MainWindow", "Save"))
        self.actionLoad_Automation.setText(_translate("MainWindow", "Load Automation"))
        self.actionLoad_Automation.setShortcut(_translate("MainWindow", "Ctrl+L"))
        self.actionSave_Data.setText(_translate("MainWindow", "Save Data"))
        self.actionSave_Data.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionScreenshot.setText(_translate("MainWindow", "Screenshot"))
        self.actionScreenshot.setShortcut(_translate("MainWindow", "Ctrl+P"))
        self.actionReset.setText(_translate("MainWindow", "Reset"))
        self.actionReset.setShortcut(_translate("MainWindow", "Ctrl+R"))


