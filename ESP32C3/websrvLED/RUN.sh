#!/bin/bash

USBPORT=$(ls /dev/ | grep -e USB -e ACM)
PORT=/dev/$USBPORT
echo Port used $PORT

PUSHCMD="ampy --port $PORT put "

CURDIR=$(pwd)
TOPDIR=${CURDIR%/*}

# Enter your path to your WLAN configuration file here, see ../wlan/wlanconfig.py for example
echo "Loading code and configuration"
$PUSHCMD ~/secrets/wlanconfig.py

$PUSHCMD $TOPDIR/wlan/wlan.py
$PUSHCMD $TOPDIR//LED/LED.py
$PUSHCMD main.py

echo "Resetting board to start wlan"
sudo timeout 10  ampy --port $PORT run ../reset/reset.py
echo "Get IP address"
sudo timeout 2  ampy --port $PORT run ipout.py
echo "Reset board to start server (and hopefully keep address)"
sudo timeout 2  ampy --port $PORT run ../reset/reset.py
