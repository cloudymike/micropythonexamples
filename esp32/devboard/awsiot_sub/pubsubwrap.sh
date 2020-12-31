#!/bin/bash
#Wrapper to show generic usage of AWS pubsub


python ./basic_pubsub.py \
  -e "a2d09uxsvr5exq-ats.iot.us-west-2.amazonaws.com" \
  -c /home/mikael/secrets/upytest/upytest.cert.pem \
  -r /home/mikael/secrets/upytest/awsrootca1.crt \
  -k /home/mikael/secrets/upytest/upytest.private.key \
  -t "upypub" \
  -id "testmonitor" \
  -m "subscribe"
