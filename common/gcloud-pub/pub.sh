#!/bin/bash
#gcloud pubsub topics publish any --message="hello"

gcloud iot devices commands send \
    --command-data='hello' \
    --region=us-central1  \
    --registry=tempctrl \
    --device=esp32tempctrl
