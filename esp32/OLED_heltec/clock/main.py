# Complete project details at https://RandomNerdTutorials.com

import textout
import time
import machine
import ntptime
import wlan

#ntptime.settime()

wlan.do_connect()
rtc = machine.RTC()
#rtc.init((2014, 5, 1, 4, 13, 0, 0, 0))
print(rtc.datetime())
t = textout.textout()
while True:
    date_str = "Date: {1:02d}/{2:02d}/{0:4d}".format(*rtc.datetime())
    time_str = "UTC: {4:02d}:{5:02d}:{6:02d}".format(*rtc.datetime())
    t.text(time_str)
    time.sleep_ms(100)
