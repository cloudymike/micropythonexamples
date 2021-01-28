#!/bin/bash
PORT='/dev/ttyUSB0'
PUSHCMD="ampy --port $PORT put "

CURDIR=$(pwd)
TOPDIR=${CURDIR%/*}

# Enter your path to your WLAN configuration file here, see ../wlan/wlanconfig.py for example
$PUSHCMD ~/secrets/wlanconfig.py

$PUSHCMD $TOPDIR/wlan/wlan.py
$PUSHCMD main.py

#echo "Resetting board"
#sudo timeout 2  ampy --port /dev/ttyUSB0 run ../reset/reset.py
#sleep 20
echo "Run setup of webrepl"
sudo ampy --port /dev/ttyUSB0 run main.py
