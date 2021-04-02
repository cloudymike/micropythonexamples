import machine
import time
import json
import ubinascii
from ds18x20 import DS18X20
from onewire import OneWire

blueLed = machine.Pin(2, machine.Pin.OUT)

pin = machine.Pin(18)

o = OneWire(pin)
d = DS18X20(o)


while(1):
    
    devicelist = d.scan()
    tempdict = {}
    mydict = {}
    d.convert_temp()
    
    blueLed.off()
    time.sleep_ms(750)

    for device in devicelist:
        tempdict[ubinascii.hexlify(device)] = d.read_temp(device)
    mydict['devicelist'] = tempdict
    mystr = json.dumps(mydict)
    print(mystr)
    blueLed.on()






