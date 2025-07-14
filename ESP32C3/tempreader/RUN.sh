#!/bin/bash

USBPORT=$(ls /dev/ | grep -e USB -e ACM)
PORT=/dev/$USBPORT
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
