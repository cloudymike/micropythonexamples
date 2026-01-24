import dht
import machine
import time
import LED

d = dht.DHT11(machine.Pin(4))

while(1):
    LED.LED.off()
    time.sleep_ms(500)
    waiting=True
    while(waiting):
    	try:
			d.measure()
			waiting=False
        except:
			time.sleep_ms(500)  

	temperature = d.temperature()
	humidity = d.humidity()
	print("T:{0}C   H:{1}%".format(temperature,humidity))


    LED.LED.on()
    time.sleep_ms(500)
