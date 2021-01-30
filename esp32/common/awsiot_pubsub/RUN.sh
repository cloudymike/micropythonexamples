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
MQTT_PUB_TOPIC="upypub"
MQTT_SUB_TOPIC="upysub"

# Filename for cert and key on the esp32 device
CERT_FILE=cert
KEY_FILE=key

# Create command alias
PORT='/dev/ttyUSB0'
PUSHCMD="ampy --port $PORT put "
CURDIR=$(pwd)
TOPDIR=${CURDIR%/*}

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

MQTT_PORT = "${MQTT_PORT}"

#if you change the topic make sure update AWS policy
MQTT_PUB_TOPIC = "${MQTT_PUB_TOPIC}"
MQTT_SUB_TOPIC = "${MQTT_SUB_TOPIC}"

#Change the following to match your environment
MQTT_HOST = "${MQTT_HOST}"
EOF

echo "Loading programs"
$PUSHCMD $TOPDIR/wlan/wlan.py
$PUSHCMD mqtt_aws.py
$PUSHCMD awsiotconfig.py
$PUSHCMD main.py

echo "Resetting board"
sudo timeout 2  ampy --port /dev/ttyUSB0 run ../reset/reset.py

echo "Message published from hall sensor on device"

mosquitto_sub \
  -h "${MQTT_HOST}" \
  --cert ${CERT_FILE_PATH} \
  --cafile ${ROOT_CERT_FILE_PATH} \
  --key ${KEY_FILE_PATH} \
  -t "${MQTT_PUB_TOPIC}" \
  -i "testmonitor" \
  -p ${MQTT_PORT} &

  echo "Publish message to turn LED on and off"
  echo "Loops forever press any key when done"

  old_tty=$(stty --save)
  # Minimum required changes to terminal.  Add -echo to avoid output to screen.
  stty -icanon min 0;


  while true ; do
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
          sleep 1
          mosquitto_pub \
          -h "${MQTT_HOST}" \
          --cert ${CERT_FILE_PATH} \
          --cafile ${ROOT_CERT_FILE_PATH} \
          --key ${KEY_FILE_PATH} \
          -t "${MQTT_TOPIC}" \
          -i "testmonitor" \
          -p ${MQTT_PORT} \
          -m "off"
          sleep 1
      fi
  done

  stty $old_tty
  pkill -9 mosquitto_sub

  echo "Quitting but there may be more messages in the queue so LED may keep blinking"
