
import machine
import esp32
import time
import wlan
import mqtthost
#import ubinascii
from umqtt.simple import MQTTClient
import mip
import internaltempreader

#CLIENT_ID = ubinascii.hexlify(machine.unique_id())
CLIENT_ID = "inf_internal_sensor"
print("CLIENT_ID: {}".format(CLIENT_ID))

gc.collect()

sta=wlan.do_connect('infint')

# uhome
try:
    import uhome
except:
    print("Exception: uhome not found. Trying to download...")
    mip.install('github:ederjc/uhome/uhome/uhome.py')
    import uhome


device = uhome.Device(CLIENT_ID)
mqttc = MQTTClient(device.id, mqtthost.MQTT_HOST)
device.connect(mqttc)

### DIAGNOSTIC ENTITIES ###
"""
These are some default entities that are useful for diagnostics.
"""
signal_strength = uhome.Sensor(device, 'Signal Strength', device_class="signal_strength", unit_of_measurement='dBm', entity_category="diagnostic")
wifi_ch = uhome.Sensor(device, 'WiFi Channel', device_class="enum", entity_category="diagnostic")
reset_cause = uhome.Sensor(device, 'Last Reset Cause', device_class="enum", entity_category="diagnostic")
ip_addr = uhome.Sensor(device, 'IP Address', device_class="enum", entity_category="diagnostic")

### SENSOR ENTITIES ###
"""
Entities for the connected sensors.
Look here for some docs:
- https://www.home-assistant.io/integrations/sensor.mqtt/
- https://www.home-assistant.io/integrations/sensor#device-class
"""
hall = uhome.Sensor(device, 'Hall')
internaltemperature = uhome.Sensor(device, 'Internal Temperature', unit_of_measurement='C')

"""
The uhome module keeps track of all entities.
With this method we can send the discovery
message for all entities to Home Assistant:
"""
device.discover_all()

### PUBLISH ENTITY VALUES ###
"""
Here we publish the values of the diagnostic entities.
Some of these values are published only once, while others
should be published regularly to keep Home Assistant up to date.
"""
def publishDiagnostics(tmr=None):
    """
    Helper function to publish variable diagnostic values.
    """
    signal_strength.publish(f'{sta.status('rssi'):.0f}')
    wifi_ch.publish(f'{sta.config('channel')}')
    reset_cause.publish(f'{machine.reset_cause()}')
    ip_addr.publish(f'{sta.ifconfig()[0]}')

diagnostics_tmr = machine.Timer(0, mode=machine.Timer.PERIODIC, period=30000, callback=publishDiagnostics)

def publishTemperature(tmr=None):
    '''
    Callback function for retrieving
    internal temperature.
    '''
    internaltemperature.publish(f'{esp32.raw_temperature():.1f}')

def publishHall(tmr=None):
    """
    Helper function to publish magentic value from hall sensor.
    """
    hall.publish(f'{esp32.hall_sensor():.0f}')

it_tmr = machine.Timer(1, mode=machine.Timer.PERIODIC, period=32000, callback=publishTemperature)

hall_tmr = machine.Timer(2, mode=machine.Timer.PERIODIC, period=3000, callback=publishHall)


while True:
    device.loop()
    time.sleep(1)
 
