#!/bin/bash


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

echo loading configs
# Enter your path to your WLAN configuration file here, see ../wlan/wlanconfig.py for example
$PUSHCMD ~/secrets/wlanconfig.py

# This is just to get the host IP address, you may have to change it
echo "MQTT_HOST='$(hostname -I | awk '{print $1}')'" >mqtthost.py
$PUSHCMD mqtthost.py

echo loading mha
$PUSHCMD mha

echo loading other libraries
$PUSHCMD $TOPDIR/wlan/wlan.py
$PUSHCMD $TOPDIR/LED/LED.py

echo loading main
$PUSHCMD main.py

echo "Resetting board"
timeout 2  ampy --port $PORT run ../reset/reset.py
