#!/bin/bash

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

$PUSHCMD ../oled/ssd1306.py
$PUSHCMD ../oled/gfx.py
$PUSHCMD textout.py
$PUSHCMD main.py

echo "Resetting board"
timeout 2  ampy --port $PORT run $TOPDIR/reset/reset.py
