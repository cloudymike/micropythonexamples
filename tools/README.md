# Tools to help with development

## When in doubt, run reload.sh
Reload.sh does a complete reload of all the firmware and packages needed
in most of the examples.

The actual version to use is defined in loadmicropython.sh, change  this if you
want a different version.

In addition to loading the firmware and python packages, it will also do some
simple testing to see that it is loaded OK.

## pub.sh
Publish a message to device, setup with mqtt. Uses same parameters from ../common/terraform as the device
Usage:
  `pub.sh 'message string'`
This is to manually test that the mqtt with AWS is working.
