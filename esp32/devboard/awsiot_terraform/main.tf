provider "aws" {
  region = "us-west-2"
}

resource "aws_iot_thing" "micropython_iot_thing" {
   name = "my-esp32"
}
# Get the aws iot endpoint to print out for reference
data "aws_iot_endpoint" "endpoint" {
    endpoint_type = "iot:Data-ATS"
}

# Output arn of iot thing(s) 
output "iot_endpoint" {
  value = data.aws_iot_endpoint.endpoint.endpoint_address
}

