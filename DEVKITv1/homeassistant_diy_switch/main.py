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

TOPIC_PREFIX="homeassistant"
COMMAND_TOPIC = "{}/diy/blueled/set".format(TOPIC_PREFIX)
STATE_TOPIC = "{}/diy/blueled".format(TOPIC_PREFIX)
AVAILABILITY_TOPIC = "{}/diy/blueled/available".format(TOPIC_PREFIX)

CLIENT = None
#CLIENT_ID = ubinascii.hexlify(machine.unique_id())
CLIENT_ID = "diy_led_switch"
print("CLIENT_ID: {}".format(CLIENT_ID))

gc.collect()

wlan.do_connect(CLIENT_ID)

def new_msg(topic, msg):

    print("Received {}".format(msg))

    if msg == b"on":
        LED.LED.value(1)
        CLIENT.publish(STATE_TOPIC, "on")
    elif msg == b"off":
        LED.LED.value(0)
        CLIENT.publish(STATE_TOPIC, "off")


def main():
    global CLIENT
    CLIENT = MQTTClient(CLIENT_ID, mqtthost.MQTT_HOST)
    CLIENT.set_callback(new_msg)
    CLIENT.connect()
 
    CLIENT.subscribe(COMMAND_TOPIC)
 
    # Publish as available once connected
    CLIENT.publish(AVAILABILITY_TOPIC, "online")
 
    print("Connected to {}, subscribed to {} topic".format(mqtthost.MQTT_HOST, COMMAND_TOPIC))
 
    try:
        while 1:
            CLIENT.wait_msg()
    finally:
        CLIENT.publish(AVAILABILITY_TOPIC, "offline")
        CLIENT.disconnect()
 
main()