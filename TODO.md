# Ideas of projects to do

## Current mission
* To create an aws mqtt device that talk to AWS.
    * ✓ publish
        * ✓ mqtt_pub
        * ✓ awsiot_pub
    * subscribe
        * ✓ mqtt_sub
        * ✓ awsiot_sub
* The device should be able to receive commands like desire temperature for temperature control
* ✓ The device should be able to publish current state, as temperature
* The device should display locally current desired and actual state, as temperature.
* ✓ The device should be able to interface with hardware
    * ✓ Temperature sensor
        * ✓ esp32/devboard/brewtemp
    * ✓ Relay control
        * ✓ esp32/devboard/blinkblue
* The device should run internal controller for reaching desired state, as PID or simple thermostat
* Setup WLAN w/o hardcoding: https://randomnerdtutorials.com/micropython-wi-fi-manager-esp32-esp8266/
* OTA code updates: https://medium.com/@ronald.dehuysser/micropython-ota-updates-and-github-a-match-made-in-heaven-45fde670d4eb

## Next steps
* RTC, realtime clock, print output in seconds or show on OLED
  * Use ntp to set time, use UTC for output time
* Over the air software update

## Information and links
Here are some useful pages to draw on for creating the examples
### MQTT
Examples:
* https://micropython-iot-hackathon.readthedocs.io/en/latest/mqtt.html
* https://pycom.io/get-started-subscribing-and-publishing-messages-in-micropython-using-mqtt/

### AWS MQTT
Same as MQTT but with AWS setup
Use this as example: https://awsiot.wordpress.com/2019/01/10/connect-8266-to-aws-mqtt-using-miropython/

### Display text
Type input to OLED display
https://randomnerdtutorials.com/micropython-oled-display-esp32-esp8266/
