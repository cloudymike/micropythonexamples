#!/bin/bash

# Attempt to auto generate key
DEVICE=esp32tempctrl
REGISTRY=tempctrl
PROJECT=oauthtest-164000
# Create key
openssl genrsa -out rsa_private.pem 2048
openssl rsa -in rsa_private.pem -pubout -out rsa_public.pem

# Create the integer of the private key
MYKEY=$(python utils/decode_rsa.py)

# TODO create python wrapper for the integer
cat > gcloudconfig.py << EOF
jwt_config = {
    'algorithm':'RS256',
    'token_ttl': 43200, #12 hours
    # Use utiles/decode_rsa.py to decode private pem to pkcs1.
    'private_key':$MYKEY
}
EOF

exit 0

# Push public key to gcloud
gcloud iot devices credentials create \
            --region=us-central1 \
            --project=$PROJECT \
            --registry=$REGISTRY --device=$DEVICE \
            --path=rsa_public.pem --type=rsa-pem \
