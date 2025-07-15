# Measures magnetic filed with interal hall sensor
# Use a magnet right over the chip, try to turn it if the number does not change
# Be careful, you do not want it to find the pins and short them.

import machine
import esp32
import time
import wlan
from mqtt_writer import MQTTWriter
import mqtthost
import internaltempreader


# Do this with an import
#MQTT_HOST='192.168.62.26'
wlan.do_connect()
unit='F'
tempDevice = internaltempreader.internaltempreader(unit)

# Should this be esp32?
m = MQTTWriter('esp32c3', mqtthost.MQTT_HOST, 1883, 'sensor-data')
while(1):
    temp = tempDevice.get_temp()

    print(temp)
    m.on_next(temp)
    time.sleep_ms(750)
