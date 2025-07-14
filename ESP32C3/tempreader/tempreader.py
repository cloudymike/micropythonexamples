import machine
import json
import ubinascii
from ds18x20 import DS18X20
from onewire import OneWire



class tempreader:

    def __init__(self, unit='C'):

        pin = machine.Pin(2)
        o = OneWire(pin)

        self.d = DS18X20(o)
        self.devicelist = self.d.scan()
        self.unit = unit



    # Assume there is just one sensor
    # =====================================================
    def get_temp(self):
        all=self.get_temp_list()
        hexi = ubinascii.hexlify(self.devicelist[0])
        return(all[hexi])

    def get_rom(self):
        all=self.get_temp_list()
        hexstr = ubinascii.hexlify(self.devicelist[0]).decode("utf-8")
        return(hexstr)

    # For a full list of sensors get all
    # =====================================================
    def get_temp_list(self):
        tempdict = {}
        self.d.convert_temp()

        # Multiple temperature sensors are OK with onewire bus
        for device in self.devicelist:
            C = self.d.read_temp(device)
            if self.unit == 'F':
                temp=(C * 9/5) + 32
            else:
                temp=C
            tempdict[ubinascii.hexlify(device)] = temp
        return(tempdict)
