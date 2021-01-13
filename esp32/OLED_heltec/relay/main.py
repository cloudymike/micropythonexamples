import relay
import time
HOT = False
COLD = True
if __name__ == "__main__":
    while(1):
        if HOT:
            relay.HOT.on()
        else:
            relay.HOT.off()
        if COLD:
            relay.COLD.on()
        else:
            relay.COLD.off()

        COLD = not COLD
        HOT = not HOT
        #COLD = COLD and not HOT
        #HOT = HOT and not COLD
        time.sleep_ms(500)
