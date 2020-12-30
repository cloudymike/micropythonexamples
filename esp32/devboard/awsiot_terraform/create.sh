#!/bin/bash

terraform init

terraform plan -out planfile
terraform apply planfile
terraform output > endpoint.py
