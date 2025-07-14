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
$PUSHCMD ../internaltemp/internaltempreader.py
$PUSHCMD mqtt_local.py
$PUSHCMD main.py

echo "Resetting board"
timeout 2  ampy --port $PORT run ../reset/reset.py

echo "Message published from hall sensor on device"
mosquitto_sub -t sensor-data &

echo "Publish message to turn LED on and off"
echo "Loops forever press any key when done"

old_tty=$(stty --save)
# Minimum required changes to terminal.  Add -echo to avoid output to screen.
stty -icanon min 0;


while true ; do
    if read -t 0; then # Input ready
        read -n 1 char
        echo -e "\nRead: ${char}\n"
        break
    else # No input
        mosquitto_pub -t BlueLED -q 0 -m on
        sleep 1
        mosquitto_pub -t BlueLED -q 0 -m off
        sleep 1
    fi
done

stty $old_tty
pkill -9 mosquitto_sub

echo "Quitting but there may be more messages in the queue so LED may keep blinking"
