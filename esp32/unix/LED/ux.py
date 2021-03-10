import time
import machine

class Pin(machine.PinBase):
    '''
    Dummy class that can be used to test a pin
    '''
    OUT='out'
    def __init__(self, pin, direction='out'):
        self.pin = pin
        self.v = False

    def value(self, v=None):
        if v is not None:
            self.v = v==1
        return(int(self.v))


if __name__ == "__main__":
    LED = Pin(2, Pin.OUT)
    for x in range(5):
        LED.value(abs(LED.value()-1))
        print(LED.value())
        time.sleep_ms(500)
