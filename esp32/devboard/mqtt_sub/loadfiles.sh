#!/bin/bash
PORT='/dev/ttyUSB0'
PUSHCMD="ampy --port $PORT put "

# Enter your path to your WLAN configuration file here, see ../wlan/wlanconfig.py for example
$PUSHCMD ~/secrets/wlanconfig.py

# This is just to get the host IP address, you may have to change it
echo "MQTT_HOST='$(hostname -I | awk '{print $1}')'" >mqtthost.py
$PUSHCMD mqtthost.py

$PUSHCMD ../wlan/wlan.py
$PUSHCMD mqtt_reader.py
$PUSHCMD main.py
echo "Reset board manually. To exit testloop, ctrl-c in this windown"
while [ 1 ];
do
  mosquitto_pub -t sensor-data -q 0 -m on
  sleep 1
  mosquitto_pub -t sensor-data -q 0 -m off
  sleep 1
done
