#!/bin/bash

USBPORT=$(ls /dev/ | grep -e USB -e ACM)
PORT=/dev/$USBPORT
echo Port used $PORT

PUSHCMD="ampy --port $PORT put "
CURDIR=$(pwd)
TOPDIR=${CURDIR%/*}

ampy --port $PORT put  main.py
sudo timeout 2  ampy --port $PORT run $TOPDIR/reset/reset.py
