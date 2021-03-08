from observer import observe
import threading
import parameter
from parameter import pprint
import time
import datetime
import multiprocessing as pc
from tkinter import *




class HeatMeter(threading.Thread, observe.Observer):

    headerH1 = "'HM1_Power [W]', 'HM1_WaterVolumeFlow [m³/h]', 'HM1_T_Flow [°C]', 'HM1_T_Return [°C]'"
    headerH2 = "'HM2_Power [W]', 'HM2_WaterVolumeFlow [m³/h]', 'HM2_T_Flow [°C]', 'HM2_T_Return [°C]'"
    headerH3 = "'HM3_Power [W]', 'HM3_WaterVolumeFlow [m³/h]', 'HM3_T_Flow [°C]', 'HM3_T_Return [°C]'"

    data1 = "'NaN', 'NaN', 'NaN', 'NaN'"
    data2 = "'NaN', 'NaN', 'NaN', 'NaN'"
    data3 = "'NaN', 'NaN', 'NaN', 'NaN'"

    exit = True
    stop = True

    def __init__(self, observable):
        observe.Observer.__init__(self, observable)
        self.addr = 3

        self.Entry = EmulateEntry()

        threading.Thread.__init__(self)
        threading.Thread.start(self)

    def notify(self):
        if self.addr == 1:
            return self.data1
        if self.addr == 2:
            return self.data2
        if self.addr == 3:
            return self.data3

    def run(self):
        while self.exit:
            if self.stop:
                self.request()
            time.sleep(parameter.timeTriggerMeterbus)

    def request(self):
        powList = self.Entry.get()
        replace = powList[1]
        self.data3 = "{:8.6f}, {:8.6f}, {:8.6f}, {:8.6f}".format(powList[0], replace, powList[3], powList[4])

    def getData3(self):
        return self.data3

    def setExit(self):
        self.exit = False


class EmulateEntry:
    def __init__(self):
        self.Powerreading = pc.Value('d', 0.0)
        self.Flowreading = pc.Value('d', 0.0)
        self.Temperatur1 = pc.Value('d', 0.0)
        self.Temperatur2 = pc.Value('d', 0.0)
        self.process = pc.Process(target=self.EmulateAxisReaderProcess)
        self.process.start()


    def EmulateAxisReaderProcess(self):
        root = Tk()
        root.title("HeatMeterEmulator")

        PowerLabel = Label(root, text="Power [W]").pack()
        PowerEntry = Entry(root)
        PowerEntry.pack()
        FlowLabel = Label(root, text="Flow [m³/h]").pack()
        FlowEntry = Entry(root)
        FlowEntry.pack()
        Temperatur1Label = Label(root, text="Temperatur 1 (Flow) [°C]").pack()
        Temperatur1Entry = Entry(root)
        Temperatur1Entry.pack()
        Temperatur2Label = Label(root, text="Temperatur 2 (Return) [°C]").pack()
        Temperatur2Entry = Entry(root)
        Temperatur2Entry.pack()
        #ButtonSubmit = Button(root, text="Submit", command=lambda: self.onSubmitButton(PowerEntry.get(), FlowEntry.get(), Temperatur1Entry.get(), Temperatur2Entry.get()))
        ButtonSubmit = Button(root, text="Submit",
                              command=lambda: self.onSubmitButton(PowerEntry.get(), FlowEntry.get(),
                                                                  Temperatur1Entry.get(), Temperatur2Entry.get()))
        ButtonSubmit.pack()

        root.mainloop()

    def onSubmitButton(self, p, v, t1, t2):
        self.Powerreading.value = float(p)
        self.Flowreading.value = float(v)
        self.Temperatur1.value = float(t1)
        self.Temperatur2.value = float(t2)


    def get(self):
        a = [self.Powerreading.value, self.Flowreading.value, 0, self.Temperatur1.value, self.Temperatur2.value]
        return a


if __name__ =='__main__':
    o = observe.Observable()
    hm = HeatMeter(o)
    while True:
        time.sleep(1)
        pprint(hm.getData3())