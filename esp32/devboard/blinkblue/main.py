import machine
import time

def blinkblue(ledPin=2):
    blueLed = machine.Pin(ledPin, machine.Pin.OUT)
    pin = machine.Pin(18)

    while(1):
        blueLed.off()
        time.sleep_ms(500)
        blueLed.on()
        time.sleep_ms(500)

if __name__ == "__main__":
    blinkblue()
