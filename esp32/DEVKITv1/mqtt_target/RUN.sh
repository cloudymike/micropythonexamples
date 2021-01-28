#!/bin/bash
PORT='/dev/ttyUSB0'
PUSHCMD="ampy --port $PORT put "

CURDIR=$(pwd)
TOPDIR=${CURDIR%/*}

# Enter your path to your WLAN configuration file here, see ../wlan/wlanconfig.py for example
$PUSHCMD ~/secrets/wlanconfig.py

# This is just to get the host IP address, you may have to change it
echo "MQTT_HOST='$(hostname -I | awk '{print $1}')'" >mqtthost.py
$PUSHCMD mqtthost.py

$PUSHCMD $TOPDIR/wlan/wlan.py
$PUSHCMD $TOPDIR/LED/LED.py
$PUSHCMD $TOPDIR/textout/textout.py
$PUSHCMD mqtt_reader.py
$PUSHCMD main.py

echo "Resetting board"
sudo timeout 2  ampy --port /dev/ttyUSB0 run ../reset/reset.py

echo "Publish message to turn LED on and off"
echo "Loops forever so ctrl-C when done"
while [ 1 ];
do
  mosquitto_pub -t BlueLED -q 0 -m $((65 + $RANDOM % 10))
  sleep 1
done
