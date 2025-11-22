#!/bin/bash

#Define some variables, change if needed

WLAN_CONFIG_PATH=~/secrets/wlanconfig.py

# Create command aliasPORT='/dev/ttyUSB0'
USBPORT=$(ls /dev/ | grep -e ACM)
if [ "$USBPORT" = "" ]
then
USBPORT=$(ls /dev/ | grep -e USB)
fi

PORT=/dev/$USBPORT
echo Port used $PORT

PUSHCMD="ampy --port $PORT put "
CURDIR=$(pwd)
TOPDIR=${CURDIR%/*}

echo "Loading wireless"
$PUSHCMD ${WLAN_CONFIG_PATH}
$PUSHCMD $TOPDIR/common/wlan/wlan.py
echo "Load packages"
timeout 20  ampy --port /dev/ttyUSB0 run upip_install.py
