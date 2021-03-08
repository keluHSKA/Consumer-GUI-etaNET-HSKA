# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import sys
import time
import numpy as np
import threading as th
from PyQt5 import QtWidgets, QtGui, QtCore
import parameter
from parameter import pprint
from GUI import UI
from GUI.MplCanvas import MplCanvas
if parameter.emulate:
    from datacollector.emulatetHeatMeter import HeatMeter
    from observer.observe import Observable
    from controling.EmulatePID import PID
else:
    from datacollector.heatMeter import HeatMeter
    from connections.networkConnection import etaNetClient
    from observer.observe import Observable
    from controling.PID import PID

from controling.actuator import actuator
import pandas as pd
from GUI import TableCanvas as tc
from PyQt5.QtWidgets import *
from GUI import Container
import random
import paho.mqtt.client as mqtt

from connections import mqttNetwork

brokers = ["localhost", "95724970-8a39-4c68-865e-685f3423d23b.ka.bw-cloud-instance.org","193.196.38.87",
           "test.mosquitto.org", "broker.hivemq.com", "iot.eclipse.org", "36754164-7c2a-40b7-9f35-9f562e2c14ba.ka.bw-cloud-instance.org"]

password = "gui"
username = "etalabgui"
#username = "vm-mqtt"

class etaMainApplication(UI.Ui_MainWindow):
    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)
        super(etaMainApplication, self).__init__()
        self.MainWindow = QtWidgets.QMainWindow()
        self.setupUi(self.MainWindow)
        self.canvas = MplCanvas(self);
        self.connect()

        if parameter.emulate:
            self.netconn = Observable()
        else:
            self.netconn = Observable()
            #self.netconn = HeatMeter(Observable)
            #self.netconn = etaNetClient()

        self.init()
        ###
        self.canvas.plotData(self.time, self.isPower, self.setPower, self.plotType)
        self.update = th.Thread(target=self.updateThread)
        #self.update.setDaemon(True)
        self.update.setDaemon(True)

    def connect(self):
        self.pushButton_StartAutomation.clicked.connect(self.startAutomation)
        #self.pushButton_StartAutomation.clicked.connect(self.pidImpulseResponse)
        self.pushButton_StopAutomation.clicked.connect(self.stopAutomation)
        #self.pushButton_ShutDown_2.clicked.connect(self.shutDown)
        self.pushButton_CropPlot.clicked.connect(self.cropPlot)
        self.radioButton_PlotSwitchPower.toggled.connect(lambda: self.plotSwitch("Power"))
        self.radioButton_PlotSwitchTemperatur.toggled.connect(lambda: self.plotSwitch("Temperature"))
        self.spinBox_3WayValve_2.valueChanged.connect(lambda: self.onSpinBox(self.spinBox_3WayValve_2, self.horizontalSlider_3WayValve_2, "3-Way-Valve"))
        self.horizontalSlider_3WayValve_2.valueChanged.connect(lambda: self.onSlider(self.horizontalSlider_3WayValve_2, self.spinBox_3WayValve_2, "3-Way-Valve"))
        self.spinBox_MassFlowValve_2.valueChanged.connect(lambda: self.onSpinBox(self.spinBox_MassFlowValve_2, self.horizontalSlider_MassFlowValve_2, "Mass Flow Valve"))
        self.horizontalSlider_MassFlowValve_2.valueChanged.connect(lambda: self.onSlider(self.horizontalSlider_MassFlowValve_2, self.spinBox_MassFlowValve_2, "Mass Flow Valve"))
        self.spinBox_CropPlot.valueChanged.connect(lambda: self.onSpinBox(self.spinBox_CropPlot, self.horizontalSlider_CropPlot, "Crop Plot"))
        self.horizontalSlider_CropPlot.valueChanged.connect(lambda: self.onSlider(self.horizontalSlider_CropPlot, self.spinBox_CropPlot, "Crop Plot"))
        self.pushButton_StartAutomation.setEnabled(True)
        self.pushButton_StopAutomation.setEnabled(False)
        self.horizontalLayout.addWidget(self.canvas)
        #self.actionLoad_Automation.triggered.connect(lambda: self.openFileDialog("Automation"))
        #self.actionSave_Data.triggered.connect(self.saveDataDialog)
        self.pushButton_OpenAutomationButton.clicked.connect(lambda: self.openFileDialog("Automation"))
        self.pushButton_SavePlotButton.clicked.connect(self.saveDataDialog)
        
        self.lineEdit_MqttBroker.returnPressed.connect(lambda: self.lineEdits("broker"))
        self.lineEdit_Port.returnPressed.connect(lambda: self.lineEdits("port"))
        self.lineEdit_Topic.returnPressed.connect(lambda: self.lineEdits("topic"))
        self.pushButton_ConnectMQTT.setEnabled(True)
        self.pushButton_DisconnectMQTT.setEnabled(False)
        #self.pushButton_ConnectMQTT.clicked.connect(self.startMQTT)
        self.pushButton_ConnectMQTT.clicked.connect(self.connectMQTT)
        self.pushButton_DisconnectMQTT.clicked.connect(self.disconnectMQTT)


    ###
    def init(self):
        self.initArrays()
        self.HeatMeter = HeatMeter(self.netconn)
        self.desiredPower = 50
        self.plotType = "Power"
        self.cropPlotVar = 10
        self.cropFlag = False
        self.table = tc.tableCanvas(self)
        self.tableWidget.addWidget(self.table)
        self.tableData = 'resources/tableData.csv'
        ### MQTT SETUP ###
        #self.mqttBroker = 'test.mosquitto.org'
        #self.mqttBroker = '193.196.38.87'
        self.mqttBroker = brokers[6]

        self.mqttPort = 1883
        #self.mqttPort = 80
        self.mqttTopic = '/python/mqtt'
        self.connectionState = False
        self.lineEdit_MqttBroker.setText(self.mqttBroker)
        self.lineEdit_Port.setText(str(self.mqttPort))
        self.lineEdit_Topic.setText(self.mqttTopic)
        self.label_ConnectionState.setText("Not Connected")
        self.container = Container.Container()
        self.updateContainer = Container.Container()
        self.automationStartTime = -1
        self.mqttConnectedFlag = False
        self.loadAutomationData()
        ###
        #self.TempPID = PID(P=1, D=0, I=0.1)
        #self.TempPID = PID(P=0.6377, D=0.44877, I=0.4263)
        self.TempPID = PID(P=0.201713, D=0.0809676, I=0.04764574)#flachNormiert
        #self.TempPID = PID(P=0.226, D=0.09072, I=0.05338)
        #self.TempPID = PID(P=0.923, D=0.792, I=0.349)#flach
        #self.TempPID = PID(P=0.226, D=0.09072, I=0.05338)#noormiert auf 14°C
        self.TempPID.setSampleTime(parameter.timeTriggerCanvasUpdate)
        #self.FlowPID = PID(P=0.6377, D=0.44877, I=0.4263)
        self.FlowPID = PID(P=0.201713, D=0.0809676, I=0.04764574)#flachNormiert
        #self.FlowPID = PID(P=3.164, D=1.27, I=0.747)#flach
        #self.FlowPID = PID(P=0.00077103, D=0.00031752, I=0.00018685)#normiert auf 4000
        self.FlowPID.setSampleTime(parameter.timeTriggerCanvasUpdate)
        #self.TempActor = actuator(32)
        self.TempActor = actuator(12)
    
        #self.FlowActor = actuator(12)
        self.FlowActor = actuator(18)

    def initArrays(self):
        self.time = np.array([])
        self.isPower = np.array([])
        self.setPower = np.array([])
        self.startTime = time.time()/3600
        self.temp1 = np.array([])
        self.temp2 = np.array([])
        self.powerCrop = np.array([])
        self.tempCrop = np.array([])
        self.dataPointIndex = 0
        self.floatMData = np.array([])
        self.floatMDataTemp = np.array([])
        self.floatMeanCorrFactor = 17
        pprint(self.startTime)
    ###

    def addDataPoint(self, pis, pset, temp1, temp2):
        self.currentTime = time.time()/3600-self.startTime
        self.time = np.append(self.time, self.currentTime)
        self.isPower = np.append(self.isPower, pis)
        self.setPower = np.append(self.setPower, pset)
        self.temp1=np.append(self.temp1, temp1)
        self.temp2=np.append(self.temp2, temp2)
        self.container.set(np.array([self.time,self.isPower,self.setPower,self.temp1, self.temp2]))
        self.updateContainer.set(np.array([self.currentTime, pis, pset, temp1, temp2,self.automationStartTime]))
        
        self.floatMData = np.append(self.floatMData, self.floatingMeanCorr(self.isPower, self.floatMeanCorrFactor, self.dataPointIndex))
        self.floatMDataTemp = np.append(self.floatMDataTemp, self.floatingMeanCorr(self.temp1, self.floatMeanCorrFactor, self.dataPointIndex))
        #print("SHAPE OF IS POWER: ", self.isPower.shape)
        #print("FLOAT MEAN POWER: ", self.floatMData.shape)
        #print("DATA POINT INDEX: ", self.dataPointIndex)

        if self.plotType =="Power":
            if self.cropFlag ==True:
                self.powerCrop = np.array(self.cropFunction(self.time, self.floatMData, self.setPower, self.cropPlotVar))
                self.canvas.plotData(self.powerCrop[0], self.powerCrop[1], self.powerCrop[2], self.plotType)
            else:
                #self.canvas.plotData(self.time, self.isPower, self.setPower, self.plotType)
                self.canvas.plotData(self.time, self.floatMData, self.setPower, self.plotType)

        if self.plotType =="Temperature":
            if self.cropFlag ==True:
                self.tempCrop = np.array(self.cropFunction(self.time, self.temp1, self.temp2, self.cropPlotVar))
                self.canvas.plotData(self.tempCrop[0], self.tempCrop[1], self.tempCrop[2], self.plotType)
            else:
                self.canvas.plotData(self.time, self.temp1, self.temp2, self.plotType)
        self.dataPointIndex = self.dataPointIndex+1

    def startAutomation(self):
        self.automationCancel = True
        self.TempPID.clear()
        self.FlowPID.clear()
        ##HIER NOCH Clear Function für beide Regler aufrufen
        if self.connectionState==False:
            self.automationCancel=self.alertDialog("You are not connected to a MQTT-Broker, the Data won't be send to a Broker!")
            pprint(self.automationCancel)

        if self.automationCancel ==True:
            self.pushButton_StopAutomation.setEnabled(True)
            self.pushButton_StartAutomation.setEnabled(False)
            self.horizontalSlider_3WayValve_2.setEnabled(False)
            self.horizontalSlider_MassFlowValve_2.setEnabled(False)
            self.spinBox_3WayValve_2.setEnabled(False)
            self.spinBox_MassFlowValve_2.setEnabled(False)
            self.initArrays()
            self.automationStartTime = time.time()/3600-self.startTime
            self.table.loadTableData(self.tableData)
            self.setStyle("automation")
            #self.MainWindow.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(227, 190, 27 255), stop:1 rgba(251, 216, 17 255));")
            ###
            if self.table.dataLoaded ==True:
                pprint("Automation Run Call")
                self.table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
                #self.table.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)

                self.table.automationRun()
            else:
                pprint("Please Load Data")
        ###

    def stopAutomation(self):
        self.pushButton_StartAutomation.setEnabled(True)
        self.pushButton_StopAutomation.setEnabled(False)
        self.horizontalSlider_3WayValve_2.setEnabled(True)
        self.horizontalSlider_MassFlowValve_2.setEnabled(True)
        self.spinBox_3WayValve_2.setEnabled(True)
        self.spinBox_MassFlowValve_2.setEnabled(True)
        self.table.automationRunFlag = False
        self.loadAutomationData()
        self.automationStartTime = -1
        self.setStyle()
        self.TempPID.clear()
        self.FlowPID.clear()
        self.TempActor.setdc(0)
        self.FlowActor.setdc(0)
        #self.MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(62, 62, 62, 255), stop:1 rgba(114, 114, 114, 255));")

    def loadAutomationData(self):
        self.table.loadTableData(self.tableData)
        self.table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        ###

    def shutDown(self):
        pprint("ShutDownButton was pressed")
        #self.startMQTT()

    def lineEdits(self, handle=None):
        if handle == "broker":
            self.mqttBroker = self.lineEdit_MqttBroker.text()
            pprint(self.mqttBroker)
        if handle == "port":
            self.mqttPort = self.lineEdit_Port.text()
            pprint(self.mqttPort)
        if handle == "topic":
            self.mqttTopic = self.lineEdit_Topic.text()
            pprint(self.mqttTopic)


        pprint("LineEDIT")
###
    def cropPlot(self):
        pprint(self.pushButton_CropPlot.text())
        current_button_text = self.pushButton_CropPlot.text()

        if current_button_text =="Crop":
            self.pushButton_CropPlot.setText("Full Plot")
            self.cropFlag = True
        if current_button_text == "Full Plot":
            self.pushButton_CropPlot.setText("Crop")
            self.cropFlag = False

    def cropFunction(self,time_vector, data_vector=None, data2_vector=None, cropPlotVar=10):
        if len(time_vector)>2*cropPlotVar:
            time_vector_cropped = time_vector[(len(time_vector) - cropPlotVar):len(time_vector)]
            data_vector_cropped = data_vector[(len(data_vector) - cropPlotVar):len(data_vector)]
            data2_vector_cropped = data2_vector[(len(data2_vector) - cropPlotVar):len(data2_vector)]
            return time_vector_cropped, data_vector_cropped, data2_vector_cropped
        else:
            return time_vector, data_vector, data2_vector, cropPlotVar

    def plotSwitch(self, name, handle=None):
        if name == "Power":
            self.plotType = "Power"
        if name == "Temperature":
            self.plotType = "Temperature"

    def sendDataToCloud(self):
        pprint("MESSAGE TO CLOUD ROUTINE WAS CALLED")
        #self.msgArray = np.array([self.time,self.isPower,self.setPower,self.temp1,self.temp2])

    ###
    def onSlider(self, slider, spinBox, handle=None):
        spinBox.setValue(slider.value())
        ###
        if handle =="Crop Plot":
            self.cropPlotVar = spinBox.value()
        ###
        if handle =="3-Way-Valve":
            self.TempActor.setdc(slider.value())
        if handle =="Mass Flow Valve":
            self.FlowActor.setdc(slider.value())

    def onSpinBox(self, slider, spinBox, handle=None):
        spinBox.setValue(slider.value())
        ###
        if handle =="Crop Plot":
            self.cropPlotVar = slider.value()
        ###
        if handle =="3-Way-Valve":
            self.TempActor.setdc(slider.value())
        if handle =="Mass Flow Valve":
            self.FlowActor.setdc(slider.value())

###
    def openFileDialog(self, ptype):
        dialog = QtWidgets.QFileDialog()
        dialog.setModal(True)
        dialog.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        filename = QtWidgets.QFileDialog.getOpenFileName(dialog, "Open "+str(ptype), "/home")[0]
        if filename != "":
            self.tableData = filename
            self.loadAutomationData()
        else:
            print("Load Data Again")

    def saveDataDialog(self):
        self.headers = ["Time", "isPower", "setPower", "Temp1", "Temp2"]
        self.dataArrayToBeSaved = np.array([self.time, self.isPower, self.setPower, self.temp1, self.temp2])
        dialog = QtWidgets.QFileDialog()
        dialog.setModal(True)
        dialog.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        filename = QtWidgets.QFileDialog.getSaveFileName(dialog, "Save Screenshot", "/home", "Image Files ")[0]
        if filename != "":
            self.canvas.fig.savefig(filename+".png")
            df = pd.DataFrame(np.transpose(self.dataArrayToBeSaved))
            #filepath = filename+'.xls'
            #df.to_excel(filepath, header=self.headers, index=False)
            pd.DataFrame(np.transpose(self.dataArrayToBeSaved)).to_csv(filename+'.csv')

    def alertDialog(self, infoBoxText=""):
        dialog = QDialog()
        dialog.setWindowTitle("ALERT")
        buttons = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        dialog.buttonBox = QDialogButtonBox(buttons)
        dialog.buttonBox.accepted.connect(dialog.accept)
        dialog.buttonBox.rejected.connect(dialog.reject)
        dialog.infoBox = QtWidgets.QLabel()
        dialog.infoBox.setText(infoBoxText)
        dialog.layout = QVBoxLayout()
        dialog.layout.addWidget(dialog.infoBox)
        dialog.layout.addWidget(dialog.buttonBox)
        dialog.setLayout(dialog.layout)
        dialog.exec_()
        return dialog.result()


    def startMQTT(self):
        self.client.runMQTTClient(self.updateContainer)
        self.subscriber.runMQTTSubscriber()
        print(self.container.get())

    def connectMQTT(self):
        self.client = mqttNetwork.mqttClient(self, self.mqttBroker, self.mqttPort, self.mqttTopic, username, password)
        self.subscriber = mqttNetwork.mqttSubscriber(self, self.mqttBroker, self.mqttPort, self.mqttTopic, username, password)
        self.mqttConnectedFlag = self.client.connect_mqtt()
        if self.mqttConnectedFlag ==True:
            self.startMQTT()
            self.connectionState = True
            self.pushButton_ConnectMQTT.setEnabled(False)
            self.pushButton_DisconnectMQTT.setEnabled(True)
            self.label_ConnectionState.setText("Connected")

    def disconnectMQTT(self):
        self.connectionState = False
        self.label_ConnectionState.setText("Not Connected")
        self.pushButton_ConnectMQTT.setEnabled(True)
        self.pushButton_DisconnectMQTT.setEnabled(False)
        self.client.on_disconnect()
        self.subscriber.on_disconnect()

    def setStyle(self, handler=None):
        #default settings
        self.MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(62, 62, 62, 255), stop:1 rgba(114, 114, 114, 255));")
        self.groupBox_Plot.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(86, 170, 255, 125), stop:1 rgba(255, 255, 255, 50));""border-radius: 5px;""font: 20pt \"Avenir\";")
        self.groupBox_valveControl.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(85, 170, 255, 125), stop:1 rgba(255, 255, 255, 50));""border-radius: 5px;""font: 20pt \"Avenir\";")
        self.groupBox_Automation.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(85, 170, 255, 125), stop:1 rgba(255, 255, 255, 50));""border-radius: 5px;""font: 20pt \"Avenir\";")
        self.groupBox_MQTT_Settings.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(85, 170, 255, 125), stop:1 rgba(255, 255, 255, 50));""border-radius: 5px;""font: 20pt \"Avenir\";")
        self.groupBox.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(85, 170, 255, 125), stop:1 rgba(255, 255, 255, 50));""border-radius: 5px;""font: 20pt \"Avenir\";")

        if handler =="automation":
            #self.MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(227, 190, 27, 255), stop:1 rgba(251, 216, 17, 255));")
            self.MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(227, 190, 27, 255), stop:1 rgba(251, 216, 17, 255));")
            self.groupBox_Plot.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(250, 250, 250, 255), stop:1 rgba(210, 210, 210, 210));""border-radius: 5px;""font: 20pt \"Avenir\";")
            self.groupBox_valveControl.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(250, 250, 250, 255), stop:1 rgba(210, 210, 210, 210));""border-radius: 5px;""font: 20pt \"Avenir\";")
            self.groupBox_Automation.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(250, 250, 250, 255), stop:1 rgba(210, 210, 210, 210));""border-radius: 5px;""font: 20pt \"Avenir\";")
            self.groupBox_MQTT_Settings.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(250, 250, 250, 255), stop:1 rgba(210, 210, 210, 210));""border-radius: 5px;""font: 20pt \"Avenir\";")
            self.groupBox.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(250, 250, 250, 255), stop:1 rgba(210, 210, 210, 255));""border-radius: 5px;""font: 20pt \"Avenir\";")

    ###

    def translateHeatMeter(self, s):
        n = ''.join((ch if ch in '0123456789.-' else ' ') for ch in s)
        l = [float(i) for i in n.split()]
        #pprint(s)
        #pprint(l)
        return l


    def run(self):
        self.update.start()
        self.MainWindow.show()
        sys.exit(self.exec_())


    def exec_(self):
        r = self.app.exec_()
        self.HeatMeter.setExit()
        pprint("exit")
        return r
    
    
    def pidImpulseResponse(self):
        self.desiredPower = 3000
        self.TempActor.setdc(255)
        self.FlowActor.setdc(0)
    

    def floatingMeanCorr(self, vector, meanSize =3, index=0):
        self.newArrayEntry = vector[index]
        summe = 0
        j = 0
        if index > meanSize:
            while j<meanSize:
                summe = summe+vector[index-j]
                self.newArrayEntry = summe/meanSize
                j = j+1
        else:
            self.newArrayEntry = vector[index]
            
        return self.newArrayEntry 
        
        

    def updateThread(self):
        #time.sleep(3)
        while self.HeatMeter.getData1()== "'NaN', 'NaN', 'NaN', 'NaN'":
            time.sleep(0.1)
        counter = 0
        while True:
            ###
            if self.table.automationRunFlag ==True:
                self.desiredPower = self.table.getCurrentSetVal()
                #self.FlowPID.update(self.translateHeatMeter(self.HeatMeter.getData1())[0], self.desiredPower)
                #print("MDataShape: ", self.floatMData.shape)
                #print("MDataTempShape: ", self.floatMDataTemp.shape)
                if self.dataPointIndex > 1:
                    print("###FLOW PID###")
                    self.FlowPID.update(self.floatMData[self.dataPointIndex-1], self.desiredPower)
                    #self.FlowActor.setdc(-1*(self.FlowPID.output-255))
                    self.FlowActor.setdc(255-(-1*self.FlowPID.output))
                    print("###TEMP PID###")
                    self.TempPID.update(self.floatMDataTemp[self.dataPointIndex-1], 0)
                    #self.TempActor.setdc(-1*(self.TempPID.output-255))
                    self.TempActor.setdc(255-(-1*self.TempPID.output))
                    

            self.addDataPoint(self.translateHeatMeter(self.HeatMeter.getData1())[0], self.desiredPower,self.translateHeatMeter(self.HeatMeter.getData1())[2],self.translateHeatMeter(self.HeatMeter.getData1())[3])
            #self.updateContainer.set(np.array([self.translateHeatMeter(self.HeatMeter.getData3())[0], self.desiredPower,self.translateHeatMeter(self.HeatMeter.getData3())[2],self.translateHeatMeter(self.HeatMeter.getData3())[3]]))
            time.sleep(parameter.timeTriggerCanvasUpdate)
            QApplication.processEvents()

if __name__ == '__main__':
    a = etaMainApplication()
    a.run()
