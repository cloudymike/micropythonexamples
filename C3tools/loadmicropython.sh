#!/bin/bash

PACKAGE=ESP32_GENERIC_C3-20250415-v1.25.0.bin

PORT='/dev/ttyACM0'
#PORT='/dev/ttyS0'


if [ ! -f $PACKAGE ]
then
	wget https://micropython.org/resources/firmware/$PACKAGE
fi

python3 -m venv venv
source venv/bin/activate
pip install  -r requirements.txt

timeout 1  ampy --port $PORT run reset.py
esptool.py --chip esp32 --port $PORT erase_flash
esptool.py --baud 460800 --port $PORT write_flash 0 ./$PACKAGE

