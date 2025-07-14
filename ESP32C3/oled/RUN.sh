#!/bin/bash
PORT='/dev/ttyUSB0'
PUSHCMD="ampy --port $PORT put "

$PUSHCMD ssd1306.py
$PUSHCMD gfx.py
$PUSHCMD bignumber.py
$PUSHCMD main.py

echo "Resetting board"
sudo timeout 2  ampy --port /dev/ttyUSB0 run ../reset/reset.py
