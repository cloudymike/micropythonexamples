#!/bin/bash

USBPORT=$(ls /dev/ | grep -e USB -e ACM)
PORT=/dev/$USBPORT
echo Port used $PORT

PUSHCMD="ampy --port $PORT put "

echo ssd1306
$PUSHCMD ssd1306.py
echo gfx
$PUSHCMD gfx.py
echo main
$PUSHCMD main.py

echo "Resetting board"
sudo timeout 2  ampy --port $PORT run ../reset/reset.py
