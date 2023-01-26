#!/bin/bash
PORT='/dev/ttyUSB0'
PUSHCMD="ampy --port $PORT put "
CURDIR=$(pwd)
TOPDIR=${CURDIR%/*}

$PUSHCMD ../oled/ssd1306.py
$PUSHCMD ../oled/gfx.py
$PUSHCMD textout.py
$PUSHCMD main.py

echo "Resetting board"
timeout 2  ampy --port /dev/ttyUSB0 run $TOPDIR/reset/reset.py
