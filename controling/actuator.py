import parameter
from parameter import pprint


class actuator:
    def __init__(self, pin, dc=0, freq=1000):
        if parameter.emulate:
            pprint("createt actuator at pin " + str(pin))

        else:
            import pigpio
            global pi
            pi = pigpio.pi()
            #pi = pigpio.pi('soft',8888)

            self.GPIO = pin
            pi.set_mode(self.GPIO, pigpio.OUTPUT)
            pi.set_PWM_frequency(self.GPIO, freq)
            pi.set_PWM_dutycycle(self.GPIO, dc)
            self.prevDC = 0

    def setdc(self, dc):
        self.prevDC = dc
        dc = int(max(min(dc, 255.0), 0.0))
        if parameter.emulate:
            pprint("dutycycle set to " + str(dc))

        else:
            pi.set_PWM_dutycycle(self.GPIO, dc)
            #print("SET ACTUATOR VAL: ", dc)
            
    def getdc(self):
        return self.prevDC
