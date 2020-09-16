#!/bin/bash

ampy --port /dev/ttyUSB0 put ../wlan/wlan.py
ampy --port /dev/ttyUSB0 put mqtt_writer.py
ampy --port /dev/ttyUSB0 put main.py
