#!/bin/bash
PORT='/dev/ttyUSB0'
PUSHCMD="ampy --port $PORT put "
CURDIR=$(pwd)
TOPDIR=${CURDIR%/*}

ampy --port $PORT put  LED.py
ampy --port $PORT put  main.py
timeout 2  ampy --port /dev/ttyUSB0 run $TOPDIR/reset/reset.py
