#AWS MQTT client cert example for esp8266 or esp32 running MicroPython 1.9
from umqtt.robust import MQTTClient
import time
import esp32
import wlan
import json

#This works for either ESP8266 ESP32 if you rename certs before moving into /flash
CERT_FILE = "cert"
KEY_FILE = "key"

#if you change the ClientId make sure update AWS policy
MQTT_CLIENT_ID = "esp32"
MQTT_PORT = 8883

#if you change the topic make sure update AWS policy
MQTT_TOPIC = "upypub"

#Change the following three settings to match your environment
MQTT_HOST = "a2d09uxsvr5exq-ats.iot.us-west-2.amazonaws.com"
#WIFI_SSID = 'Sonic-6887'
#WIFI_PW = ''

mqtt_client = None

class MQTTWriter:
    __slots__ = ('host', 'port', 'topic', 'client')

    def __init__(self, client_id, host, port, topic):
        self.client_id = client_id
        self.host = host
        self.port = port
        self.topic = topic

    def pub_msg(self, msg):
        global mqtt_client
        try:
            mqtt_client.publish(self.topic, msg, qos=0)
            print("Sent: " + msg)
        except Exception as e:
            print("Exception publish: " + str(e))
            raise

    def connect_mqtt(self):
        global mqtt_client

        try:
            with open(KEY_FILE, "r") as f:
                key = f.read()
            print("Got Key")

            with open(CERT_FILE, "r") as f:
                cert = f.read()
            print("Got Cert")

            mqtt_client = MQTTClient(
                client_id=self.client_id,
                server=self.host,
                port=self.port,
                keepalive=5000,
                ssl=True,
                ssl_params={"cert":cert, "key":key, "server_side":False})
            mqtt_client.connect()
            print('MQTT Connected')

        except Exception as e:
            print('Cannot connect MQTT: ' + str(e))
            raise

    def disconnect(self):
        global mqtt_client
        mqtt_client.disconnect()

    def oldmain(self):
        #start execution
        try:
            print("Connecting WIFI")
            #connect_wifi(WIFI_SSID, WIFI_PW)
            wlan.do_connect()
            print("Connecting MQTT")
            connect_mqtt()

            magneto=esp32.hall_sensor()
            pub_msg("{\"message\":" + str(magneto) + "}")
            #pub_msg(messageJson)

            disconnect()

            #myAWSIoTMQTTClient.publish(MQTT_TOPIC, messageJson, 1)
            print("OK")
        except Exception as e:
            print(str(e))




if __name__ == "__main__":  # pragma: no cover
    wlan.do_connect()
    m = MQTTWriter(MQTT_CLIENT_ID, MQTT_HOST, MQTT_PORT, MQTT_TOPIC)
    m.connect_mqtt()
    while(1):
        magneto=esp32.hall_sensor()
        print(magneto)
        m.pub_msg("{\"message\":" + str(magneto) + "}")
        time.sleep_ms(750)
