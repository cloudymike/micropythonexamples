#!/bin/bash
PORT='/dev/ttyUSB0'
PUSHCMD="ampy --port $PORT put "

# Enter your path to your WLAN configuration file here, see ../wlan/wlanconfig.py for example
$PUSHCMD ~/secrets/wlanconfig.py

$PUSHCMD wlan.py
$PUSHCMD main.py

echo "Resetting board"
sudo timeout 2  ampy --port /dev/ttyUSB0 run ../reset/reset.py
sleep 20
echo "Run test, if OK TESTOK will be shown. If failed, then stacktrace"
sudo ampy --port /dev/ttyUSB0 run test.py
