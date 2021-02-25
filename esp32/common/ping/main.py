# Measures magnetic filed with interal hall sensor
# Use a magnet right over the chip, try to turn it if the number does not change
# Be careful, you do not want it to find the pins and short them.

import wlan
import uping

wlan.do_connect()
result=uping.ping('google.com')
if __name__ != "__main__":
        assert(result == (4,4))
        print('TESTOK')
