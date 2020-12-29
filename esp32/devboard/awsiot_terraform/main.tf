provider "aws" {
  region = "us-east-2"
}

resource "aws_iot_thing" "micropython_iot_thing" {
   name = "my-esp32"
}
