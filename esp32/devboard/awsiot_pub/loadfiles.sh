#!/bin/bash

#Define some variables, change if needed

# These are your certificates, update with the path were you put it (and NOT in the repo)
CERT_FILE_PATH=../awsiot_terraform/certs/upyex_cert.pem.crt
ROOT_CERT_FILE_PATH=../awsiot_terraform/certs/AmazonRootCA1.pem
KEY_FILE_PATH=../awsiot_terraform/certs/upyex_cert.private.key

WLAN_CONFIG_PATH=~/secrets/upytest/wlanconfig.py

# Server and topic
#MQTT_HOST="a2d09uxsvr5exq-ats.iot.us-west-2.amazonaws.com"
MQTT_HOST=$(cut -f 3 -d ' ' < ../awsiot_terraform/endpoint.py)

MQTT_TOPIC="upypub"

# Filename for cert and key on the esp32 device
CERT_FILE=cert
KEY_FILE=key

# Create command alias
PORT='/dev/ttyUSB0'
PUSHCMD="ampy --port $PORT put "

echo "Loading certs and keys"
$PUSHCMD ${CERT_FILE_PATH} ${CERT_FILE}
$PUSHCMD ${KEY_FILE_PATH} ${KEY_FILE}
$PUSHCMD ${WLAN_CONFIG_PATH}

# Create configuration file
cat > awsiotconfig.py << EOF
CERT_FILE = "${CERT_FILE}"
KEY_FILE = "${KEY_FILE}"

#if you change the ClientId make sure update AWS policy
MQTT_CLIENT_ID = "esp32"
MQTT_PORT = 8883

#if you change the topic make sure update AWS policy
MQTT_TOPIC = "${MQTT_TOPIC}"

#Change the following to match your environment
MQTT_HOST = "${MQTT_HOST}"
EOF

echo "Loading programs"
$PUSHCMD ../wlan/wlan.py
$PUSHCMD mqtt_writer_aws.py
$PUSHCMD awsiotconfig.py
$PUSHCMD main.py

echo "Reset board manually"
echo "Starting test monitor"


python ./basic_pubsub.py \
  -e "${MQTT_HOST}" \
  -c ${CERT_FILE_PATH} \
  -r ${ROOT_CERT_FILE_PATH} \
  -k ${KEY_FILE_PATH} \
  -t "${MQTT_TOPIC}" \
  -id "testmonitor" \
  -m "subscribe"
