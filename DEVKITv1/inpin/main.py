import time
import machine

LED = machine.Pin(2, machine.Pin.OUT)
inpin = machine.Pin(4, machine.Pin.IN, machine.Pin.PULL_DOWN)

while(1):
    switch = inpin.value()
    print("Switch is {}".format(switch))
    if switch:
        LED.value(1)
    else:
        LED.value(0)
    time.sleep_ms(50)
