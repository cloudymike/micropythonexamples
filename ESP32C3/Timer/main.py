from machine import Timer
import time
sum = 0

def cb(x):
    global sum
    sum = sum+x
    print("Timer adder:{}".format(sum))


tim = Timer(0)
tim.init(period=5000, mode=Timer.ONE_SHOT, callback=lambda t:print("Hello world"))

tim3 = Timer(0)
tim3.init(period=3000, mode=Timer.PERIODIC, callback=lambda t:cb(3))

count = 0
while True:
    count = count + 1
    print("            Main loop: {}".format(count))
    time.sleep(1)
