import LED
import time

if __name__ == "__main__":
    while(1):
        LED.LED.value(abs(LED.LED.value()-1))
        time.sleep_ms(500)
