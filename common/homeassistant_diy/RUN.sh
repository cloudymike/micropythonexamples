#!/bin/bash
PORT='/dev/ttyUSB0'
PUSHCMD="ampy --port $PORT put "

COMMAND_TOPIC="home/diy/blueled/set"
STATE_TOPIC="home/diy/blueled"
AVAILABILITY_TOPIC="home/diy/blueled/available"


# Enter your path to your WLAN configuration file here, see ../wlan/wlanconfig.py for example
$PUSHCMD ~/secrets/wlanconfig.py

# This is just to get the host IP address, you may have to change it
echo "MQTT_HOST='$(hostname -I | awk '{print $1}')'" >mqtthost.py
$PUSHCMD mqtthost.py

$PUSHCMD ../wlan/wlan.py
$PUSHCMD main.py

echo "Resetting board"
timeout 2  ampy --port /dev/ttyUSB0 run ../reset/reset.py


#exit 1

echo "Message published from hall sensor on device"
mosquitto_sub -t $STATE_TOPIC &

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
        mosquitto_pub -t $COMMAND_TOPIC -q 0 -m on
        sleep 1
        mosquitto_pub -t $COMMAND_TOPIC -q 0 -m off
        sleep 1
    fi
done

stty $old_tty
pkill -9 mosquitto_sub

echo "Quitting but there may be more messages in the queue so LED may keep blinking"
