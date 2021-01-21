#AWS MQTT client cert example for esp8266 or esp32 running MicroPython 1.9
import time
import wlan
import json
import esp32
import awsiotconfig

from mqtt_reader_aws import MQTTReaderAWS

if __name__ == "__main__":  # pragma: no cover
    wlan.do_connect()
    m = MQTTReaderAWS(
        awsiotconfig.MQTT_CLIENT_ID,
        awsiotconfig.MQTT_HOST,
        awsiotconfig.MQTT_PORT,
        awsiotconfig.MQTT_TOPIC,
        awsiotconfig.KEY_FILE,
        awsiotconfig.CERT_FILE)

    print('Start subscribe')
    while 1:
        # wait_msg seems better than subscribe. Go figure.
        # If no message, will wait forever
        #m.subscribe()
        m.wait_msg()

    print('Done, disconnecting')
    m.disconnect()
