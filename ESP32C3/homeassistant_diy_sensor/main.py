# Measures magnetic filed with interal hall sensor
# Use a magnet right over the chip, try to turn it if the number does not change
# Be careful, you do not want it to find the pins and short them.

import machine
import esp32
import time
import wlan
import mqtthost
import LED
import ubinascii
from umqtt.simple import MQTTClient


STATE_TOPIC = "home/diy/hall"
AVAILABILITY_TOPIC = "home/diy/hall/available"

#CLIENT_ID = ubinascii.hexlify(machine.unique_id())
CLIENT_ID = "diy_hall_sensor"
print("CLIENT_ID: {}".format(CLIENT_ID))

gc.collect()

wlan.do_connect()


def main():
    CLIENT = MQTTClient(CLIENT_ID, mqtthost.MQTT_HOST)
    CLIENT.connect()
 
 
    # Publish as available once connected
    CLIENT.publish(AVAILABILITY_TOPIC, "online")
 
    print("Connected to {}, subscribed to {} topic".format(mqtthost.MQTT_HOST, STATE_TOPIC))

    while True:
        data = esp32.hall_sensor()
#        CLIENT.publish('{}/{}'.format(STATE_TOPIC,CLIENT_ID),bytes(str(data), 'utf-8'))
        CLIENT.publish(STATE_TOPIC, bytes(str(data), 'utf-8'))

        print('Sensor state: {}'.format(data))
        time.sleep(5)
 
main()