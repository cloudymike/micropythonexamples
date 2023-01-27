#!/bin/bash
pushd tools
./loadmicropython.sh
sleep 5
timeout 5  ampy --port /dev/ttyUSB0 run ./getversion.py
popd
pushd DEVKITv1
./test.sh
popd
