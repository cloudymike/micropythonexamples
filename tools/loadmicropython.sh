#!/bin/bash
PACKAGE=esp32-idf3-20210130-unstable-v1.13-305-gb8f4c623f.bin
PACKAGE=esp32-idf3-20200902-v1.13.bin
PACKAGE=esp32-idf3-20191220-v1.12.bin
PACKAGE=esp32-idf3-20190529-v1.11.bin
#PACKAGE=esp32spiram-idf3-20190529-v1.11.bin

#PACKAGE=esp32-idf3-20210130-unstable-v1.13-305-gb8f4c623f.bin
#PACKAGE=esp32-20220117-v1.18.bin
# Old: MicroPython v1.11 on 2019-05-29; ESP32 module with ESP32

if [ ! -f $PACKAGE ]
then
	wget https://micropython.org/resources/firmware/$PACKAGE
fi

timeout 1  ampy --port /dev/ttyUSB0 run reset.py
esptool/esptool.py --port /dev/ttyUSB0 erase_flash
esptool/esptool.py --chip esp32 --port /dev/ttyUSB0 write_flash -z 0x1000 ./$PACKAGE
