# Simple test to see if google can be pinged
# Also a simple test that network is running

import wlan
import uping

wlan.do_connect()
result=uping.ping('google.com')
if __name__ != "__main__":
        assert(result == (4,4))
        print('TESTOK')
