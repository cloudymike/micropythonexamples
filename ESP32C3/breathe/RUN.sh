#!/bin/bash
# IF portnumber is not 0 just export a variable with the right number
if [ -n "$PORTNUMBER" ] 
then
	PORT="/dev/ttyACM${PORTNUMBER}"
else
	PORT='/dev/ttyACM0'
fi
echo Port used $PORT

PUSHCMD="ampy --port $PORT put "
CURDIR=$(pwd)
TOPDIR=${CURDIR%/*}

ampy --port $PORT put  main.py
timeout 2  ampy --port $PORT run $TOPDIR/reset/reset.py
