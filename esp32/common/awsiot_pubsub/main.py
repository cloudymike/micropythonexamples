#AWS MQTT client cert example for esp8266 or esp32 running MicroPython 1.9
import time
import wlan
import json
import esp32
import awsiotconfig
import LED

from mqtt_aws import MQTTAWS

wlan.do_connect()
m = MQTTAWS(
    awsiotconfig.MQTT_CLIENT_ID,
    awsiotconfig.MQTT_HOST,
    awsiotconfig.MQTT_PORT,
    awsiotconfig.MQTT_PUB_TOPIC,
    awsiotconfig.MQTT_SUB_TOPIC,
    awsiotconfig.KEY_FILE,
    awsiotconfig.CERT_FILE)
while(1):
    magneto=esp32.hall_sensor()
    print(magneto)
    m.pub_msg("{\"message\":" + str(magneto) + "}")
    m.check_msg()
    if m.last_msg() == "on":
        LED.LED.on()
    if m.last_msg() == "off":
        LED.LED.off()
    time.sleep_ms(5000)
    if __name__ != "__main__":  # pragma: no cover
        print('TESTOK')
        break
