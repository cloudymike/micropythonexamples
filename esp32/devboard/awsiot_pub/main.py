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

def pub_msg(msg):
    global mqtt_client
    try:
        mqtt_client.publish(MQTT_TOPIC, msg, qos=0)
        print("Sent: " + msg)
    except Exception as e:
        print("Exception publish: " + str(e))
        raise

def connect_mqtt():
    global mqtt_client

    try:
        with open(KEY_FILE, "r") as f:
            key = f.read()
        print("Got Key")

        with open(CERT_FILE, "r") as f:
            cert = f.read()
        print("Got Cert")

        mqtt_client = MQTTClient(client_id=MQTT_CLIENT_ID, server=MQTT_HOST, port=MQTT_PORT, keepalive=5000, ssl=True, ssl_params={"cert":cert, "key":key, "server_side":False})
        mqtt_client.connect()
        print('MQTT Connected')


    except Exception as e:
        print('Cannot connect MQTT: ' + str(e))
        raise

def disconnect():
    global mqtt_client
    mqtt_client.disconnect()

#start execution
try:
    print("Connecting WIFI")
    #connect_wifi(WIFI_SSID, WIFI_PW)
    wlan.do_connect()
    print("Connecting MQTT")
    connect_mqtt()

    magneto=esp32.hall_sensor()

    print("Publishing")
    message = {}
    message['message'] = "Hi from esp32"
    message['sequence'] = 0
    messageJson = json.dumps(message)

    pub_msg("{\"message\":" + str(magneto) + "}")
    #pub_msg(messageJson)

    disconnect()

    #myAWSIoTMQTTClient.publish(MQTT_TOPIC, messageJson, 1)
    print("OK")
except Exception as e:
    print(str(e))
