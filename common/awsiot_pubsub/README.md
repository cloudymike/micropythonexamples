# AWS IOT publish

Most of the info is in this article:  https://awsiot.wordpress.com/2019/01/10/connect-8266-to-aws-mqtt-using-miropython/

## (Not so) Quickstart
Run ../awsiot_terraform to create a AWS iot thing. This will create certificates, policy endpoints etc as required

Create a file "wlanconfig.py" with wireless lan credentials, see wlan directory for more details. Update loadfiles.sh to load these files.

Use AWS console to check the messages being created
Got to aws console,
AWS IoT -> Manage -> Things ->"NameOfYourDevice" -> Activity ->Mqtt Client ->
Subscribe to a Topic -> "sdk/test/Python"

The Run.sh script sets everything up and should be enough to run this example.

IF you like to see what device is doing in another terminal, while RUN.sh is running:
```
sudo picocom /dev/ttyUSB0 -b115200
```
The last lines in the output should be something like:
```
Sent: {"message":42}
```
To exit picocom, ctrl-a ctrl-x

## Policy
If there is a problem it is always the policy
Here you can define what client names are allowed to connect. Without that you will get multiple client behave as one and trying to talk over each other. You will also reset both client one one is reset.

You can also define allowed topics so even if you happily change it nothing happens until you put it into allowed topics.

## Configuration
All variables comes in a configuration file. This is created by RUN.sh

## Libraries
You need to load umqtt.simple ("micropython-umqtt.simple"). Run example upip, and it will load this library, among other things.
