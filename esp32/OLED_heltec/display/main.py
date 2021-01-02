# Complete project details at https://RandomNerdTutorials.com

from machine import Pin, I2C
import ssd1306
from time import sleep
import os
from time import sleep_ms

# Blue LED as status indicator, strarting program
blueLed = Pin(25, Pin.OUT)
blueLed.value(1)

# ESP32 Pin assignment 
i2c = I2C(-1, scl=Pin(15), sda=Pin(4))

# ESP8266 Pin assignment
#i2c = I2C(-1, scl=Pin(5), sda=Pin(24))

# Reset OLED
oledReset=Pin(16, Pin.OUT)
oledReset.value(0)
sleep_ms(500)
oledReset.value(1)

oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

oled.text('Hello, World 2!', 0, 0)
oled.text('Hello, World 2!', 0, 10)
oled.text('Hello, World 3!', 0, 20)
        
oled.show()
sleep_ms(500)
blueLed.value(0)




