import parameter
import meterbus
from connections import networkConnection
from observer import observe
import datetime
import re
import time


class HeatMeter(networkConnection.MBusConnection, observe.Observer):
    dataStr = "'NaN', 'NaN', 'NaN', 'NaN', 'NaN', 'NaN', 'NaN', 'NaN', 'NaN', 'NaN', 'NaN', 'NaN'"
    headerStr = "'HM1_Power [W]', 'HM1_WaterVolumeFlow [m³/h]', 'HM1_T_Flow [°C]', 'HM1_T_Return [°C]', 'HM2_Power [W]', 'HM2_WaterVolumeFlow [m³/h]', 'HM2_T_Flow [°C]', 'HM2_T_Return [°C]', 'HM3_Power [W]', 'HM3_WaterVolumeFlow [m³/h]', 'HM3_T_Flow [°C]', 'HM3_T_Return [°C]'"

    headerH1 = "'HM1_Power [W]', 'HM1_WaterVolumeFlow [m³/h]', 'HM1_T_Flow [°C]', 'HM1_T_Return [°C]'"
    headerH2 = "'HM2_Power [W]', 'HM2_WaterVolumeFlow [m³/h]', 'HM2_T_Flow [°C]', 'HM2_T_Return [°C]'"
    headerH3 = "'HM3_Power [W]', 'HM3_WaterVolumeFlow [m³/h]', 'HM3_T_Flow [°C]', 'HM3_T_Return [°C]'"

    data1 = "'NaN', 'NaN', 'NaN', 'NaN'"
    data2 = "'NaN', 'NaN', 'NaN', 'NaN'"
    data3 = "'NaN', 'NaN', 'NaN', 'NaN'"

    def __init__(self, observable):
        networkConnection.MBusConnection.__init__(self, '192.168.178.66', 10001)
        #networkConnection.MBusConnection.__init__(self, '192.168.178.66', 10001)
        observe.Observer.__init__(self, observable)
        # Regular expression operations to find all scientific numbers
        self.match_number = re.compile('-?\ *[0-9]+\.?[0-9]*(?:[Ee]\ *-?\ *[0-9]+)?')

    def notifyData(self):
        return self.dataStr

    def notifyHeader(self):
        return self.headerStr

    def request(self):
        heatMeterList = []
        # try:
        for addr in range(1, 4):

            data = self.getAllData(addr)
            powerTs = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            telegram = meterbus.load(data)
            # Instabilities/bugs of meterbus lib/package
            find3 = [float(x) for x in re.findall(self.match_number, str(telegram.records[13].interpreted) + str(
                telegram.records[13].interpreted))]
            if find3[0] == 3:
                replace = find3[1]
            else:
                replace = find3[0]

            powList = [float(x) for x in re.findall(self.match_number, str(telegram.records[12].interpreted) \
                                                    + str(telegram.records[13].interpreted) + str(
                telegram.records[9].interpreted) \
                                                    + str(telegram.records[10].interpreted))]

            heatMeterList.append(
                "{:8.6f}, {:8.6f}, {:8.6f}, {:8.6f}".format(powList[0], replace, powList[3], powList[4]))

            self.dataStr = ','.join(heatMeterList)
            self.returnT = powList[4]
            # time.sleep(0.2)
        #print(heatMeterList)
        #print("test")
        self.data1 = heatMeterList[0]
        self.data2 = heatMeterList[1]
        self.data3 = heatMeterList[2]
        #print(self.data1)
        #print(self.data2)
        #print(self.data3)

    def getTreturn(self):
        return self.returnT

    def getHeader1(self):
        return self.headerH1

    def getHeader2(self):
        return self.headerH2

    def getHeader3(self):
        return self.headerH3

    def getData1(self):
        return self.data1

    def getData2(self):
        return self.data2

    def getData3(self):
        return self.data3
