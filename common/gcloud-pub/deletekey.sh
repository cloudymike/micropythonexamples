#!/bin/bash

DEVICE=esp32tempctrl
REGISTRY=tempctrl
PROJECT=oauthtest-164000


# Push public key to gcloud
gcloud iot devices credentials delete \
            --region=us-central1 \
            --project=$PROJECT \
            --registry=$REGISTRY \
            --device=$DEVICE \
            0
