#!/bin/bash

echo Subscribing to topic...wait until blue light is turned off
watch gcloud pubsub subscriptions pull oauthferm1pub --limit=1 --auto-ack
