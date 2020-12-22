#This works for either ESP8266 ESP32 if you rename certs before moving into /flash
CERT_FILE = "cert"
KEY_FILE = "key"

#if you change the ClientId make sure update AWS policy
MQTT_CLIENT_ID = "esp32"
MQTT_PORT = 8883

#if you change the topic make sure update AWS policy
MQTT_TOPIC = "upypub"

#Change the following three settings to match your environment
MQTT_HOST = "a2d09uxsvr5exq-ats.iot.us-west-2.amazonaws.com"
