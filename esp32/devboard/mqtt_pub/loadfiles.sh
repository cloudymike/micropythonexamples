#!/bin/bash
PORT='/dev/ttyUSB0'
PUSHCMD="ampy --port $PORT put "
$PUSHCMD ../wlan/wlan.py
$PUSHCMD mqtt_writer.py
$PUSHCMD main.py
echo "Reset board manually"
mosquitto_sub -t sensor-data
