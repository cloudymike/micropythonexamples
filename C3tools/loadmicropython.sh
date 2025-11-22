#!/bin/bash

PACKAGE=ESP32_GENERIC_C3-20250415-v1.25.0.bin

USBPORT=$(ls /dev/ | grep -e ACM)
if [ "$USBPORT" = "" ]
then
USBPORT=$(ls /dev/ | grep -e USB)
fi

PORT=/dev/$USBPORT
echo Port used $PORT



if [ ! -f $PACKAGE ]
then
	wget https://micropython.org/resources/firmware/$PACKAGE
fi

python3 -m venv venv
source venv/bin/activate
pip install  -r requirements.txt

timeout 1  ampy --port $PORT run reset.py
#esptool.py --chip ESP32-C3 --port $PORT erase_flash
#esptool.py --baud 460800 --chip ESP32-C3 --port $PORT write_flash 0 ./$PACKAGE

# If it fails try this:
esptool.py --no-stub --chip ESP32-C3 --baud 115200 --before default_reset --after hard_reset  write_flash 0  ./$PACKAGE


