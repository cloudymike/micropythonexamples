#!/bin/bash

USBPORT=$(ls /dev/ | grep -e USB -e ACM)
PORT=/dev/$USBPORT
echo Port used $PORT

PUSHCMD="ampy --port $PORT put "

$PUSHCMD ../oled/ssd1306.py
$PUSHCMD bignumber.py
$PUSHCMD main.py

echo "Resetting board"
sudo timeout 2  ampy --port $PORT run ../reset/reset.py
