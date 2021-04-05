#!/bin/bash
#gcloud pubsub topics publish any --message="hello"

gcloud iot devices commands send \
    --command-data=$1 \
    --region=us-central1  \
    --registry=tempctrl \
    --device=esp32tempctrl
