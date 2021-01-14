import relay
import time
HOT = False
COLD = True
if __name__ == "__main__":
    while(1):
        if HOT:
            relay.HOT.on()
            relay.COLD.off()
        else:
            relay.HOT.off()
        if COLD:
            relay.COLD.on()
            relay.HOT.off()
        else:
            relay.COLD.off()

        # Cycle through COLD,HOT,None
        if not (COLD or HOT):
            COLD = True
            HOT = False
        elif COLD :
            HOT = True
            COLD = False
        else:
            HOT = False
            COLD = False
        time.sleep_ms(1000)
