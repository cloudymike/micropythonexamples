# Measures magnetic filed with interal hall sensor
# Use a magnet right over the chip, try to turn it if the number does not change
# Be careful, you do not want it to find the pins and short them.

import machine
import esp32
import time

while(1):
    magneto=esp32.hall_sensor()
    print(magneto)
    time.sleep_ms(750)
    if __name__ != "__main__":
        assert(type(magneto) == int)
        print('TESTOK')
        break
