import time
import random

class PID:
    """PID Controller
    """

    def __init__(self, P=0.2, I=0.0, D=0.0, current_time=None):

        self.Kp = P
        self.Ki = I
        self.Kd = D

        self.current_time = current_time

        self.clear()

    def clear(self):
        self.SetPoint = 0.0
        self.output = 0.0

    def update(self, feedback_value, current_time=None):
            self.current_time = current_time
            self.output = self.SetPoint - feedback_value + random.gauss(0, 0.5)

    def setKp(self, proportional_gain):
        self.Kp = proportional_gain

    def setKi(self, integral_gain):
        self.Ki = integral_gain

    def setKd(self, derivative_gain):
        self.Kd = derivative_gain

    def setWindup(self, windup):
        self.windup_guard = windup

    def setSampleTime(self, sample_time):
        self.sample_time = sample_time
