#!/bin/bash
PORT='/dev/ttyUSB0'
PUSHCMD="ampy --port $PORT put "
CURDIR=$(pwd)
TOPDIR=${CURDIR%/*}

$PUSHCMD $TOPDIR/wlan/wlan.py
$PUSHCMD $TOPDIR/oled/ssd1306.py
$PUSHCMD $TOPDIR/textout/textout.py
$PUSHCMD main.py
sudo timeout 2  ampy --port /dev/ttyUSB0 run ../reset/reset.py
