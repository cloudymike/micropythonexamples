import sys
if sys.platform == 'linux':
    from ux import Pin
else:
    from machine import Pin

LED = Pin(2, Pin.OUT)
