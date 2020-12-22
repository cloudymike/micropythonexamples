#AWS MQTT client cert example for esp8266 or esp32 running MicroPython 1.9
import time
import wlan
import json
import esp32

from mqtt_writer_aws import MQTTWriterAWS

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

if __name__ == "__main__":  # pragma: no cover
    wlan.do_connect()
    m = MQTTWriterAWS(MQTT_CLIENT_ID, MQTT_HOST, MQTT_PORT, MQTT_TOPIC, KEY_FILE, CERT_FILE)
    while(1):
        magneto=esp32.hall_sensor()
        print(magneto)
        m.pub_msg("{\"message\":" + str(magneto) + "}")
        time.sleep_ms(750)
