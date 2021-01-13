#!/bin/bash
PORT='/dev/ttyUSB0'
PUSHCMD="ampy --port $PORT put "

$PUSHCMD ../oled/ssd1306.py
$PUSHCMD ../textout/textout.py
$PUSHCMD ../LED/LED.py
$PUSHCMD main.py
sudo timeout 2  ampy --port /dev/ttyUSB0 run ../reset/reset.py
