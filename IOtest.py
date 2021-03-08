from controling.actuator import actuator
from datacollector.emulatetHeatMeter import HeatMeter
from observer import observe
from time import sleep
import parameter

if __name__ == "__main__":
    o = observe.Observable()
    hm = HeatMeter(o)
    a = actuator(parameter.flowControlValvePin)
    while True:
        sleep(1)
        s = hm.getData3()
        n = ''.join((ch if ch in '0123456789.-' else ' ') for ch in s)
        #n = n[35:]
        l = [float(i) for i in n.split()]
        #print (l[3])
        a.setdc(l[3])