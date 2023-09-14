# Counter of switch input

This example requires extra hardware, see below.

Simple input check. The level of the pin 4 is reflected on the blue LED

You need to add a switch from GPIO4 to VCC (3.3V). The switch should be connected when pressed down. You also need a pull down resistor on the input, 10k ohm should be fine. As an alternative the internal pulldown can be used see switch example.

When ever switch is pressed, the interrupt function is called and will increase the global counter BubbleCounter. The counter value is printed out every 10 seconds and reset.

