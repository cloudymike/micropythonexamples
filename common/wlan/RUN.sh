#!/bin/bash
PORT='/dev/ttyUSB0'
PUSHCMD="ampy --port $PORT put "

# Enter your path to your WLAN configuration file here, see ../wlan/wlanconfig.py for example
echo "Loading configs"
$PUSHCMD ~/secrets/wlanconfig.py
echo "Loading software"
$PUSHCMD wlan.py
$PUSHCMD main.py

echo "Resetting board"
timeout 2  ampy --port /dev/ttyUSB0 run ../reset/reset.py
sleep 40
echo "Run test, if OK TESTOK will be shown. If failed, then stacktrace"
ampy --port /dev/ttyUSB0 run test.py
