# Complete project details at https://RandomNerdTutorials.com

import textout
import time

t = textout.textout()
if __name__ == "__main__":
    while True:
        t.terminalline('Meaning of life?')
        for answer in range(37,43):
            time.sleep(0.5)
            t.terminalline(answer)
        time.sleep(4)
else:
    t.text('TESTOK')
