import machine
import time
import sys
import os

def toggle(p):
    p.value(not p.value())

# Pin definitions
blueLed = machine.Pin(25, machine.Pin.OUT)
blueLed.value(0)

while True:
    toggle(blueLed)
    time.sleep_ms(500)




