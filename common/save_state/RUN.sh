#!/bin/bash
PORT='/dev/ttyUSB0'
PUSHCMD="ampy --port $PORT put "
CURDIR=$(pwd)
TOPDIR=${CURDIR%/*}

$PUSHCMD  main.py
$PUSHCMD  savestate.py
sudo timeout 2  ampy --port /dev/ttyUSB0 run $TOPDIR/reset/reset.py
