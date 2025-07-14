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
$PUSHCMD ../LED/LED.py
$PUSHCMD mqtt_reader.py
$PUSHCMD main.py

echo "Resetting board"
timeout 2  ampy --port $PORT run ../reset/reset.py

echo "Publish message to turn LED on and off"
echo "Loops forever so ctrl-C when done"
while [ 1 ];
do
  mosquitto_pub -t BlueLED -q 0 -m on
  sleep 1
  mosquitto_pub -t BlueLED -q 0 -m off
  sleep 1
done
