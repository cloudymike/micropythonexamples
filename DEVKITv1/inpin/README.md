# Switch input

This example requires extra hardware, see below.

Simple input check. The level of the pin 4 is reflected on the blue LED

You need to add a switch from GPIO4 to VCC (3.3V). The switch should be connected when pressed down.

Using the internal pulldown resistor to make it all work. Note that pulldown is unusual but works on many pins on ESP32.
This make it more natural for this simple test (LED is on when you press the switch)
