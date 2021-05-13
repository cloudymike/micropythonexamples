# Saves the value for testing


import time
import savestate
import random

oldstate = savestate.readState()
print()
while(1):
    stateval = random.randrange(100)
    state = {'stateval': stateval}
    savestate.writeState(state)

    print('Old:{}  New:{}'.format(oldstate['stateval'], state['stateval']))

    time.sleep_ms(750)
    if __name__ != "__main__":
        laststate = savestate.readState()

        assert(laststate == state)
        print('TESTOK')
        break
