# Measures magnetic filed with interal hall sensor
# Use a magnet right over the chip, try to turn it if the number does not change
# Be careful, you do not want it to find the pins and short them.

import machine
import esp32
import time
import wlan
from mqtt_writer import MQTTWriter

# Do this with an import
MQTT_HOST='192.168.42.73'

# Should this be esp32?
m = MQTTWriter('esp8266', MQTT_HOST, 1883, 'sensor-data')
while(1):
    magneto=esp32.hall_sensor()
    print(magneto)
    m.on_next(magneto)
    time.sleep_ms(750)
