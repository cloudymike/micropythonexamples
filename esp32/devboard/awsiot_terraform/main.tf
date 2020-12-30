provider "aws" {
  region = "us-west-2"
}

resource "aws_iot_thing" "upyex_iot_thing" {
   name = "upyex"
}

# Create an aws iot certificate
resource "aws_iot_certificate" "upyex_cert" {
  active = true
}
# Output certificate to /cert/ folder
resource "local_file" "upyex_cert_pem" {
  content     = aws_iot_certificate.upyex_cert.certificate_pem
  filename = "${path.module}/certs/upyex_cert.pem.crt"
}
# Output private key to /cert/ folder
resource "local_file" "upyex_private_key" {
  content     = aws_iot_certificate.upyex_cert.private_key
  filename = "${path.module}/certs/upyex_cert.private.key"
}


# Get the aws iot endpoint to print out for reference
data "aws_iot_endpoint" "endpoint" {
    endpoint_type = "iot:Data-ATS"
}

# Output arn of iot thing(s) 
output "iot_endpoint" {
  value = data.aws_iot_endpoint.endpoint.endpoint_address
}

