import time

import paho.mqtt.client as mqtt
import random
import threading as th
import numpy as np

class mqttClient(mqtt.Client):
    def __init__(self,parent=None, broker='test.mosquitto.org', port =1883,topic='/python/mqtt',userName=None, passWord=None,client_id=f'python-mqtt-{random.randint(0, 1000)}'):
        super(mqttClient, self).__init__()
        # broker = 'broker.emqx.io'
        # broker = 'iot.eclipse.org'
        self.broker = broker
        self.port = port
        self.topic = topic
        self.client_id = client_id
        self.threadKillFlag = False
        self.username = userName
        self.password = passWord

    def connect_mqtt(self):
        def on_connect(client, userdata, flags, rc):
            if rc == 0:
                print("Connected to MQTT Broker!")
            else:
                print("Failed to connect, return code %d\n", rc)

        # Set Connecting Client ID
        self.client = mqtt.Client(self.client_id)
        self.client.on_connect = on_connect
        print("##### ESTABLISHING CONNECTION #####")
        print("Broker: ", self.broker)
        print("Username: ", self.username)
        print("Passw: ", self.password)
        print("Port: ", self.port)
        print("###################################")

        self.client.username_pw_set(username=self.username, password=self.password)
        try:
            self.client.connect(self.broker, self.port)
            self.client.connectedFlag = True
        except:
            self.client.connectedFlag = False
            print("Client Connection Failed!")

        #return self.client
        return self.client.connectedFlag

    def on_disconnect(self):
        #logging.info("disconnecting reason  " + str(rc))
        self.threadKillFlag =True
        self.client.connected_flag = False
        self.client.disconnect()  # disconnect gracefully
        self.client.loop_stop()  # stops network loop

    def publish(self, client):
        msg_count = 0
        while self.threadKillFlag == False:
            time.sleep(1)
            self.data = np.array_str(self.container.get())
            #msg = f"messages: {msg_count}"
            msg = f"messages: {self.data}"
            #result = client.publish(self.topic, msg)
            result = client.publish(self.topic, self.data)
            # result: [0, 1]
            status = result[0]
            if status == 0:
                #print(f"Send `{msg}` to topic `{self.topic}`")
                print(f"Send `{self.data}` to topic `{self.topic}`")
            else:
                print(f"Failed to send message to topic {self.topic}")
            msg_count += 1

    def runMQTTClient(self, container=None):
        self.container = container
        #this function is called by main
        #this function creates a new thread, in which the mqtt client is established
        self.threadKillFlag = False
        self.runMQTTClientTh = th.Thread(target=self.runMQTTClientThread)
        self.runMQTTClientTh.setDaemon(True)
        self.runMQTTClientTh.start()

    def runMQTTClientThread(self):
        #self.client = self.connect_mqtt()
        self.client.loop_start()
        self.publish(self.client)


class mqttSubscriber(mqtt.Client):
    def __init__(self, parent=None, broker='test.mosquitto.org', port =1883,topic='/python/mqtt',userName=None, passWord=None,client_id=f'python-mqtt-{random.randint(0, 1000)}'):
        super(mqttSubscriber, self).__init__()
        self.broker = broker
        self.port = port
        self.topic = topic
        self.client_id = client_id
        self.username = userName
        self.password = passWord

    def connect_mqtt(self) -> mqtt:
        def on_connect(client, userdata, flags, rc):
            if rc == 0:
                print("Connected to MQTT Broker!")
            else:
                print("Failed to connect, return code %d\n", rc)

        self.client = mqtt.Client(self.client_id)
        self.client.on_connect = on_connect
        self.client.username_pw_set(username=self.username, password=self.password)

        try:
            self.client.connect(self.broker, self.port)
            self.client.connected_flag = True
        except:
            print("Subscriber Connection Failed!")
        return self.client

    def on_disconnect(self):
        #logging.info("disconnecting reason  " + str(rc))
        self.client.connected_flag = False
        self.client.disconnect()  # disconnect gracefully
        self.client.loop_stop()  # stops network loop

    def subscribe(self, client: mqtt):
        def on_message(client, userdata, msg):
            print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

        client.subscribe(self.topic)
        client.on_message = on_message

    def runMQTTSubscriber(self):
        self.runMQTTSubscriberTh = th.Thread(target=self.runMQTTSubscriberThread)
        self.runMQTTSubscriberTh.setDaemon(True)
        self.runMQTTSubscriberTh.start()

    def runMQTTSubscriberThread(self):
        self.client = self.connect_mqtt()
        self.subscribe(self.client)
        self.client.loop_forever()
        #self.client.loop_stop()



