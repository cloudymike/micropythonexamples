#!/bin/bash

echo Subscribing to topic...wait until blue light is turned off
watch -n 5 gcloud pubsub subscriptions pull oauthferm1pub --limit=1 --auto-ack
