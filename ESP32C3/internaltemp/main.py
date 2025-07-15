# Measures temp with internal sensor.
# The chip heats up so not very accurate

import machine
import esp32
import time
import internaltempreader

unit='F'
tempDevice = internaltempreader.internaltempreader(unit)

while(1):
    temp = tempDevice.get_temp()
    print(temp)
    time.sleep_ms(750)
    if __name__ != "__main__":
        assert(type(temp) == int)
        print('TESTOK')
        break
