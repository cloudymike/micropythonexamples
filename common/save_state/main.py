# Saves the value for testing


import time
import savestate
import random

count = 0
maxcount = 3


if __name__ == "__main__":
    while(1):
        oldstate = savestate.readState()
        stateval = random.randrange(100)
        state = {'stateval': stateval}
        savestate.writeState(state)
        print('Old:{}  New:{}'.format(oldstate['stateval'], state['stateval']))
        oldstate = state
        time.sleep_ms(750)
        if count > maxcount:
            break
        else:
            count = count + 1
    # Test that writing the same value does not do a write
    savestate.writeState(state)
else:
        stateval = random.randrange(100)
        state = {'stateval': stateval}
        savestate.writeState(state)
        laststate = savestate.readState()
        print(laststate)
        print(state)
        assert(laststate == state)
        print('TESTOK')
