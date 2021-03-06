#!/bin/bash
PORT='/dev/ttyUSB0'
PUSHCMD="ampy --port $PORT put "

CURDIR=$(pwd)
TOPDIR=${CURDIR%/*}

# Enter your path to your WLAN configuration file here, see ../wlan/wlanconfig.py for example
$PUSHCMD ~/secrets/wlanconfig.py

$PUSHCMD $TOPDIR/wlan/wlan.py
$PUSHCMD $TOPDIR//LED/LED.py
$PUSHCMD main.py

echo "Resetting board to start wlan"
sudo timeout 10  ampy --port /dev/ttyUSB0 run ../reset/reset.py
echo "Get IP address"
sudo timeout 2  ampy --port /dev/ttyUSB0 run ipout.py
echo "Reset board to start server (and hopefully keep address)"
sudo timeout 2  ampy --port /dev/ttyUSB0 run ../reset/reset.py
