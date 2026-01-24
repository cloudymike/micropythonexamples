#!/bin/bash

USBPORT=$(ls /dev/ | grep -e ACM)
if [ "$USBPORT" = "" ]
then
USBPORT=$(ls /dev/ | grep -e USB)
fi
PORT=/dev/$USBPORT
echo Port used $PORT


CURDIR=$(pwd)
TOPDIR=${CURDIR%/*}

ampy --port $PORT put  $TOPDIR/LED/LED.py
ampy --port $PORT put  main.py
timeout 2  ampy --port $PORT run $TOPDIR/reset/reset.py
