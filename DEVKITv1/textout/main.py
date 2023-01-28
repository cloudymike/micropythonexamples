# Complete project details at https://RandomNerdTutorials.com

import textout
import time

t = textout.textout()
if __name__ == "__main__":
    while True:
        t.text('Meaning of life?')
        time.sleep(1)
        t.text(42)
        time.sleep(2)
else:
    t.text('TESTOK')
