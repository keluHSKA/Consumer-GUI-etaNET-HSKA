global systemIdentifier
systemIdentifier = "CHP- SenerTec Dachs G5.5"

global fullscreen
fullscreen = True

global printMessages
printMessages = True

global timeTriggerSendData
#in second
timeTriggerSendData = 1
#timeTriggerSendData = 0.1

global timeTriggervisualData
#in milisecond
timeTriggervisualData = 1000
#timeTriggervisualData = 200

global timeTriggerPowerAnalayser
#in second
timeTriggerPowerAnalayser = 1
#timeTriggerPowerAnalayser = 0.1

global timeTriggerMassFlow
#in second
timeTriggerMassFlow = 1
#timeTriggerMassFlow = 0.1

global timeTriggerMeterbus
#in second
timeTriggerMeterbus = 0.1

global timeTriggerConntrolling
#in second
timeTriggerConntrolling = 0.1

global timeTriggerCanvasUpdate
#in seconds
timeTriggerCanvasUpdate = 1#1

global switchOffMaxT
#in °C
switchOffMaxT = 65

global switchOffMinT
#in °C
switchOffMinT = 20

global mixingValvePin
mixingValvePin = 12

global flowControlValvePin
flowControlValvePin = 18

global emulate
emulate = False

global timeInMin
timeInMin = True


def pprint(message=""):
    if printMessages:
        print(message)
    else:
        pass
