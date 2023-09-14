from machine import Pin
import time

motion = False
BubbleCount = 0

def handle_interrupt(pin):
    time.sleep_ms(50)
    global BubbleCount
    BubbleCount = BubbleCount + 1
    global interrupt_pin
    interrupt_pin = pin 

led = Pin(2, Pin.OUT)
pir = Pin(4, Pin.IN)

pir.irq(trigger=Pin.IRQ_RISING, handler=handle_interrupt)

while True:
    led.value(1)
    time.sleep(10)
    led.value(0)
    print(BubbleCount)
    BubbleCount = 0
    time.sleep(1)
