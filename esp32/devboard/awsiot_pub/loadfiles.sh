#!/bin/bash
PORT='/dev/ttyUSB0'
PUSHCMD="ampy --port $PORT put "
# These are your certificates, update with the path were you put it (and NOT in the repo)
echo "Loading certs and keys"
$PUSHCMD ~/secrets/upytest/upytest.cert.pem cert
$PUSHCMD ~/secrets/upytest/upytest.private.key key
$PUSHCMD ~/secrets/upytest/wlanconfig.py

echo "Loading programs"
$PUSHCMD ../wlan/wlan.py
$PUSHCMD mqtt_writer_aws.py
$PUSHCMD main.py
echo "Reset board manually"
echo "Starting test monitor"
./pubsubwrap.sh
