# AWS IOT publish

Most of the info is in this article:  https://awsiot.wordpress.com/2019/01/10/connect-8266-to-aws-mqtt-using-miropython/

## (Not so) Quickstart
If you do not have a certificate login to your AWS console and use "Get Started" to create a thing and download the "Connection Kit" (Linux/Python). When you unzip it, the certificates will be included. The URL needs to be updated in main.py, this can be found in start.sh

Put the key and certificate into a safe place and update "loadfiles.sh" to use these files.

Create a file "wlanconfig.py" with wireless lan credentials, see wlan directory for more details. Update loadfiles.sh to load these files.

Use AWS console to check the messages being created
Got to aws console,
AWS IoT -> Manage -> Things ->"NameOfYourDevice" -> Activity ->Mqtt Client ->
Subscribe to a Topic -> "sdk/test/Python"

In a terminal:
```
./loadfiles.sh
sudo picocom /dev/ttyUSB0 -b115200
import machine
machine.reset()
```
The last lines in the output should be something like:
```
Sent: {"upytest":33}
OK
```
Got an check on the AWS console at your subscription client and you should see the same message if all is OK.


A quicker version of reset is to just hit ctrl-D in picocom.
To exit picocom, ctrl-a ctrl-x

## Policy
If there is a problem it is always the policy
Here you can define what client names are allowed to connect. Without that you will get multiple client behave as one and trying to talk over each other. You will also reset both client one one is reset.

You can also define allowed topics so even if you happily change it nothing happens until you put it into allowed topics.

## Configuration
All variables comes in a configuration file. Create this before loading device, see loadfiles.sh
