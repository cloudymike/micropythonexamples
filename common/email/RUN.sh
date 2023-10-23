#!/bin/bash
PORT='/dev/ttyUSB0'
PUSHCMD="ampy --port $PORT put "

# Enter your path to your WLAN configuration file here, see ../wlan/wlanconfig.py for example
echo "Loading configs"
$PUSHCMD ~/secrets/wlanconfig.py
$PUSHCMD ~/secrets/emailconfig.py

echo "Loading software"
$PUSHCMD ../wlan/wlan.py

$PUSHCMD ../../libraries/uMail/umail.py

$PUSHCMD main.py

echo "Resetting board"
timeout 2  ampy --port /dev/ttyUSB0 run ../reset/reset.py
