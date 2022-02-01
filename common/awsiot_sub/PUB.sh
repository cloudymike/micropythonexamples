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
MQTT_PORT=8883
MQTT_TOPIC="upypub"


echo "Publish message to turn LED on and off"
echo "Loops forever press any key when done"

old_tty=$(stty --save)
# Minimum required changes to terminal.  Add -echo to avoid output to screen.
stty -icanon min 0;

while [ 1 ];
do
  if read -t 0; then # Input ready
      read -n 1 char
      echo -e "\nRead: ${char}\n"
      break
  else # No input
    mosquitto_pub \
    -h "${MQTT_HOST}" \
    --cert ${CERT_FILE_PATH} \
    --cafile ${ROOT_CERT_FILE_PATH} \
    --key ${KEY_FILE_PATH} \
    -t "${MQTT_TOPIC}" \
    -i "testmonitor" \
    -p ${MQTT_PORT} \
    -m "on"

    sleep 5

    mosquitto_pub \
    -h "${MQTT_HOST}" \
    --cert ${CERT_FILE_PATH} \
    --cafile ${ROOT_CERT_FILE_PATH} \
    --key ${KEY_FILE_PATH} \
    -t "${MQTT_TOPIC}" \
    -i "testmonitor" \
    -p ${MQTT_PORT} \
    -m "off"

    sleep 5
  fi
done


stty $old_tty
#pkill -9 mosquitto_sub

echo "Quitting but there may be more messages in the queue so LED may keep blinking"
