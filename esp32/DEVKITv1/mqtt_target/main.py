# Turns on and off blue LED based on command

import machine
import esp32
import time
import wlan
from mqtt_reader import MQTTReader
import mqtthost
import gc
import textout



# Do this with an import
#MQTT_HOST='192.168.62.26'
wlan.do_connect()

# Should this be esp32?
m = MQTTReader('esp8266', mqtthost.MQTT_HOST, 1883, 'BlueLED')
txt = textout.textout()
while 1:
    m.check_msg()


    txt.clear()
    txt.centerline("Target: {}".format(m.last_msg()),5)
    txt.centerline("Heap: {}".format(gc.mem_free()),1)
    txt.show()

    time.sleep_ms(100)

m.disconnect()
