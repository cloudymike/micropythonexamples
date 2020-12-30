#!/bin/bash
terraform plan -out planfile
terraform apply planfile
terraform output > endpoint.py
terraform destroy -auto-approve 

