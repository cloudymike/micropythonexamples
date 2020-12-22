#AWS MQTT client cert example for esp8266 or esp32 running MicroPython 1.9
import time
import wlan
import json
import esp32
import awsiotconfig

from mqtt_writer_aws import MQTTWriterAWS

if __name__ == "__main__":  # pragma: no cover
    wlan.do_connect()
    m = MQTTWriterAWS(
        awsiotconfig.MQTT_CLIENT_ID,
        awsiotconfig.MQTT_HOST,
        awsiotconfig.MQTT_PORT,
        awsiotconfig.MQTT_TOPIC,
        awsiotconfig.KEY_FILE,
        awsiotconfig.CERT_FILE)
    while(1):
        magneto=esp32.hall_sensor()
        print(magneto)
        m.pub_msg("{\"message\":" + str(magneto) + "}")
        time.sleep_ms(750)
