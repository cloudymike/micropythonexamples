# Turns on and off blue LED based on command

import machine
import esp32
import time
import wlan
from mqtt_reader import MQTTReader
import mqtthost
# Do this with an import
#MQTT_HOST='192.168.62.26'
wlan.do_connect()

# Should this be esp32?
m = MQTTReader('esp8266', mqtthost.MQTT_HOST, 1883, 'BlueLED')

while 1:
    m.check_msg()
    time.sleep_ms(100)

m.disconnect()
