#!/bin/bash

PORT=/dev/ttyUSB0
#PACKAGE=esp32-idf3-20210130-unstable-v1.13-305-gb8f4c623f.bin
#PACKAGE=esp32-idf3-20200902-v1.13.bin
#PACKAGE=esp32-idf3-20191220-v1.12.bin
#PACKAGE=esp32-idf3-20190529-v1.11.bin
#PACKAGE=esp32spiram-idf3-20190529-v1.11.bin

#PACKAGE=esp32-idf3-20210130-unstable-v1.13-305-gb8f4c623f.bin
#PACKAGE=esp32-20220117-v1.18.bin
# Old: MicroPython v1.11 on 2019-05-29; ESP32 module with ESP32
#PACKAGE=esp32-idf3-20190529-v1.11.bin

PACKAGE=esp32-20220618-v1.19.1.bin
#PACKAGE=ESP32_GENERIC-20230426-v1.20.0.bin

if [ ! -f $PACKAGE ]
then
	wget https://micropython.org/resources/firmware/$PACKAGE
fi

python3 -m venv venv
source venv/bin/activate
pip install  -r requirements.txt

timeout 1  ampy --port $PORT run reset.py
esptool.py --chip esp32 --port $PORT erase_flash
esptool.py --chip esp32 --port $PORT write_flash -z 0x1000 ./$PACKAGE
