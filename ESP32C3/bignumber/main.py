# Complete project details at https://RandomNerdTutorials.com

from machine import Pin, I2C
import ssd1306
import os
from time import sleep_ms
import bignumber

# Helper function to allow testing without display
def clear(oled):
    if oled:
        oled.fill(0)

def show(oled):
    if oled:
        oled.show()

# Check if display is there.
# If not, keep running but just output text in log
try:
    # ESP32C3 Pin assignment
    #i2c = I2C(-1, scl=Pin(7), sda=Pin(6))
    i2c = I2C(-1, scl=Pin(9), sda=Pin(8))

    # ESP32 Pin assignment
    #i2c = I2C(-1, scl=Pin(22), sda=Pin(21))

    # ESP8266 Pin assignment
    #i2c = I2C(-1, scl=Pin(5), sda=Pin(24))

    oled_width = 128
    oled_height = 64
    oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)
    oled.fill(0)
    oled.show()
except:
    oled = None

for number in range(15):
    clear(oled)
    bignumber.bigNumber(oled, number)
    show(oled)
    sleep_ms(10)

clear(oled)
bignumber.bigTemp(oled, 14.6, 'F')
sleep_ms(1000)
print('TESTOK')
