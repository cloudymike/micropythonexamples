
from machine import Pin, SPI
import max7219
from time import sleep, sleep_ms
import gfx



spi = SPI(1, baudrate=10000000)
screen = max7219.Max7219(32, 8, spi, Pin(15))


print("fill0")
screen.fill(0)
screen.show()
sleep(1)


screen.text('Hej!',-1,0,1)
screen.show()
sleep(1)

print("numbers")
screen.brightness(8)
screen.fill(0)
screen.text('1234', 0, 0, 1)
screen.show()
sleep(1)

print("text")
screen.fill(0)
screen.text('ABCD', 0, 0, 1)
screen.show()
sleep(1)

print("brightness")
for level in range(12):
	screen.fill(0)
	screen.brightness(level)
	screen.text(str(level),0,0,1)
	screen.show()
	sleep_ms(500)

print("graphics")
screen.fill(0)
graphics = gfx.GFX(32, 8, screen.pixel)
graphics.fill_circle(16, 4, 3, 1)
screen.show()
sleep(1)

print("pixels")
screen.brightness(8)
screen.fill(0)
screen.show()
for number in range(30):
	screen.pixel(number+1,7,1)
	screen.show()
	sleep_ms(100)
for number in range(30):
	screen.pixel(number+1,7,0)
	screen.show()
	sleep_ms(100)

screen.fill(0)
screen.text("bye!",-1,0,1)
screen.show()

