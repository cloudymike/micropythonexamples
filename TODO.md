# Ideas of projects to do

## Current mission
* To create an aws mqtt device that can publish and subscribe from AWS.
* The device should be able to receive commands like desire temperature for temperature control
* The device should be able to publish current state, as temperature
* The device should display locally current desired and actual state, as temperature.
* The device should be able to interface with hardware
    * Temperature sensor
    * Relay control
* The device should run internal controller for reaching desired state, as PID or simple thermostat


## MQTT
Examples:
* https://micropython-iot-hackathon.readthedocs.io/en/latest/mqtt.html
* https://pycom.io/get-started-subscribing-and-publishing-messages-in-micropython-using-mqtt/
Create example of pub/sub
* publish: Type input to publish or temperature
* subscribe: LED control

Use MQTT cli (mosquitto_pub and mosquitto_sub)

## AWS MQTT
Same as MQTT but with AWS setup
Use this as example: https://awsiot.wordpress.com/2019/01/10/connect-8266-to-aws-mqtt-using-miropython/

* publish: Type input to publish or temperature
* subscribe: LED control

## Display text
Type input to OLED display
https://randomnerdtutorials.com/micropython-oled-display-esp32-esp8266/
