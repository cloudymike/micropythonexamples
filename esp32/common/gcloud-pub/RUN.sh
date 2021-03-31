#!/bin/bash

# Create command aliasPORT='/dev/ttyUSB0'
PORT='/dev/ttyUSB0'
PUSHCMD="ampy --port $PORT put "
CURDIR=$(pwd)
TOPDIR=${CURDIR%/*}

echo "Loading programs"
$PUSHCMD ~/secrets/gcloud/config.py
$PUSHCMD third_party
$PUSHCMD main.py

echo "Resetting board"
sudo timeout 2  ampy --port /dev/ttyUSB0 run ../reset/reset.py

./sub.sh
