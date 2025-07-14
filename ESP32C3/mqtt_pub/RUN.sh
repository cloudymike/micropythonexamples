#!/bin/bash

USBPORT=$(ls /dev/ | grep -e USB -e ACM)
PORT=/dev/$USBPORT
echo Port used $PORT

PUSHCMD="ampy --port $PORT put "

# Enter your path to your WLAN configuration file here, see ../wlan/wlanconfig.py for example
$PUSHCMD ~/secrets/wlanconfig.py

# This is just to get the host IP address, you may have to change it
echo "MQTT_HOST='$(hostname -I | awk '{print $1}')'" >mqtthost.py
$PUSHCMD mqtthost.py

$PUSHCMD ../wlan/wlan.py
$PUSHCMD ../internaltemp/internaltempreader.py
$PUSHCMD mqtt_writer.py
$PUSHCMD main.py

echo "Resetting board"
timeout 2  ampy --port $PORT run ../reset/reset.py

echo "Message published from temperature sensor on device"
mosquitto_sub -t sensor-data
