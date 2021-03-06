# Micropython examples

This repo includes a number of small examples
for MicroPython, that are developed and tested
on set of MicroPython supported boards. Most of
these are in "Hello World" size. The idea is
to be able to use these examples to quickly get
something working, and to document research done
on pin out diagrams, software versions and more.


## Quick start
Using ampy to load program.
```
sudo ampy --port /dev/ttyUSB0 put main.py
```
* Restart
  * Press "en" button
  * Powercycle (unplug and reconnect usb cable)
  * Use terminal with picocom and ctrl-D (see below)
  * Run reset commands (Yes, this may throw errors, just ignore):
    ```
    sudo ampy --port /dev/ttyUSB0 run <devicename>/reset/reset.py
    ```

(Note: Some examples include a RUN.sh script to do the program loading and resetting of device)

Make sure no one else is talking to the device (i.e. no terminal open)

ampy is a download tool from Adafruit. It can be installed with pip:
`pip install adafruit-ampy`

## Interactive python

Use a terminal program over USB to connect to the device and you should get a
python prompt. If a program is running, Ctrl-c out of it.
```
sudo apt-get install picocom
sudo picocom /dev/ttyUSB0 -b115200
```
Try something simple. This will turn on and off the blue LED
```
>>> import machine
>>> pin = machine.Pin(2, machine.Pin.OUT)
>>> pin.on()
>>> pin.off()
```
This allows you to try your code interactively.

To exit picocom: ctrl-a ctrl-x


## Loading microPython on ESP32
Short summary of commands. You may want to load the latest version and path may be different
(try https://micropython.org/download/esp32/)
```
git clone https://github.com/espressif/esptool.git
sudo esptool/esptool.py --port /dev/ttyUSB0 erase_flash
wget https://micropython.org/resources/firmware/esp32-idf3-20190125-v1.10.bin
sudo esptool/esptool.py --chip esp32 --port /dev/ttyUSB0 write_flash -z 0x1000 ./esp32-idf3-20190125-v1.10.bin
```
## Loading packages (pip install)
Run the module upip to load packages that are required in this collection of example. To install individual packages
follow the instruction below.

To load micropython packages manually, make sure the network is working first. Use the WLAN example to set this up.

Then use upip to install the required package
```
import upip
upip.install("micropython-usomepackagename")
```
Note that all micropython packages follows the name structure above.


## Styleguides
Try to write all codes in classes or functions that are called from main. You can then
run this functions or class methods interactively and do your debugging online a little easier.
See esp32/devboard/LED for a simple example

## Tips and tricks
### Program does not start
After loading the new program nothing is happening. Yes this is expected. You need
to reset to start the program. Either push the EN button or use the terminal
and hit Ctrl-D, or power cycle, or run the reset.py in reset

## Da Docs
https://docs.micropython.org/en/latest/index.html

## More ampy commands
You can use amp to manipulate files and directories> try:
`sudo ampy --port /dev/ttyUSB0 ls`

Other useful commands:
* get    Retrieve a file from the board.
* ls     List contents of a directory on the board.
* mkdir  Create a directory on the board.
* put    Put a file or folder and its contents on the...
* reset  Perform soft reset/reboot of the board.
* rm     Remove a file from the board.
* rmdir  Forcefully remove a folder and all its...
* run    Run a script and print its output.

## Use python as your shell
```
  import os
  os.listdir()
```

## Hard reboot reload device
If you can not get the device to connect it is probably major messed up in flash.
If so erase flash and reload micropython. If it does not even allow connection to
erase flash, then hold down the boot button, start the erase command with esptools
and then let go of the boot button and the device should get erased.
