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

$PUSHCMD $TOPDIR/oled/ssd1306.py
$PUSHCMD $TOPDIR/textout/textout.py
$PUSHCMD $TOPDIR/LED/LED.py
$PUSHCMD tempreader.py
$PUSHCMD main.py
sudo timeout 2  ampy --port $PORT run ../reset/reset.py
