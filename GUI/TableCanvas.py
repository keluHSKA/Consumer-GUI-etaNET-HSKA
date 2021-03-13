import sys
from PyQt5 import QtCore, QtGui, QtWidgets


from PyQt5.QtCore import Qt
import pandas as pd
import numpy as np
import csv
from numpy import genfromtxt
import time
from PyQt5.QtWidgets import *
import threading as th
#import parameter


class tableCanvas(QTableWidget):
    def __init__(self, parent=None, rowCount = 3, columnCount=2):
        #self.parent = parent
        super(tableCanvas, self).__init__()
        self.setRowCount(rowCount)
        self.setColumnCount(columnCount)
        self.automationRunFlag = False
        self.dataLoaded = False
        self.tcDesiredPower = 0
        self.tcDesiredTemp = 0
        timeInMin = True
        if timeInMin:
            self.timeFactor = 60
        else:
            self.timeFactor=1

    def loadTableData(self, data=None):
        self.lastData = data
        file = open(data, 'r')
        reader = csv.reader(file, delimiter=',')
        names = next(reader)
        self.dataArr = genfromtxt(data, delimiter=',')
        self.dataArr = np.delete(self.dataArr, 0, 0)
        self.numberOfRows = self.dataArr.shape[0]
        self.numberOfColumns = self.dataArr.shape[1]
        self.setRowCount(self.numberOfRows)
        self.setColumnCount(self.numberOfColumns)
        self.fillDataTable(self.dataArr, self.numberOfRows, self.numberOfColumns,names)
        self.dataLoaded=True

    def fillDataTable(self, data, rows, columns, headers):
        m = 0
        self.setHorizontalHeaderLabels(headers)

        while m < rows:
            n = 0
            while n < columns:
                newitem = QTableWidgetItem(str(data[m,n]))
                self.setItem(m, n, newitem)
                n = n+1
            m = m + 1
        #self.horizontalHeader.
        #self.headers = self.horizontalHeader
        #self.headers.setStretchLastSection(True);
        #self.headers.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        #self.headers.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)

    def refreshDataTable(self):
        m = 0
        while m<self.numberOfRows:
            n = 0
            while n < self.numberOfColumns:
                newitem = QTableWidgetItem(self.item(m+1,n))
                self.setItem(m, n, newitem)
                n +=1
                QApplication.processEvents()
            m+=1
        self.removeRow(m-1)

    def setRowColor(self, row, r, g,b):
        i = 0
        while i<3:
            self.item(row, i).setBackground(QtGui.QColor(r, g, b))
            if row>0:
                self.item(row-1, i).setBackground(QtGui.QColor(255, 255, 255))
            i = i+1

    def automationRunThread(self):
        i = 0
        while ((self.automationRunFlag==True) and (i< self.numberOfRows)):
            self.tcDesiredPower = self.dataArr[i, 1]
            self.tcDesiredTemp = self.dataArr[i, 2]
            self.desiredSleepTime = self.timeFactor*self.dataArr[i,3]
            print("DESIRED SLEEP TIME")
            print(self.desiredSleepTime)
            print("/n/n")
            self.setRowColor(0, 90, 125,0)
            self.update()
            time.sleep(self.desiredSleepTime)
            self.refreshDataTable()
            i += 1
            #For Real Time Application:
            #time.sleep(self.desiredSleepTime*60)
        self.dataReadyForAutomation = False
        self.stopAutomation()
        return 0

    def getCurrentSetVal(self):
        return self.tcDesiredPower
    def getCurrentSetTempVal(self):
        return self.tcDesiredTemp

    def stopAutomation(self):
        self.automationRunFlag == False
        self.loadTableData(self.lastData)
        return 0

    def automationRun(self):
        self.automationRunFlag=True
        self.automation = th.Thread(target=self.automationRunThread)
        self.automation.setDaemon(True)
        self.automation.start()

