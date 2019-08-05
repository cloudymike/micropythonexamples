import machine
import time

blueLed = machine.Pin(2, machine.Pin.OUT)
pin = machine.Pin(18)

while(1):
    blueLed.off()
    time.sleep_ms(500)
    blueLed.on()
    time.sleep_ms(500)






