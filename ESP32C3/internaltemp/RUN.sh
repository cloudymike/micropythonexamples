#!/bin/bash

#USBPORT=$(ls /dev/ | grep -e USB -e ACM)
USBPORT=$(ls /dev/ | grep -e ACM)
PORT=/dev/$USBPORT
echo Port used $PORT

CURDIR=$(pwd)
TOPDIR=${CURDIR%/*}

ampy --port $PORT put  main.py
ampy --port $PORT put  internaltempreader.py
timeout 2  ampy --port $PORT run $TOPDIR/reset/reset.py
