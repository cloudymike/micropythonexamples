# Complete project details at https://RandomNerdTutorials.com

from machine import Pin, I2C
import ssd1306
from time import sleep
import os
from time import sleep_ms
import gfx




# ESP32C3 Pin assignment
i2c = I2C(-1, scl=Pin(9), sda=Pin(8))

# ESP32 Pin assignment
#i2c = I2C(-1, scl=Pin(22), sda=Pin(21))

# ESP8266 Pin assignment
#i2c = I2C(-1, scl=Pin(5), sda=Pin(24))

# Reset OLED
#oledReset=Pin(16, Pin.OUT)
#oledReset.value(0)
#sleep_ms(500)
#oledReset.value(1)

oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

oled.text('Hello, World 1!', 0, 0)
oled.text('Hello, World 2!', 0, 10)
oled.text('Hello, World 3!', 0, 20)

oled.show()
sleep_ms(1000)

oled.fill(0)
graphics = gfx.GFX(oled_width, oled_height, oled.pixel)
graphics.fill_circle(64, 16, 16, 1)
oled.show()
sleep_ms(1000)

oled.fill(1)
oled.show()
sleep_ms(1000)

oled.fill(0)
oled.text('The end!', 60, 49)
oled.show()
