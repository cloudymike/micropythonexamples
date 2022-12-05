# Measures magnetic filed with interal hall sensor
# Use a magnet right over the chip, try to turn it if the number does not change
# Be careful, you do not want it to find the pins and short them.

import machine
import esp32
import time
import wlan
from mqtt_local import MQTTlocal
import mqtthost
# Do this with an import
#MQTT_HOST='192.168.62.26'
wlan.do_connect()

# Should this be esp32?
m = MQTTlocal('esp8266', mqtthost.MQTT_HOST, 1883, 'sensor-data', 'BlueLED')
while(1):
    magneto=esp32.hall_sensor()
    print(magneto)
    m.publish(magneto)
    time.sleep_ms(2000)
    m.check_msg()

m.disconnect()
