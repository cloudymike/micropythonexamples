# Saves a dict, as json to a file and reads it back
# Intended to be used at startup
# Use a magnet right over the chip, try to turn it if the number does not change
# Be careful, you do not want it to find the pins and short them.


import json

def readState(filename='/state.json'):
    try:
        with open(filename, "r") as f:
            state = json.load(f)
            return(state)
    except:
        return({})

def writeState(state, filename='/state.json'):
    oldState = readState(filename)
    if oldState != state:
        print("Writing state {}".format(state))
        with open(filename, "w") as f:
                json.dump(state, f)
