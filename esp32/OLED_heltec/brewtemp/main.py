import machine
import time
import json
import ubinascii
from ds18x20 import DS18X20
from onewire import OneWire
import textout

pin = machine.Pin(18)

o = OneWire(pin)
d = DS18X20(o)
t = textout.textout()

while(1):
    devicelist = d.scan()
    tempdict = {}
    d.convert_temp()

    time.sleep_ms(750)

    # Multiple temperature sensors are OK with onewire bus
    for device in devicelist:
        tempdict[ubinascii.hexlify(device)] = d.read_temp(device)
    for deviceID, temp in tempdict.items():
        print("ID: {}, Temp: {}".format(deviceID, temp))
        t.text("Temp: {:.1f}C".format(temp))
