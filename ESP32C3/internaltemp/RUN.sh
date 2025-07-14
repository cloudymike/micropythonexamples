#!/bin/bash
PORT='/dev/ttyACM4'
PUSHCMD="ampy --port $PORT put "
CURDIR=$(pwd)
TOPDIR=${CURDIR%/*}

ampy --port $PORT put  main.py
ampy --port $PORT put  internaltempreader.py
timeout 2  ampy --port $PORT run $TOPDIR/reset/reset.py
