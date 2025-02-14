#!/bin/bash
PORT='/dev/ttyUSB1'
PUSHCMD="ampy --port $PORT put "
CURDIR=$(pwd)
TOPDIR=${CURDIR%/*}

echo load main
$PUSHCMD main.py

echo "Resetting board"
sudo timeout 2  ampy --port $PORT run ../reset/reset.py
