#!/bin/bash
PORT='/dev/ttyUSB0'
PUSHCMD="ampy --port $PORT put "
# These are your certificates, update with the path were you put it (and NOT in the repo)
$PUSHCMD ~/secrets/upytest/upytest.cert.pem cert
$PUSHCMD ~/secrets/upytest/upytest.private.key key
$PUSHCMD ~/secrets/upytest/wlanconfig.py

$PUSHCMD ../wlan/wlan.py
$PUSHCMD main.py
echo "Reset board manually"
