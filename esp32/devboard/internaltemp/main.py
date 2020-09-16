# Measures temp with internal sensor.
# The chip heats up so not very accurate

import machine
import esp32
import time


while(1):
    temp=esp32.raw_temperature()
    print(temp)
    time.sleep_ms(750)
