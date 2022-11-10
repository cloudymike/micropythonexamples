#!/bin/bash

#Define some variables, change if needed

WLAN_CONFIG_PATH=~/secrets/wlanconfig.py
CURDIR=$(pwd)
TOPDIR=${CURDIR%/*}

# Create command aliasPORT='/dev/ttyUSB0'
PORT='/dev/ttyUSB0'
PUSHCMD="ampy --port $PORT put "

echo "Loading network code and configs"
ampy --port '/dev/ttyUSB0' put ${WLAN_CONFIG_PATH}
ampy --port '/dev/ttyUSB0' put $TOPDIR/common/wlan/wlan.py
ampy --port '/dev/ttyUSB0' put $TOPDIR/common/wlan/main.py
echo "Starting network"
echo "Resetting board"
timeout 2  ampy --port /dev/ttyUSB0 run $TOPDIR/common/reset/reset.py
sleep 20
echo "Install pip packages"
ampy --port '/dev/ttyUSB0' run upip_install.py
