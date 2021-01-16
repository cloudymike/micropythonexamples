# Reset of processor
This is a contrived example that resets to processor. Do not try to run it as main
unless you want an endless reset loop.

It is however useful to run as a script interactively to do a soft reboot
after you have loaded up a program"
```
sudo ampy --port /dev/ttyUSB0 run reset.py
```
Or better if you are using in script:
```
sudo timeout 2  ampy --port /dev/ttyUSB0 run reset.py
```


Yes, ampy has a reset command. I have not found it to work as expected, thus the
workaround with the script.
