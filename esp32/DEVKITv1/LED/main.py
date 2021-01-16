import LED
import time

if __name__ == "__main__":
    while(1):
        LED.LED.off()
        time.sleep_ms(500)
        LED.LED.on()
        time.sleep_ms(500)
