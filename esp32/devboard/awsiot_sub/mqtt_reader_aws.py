import machine
from umqtt.simple import MQTTClient
import json


ledPin=2
blueLed = machine.Pin(ledPin, machine.Pin.OUT)

def sub_cb(topic, rawmsg):
    print((topic, rawmsg))
    msgjson = json.loads(rawmsg)
    msg = msgjson['message']
    if msg == "on":
        blueLed.on()
    if msg == "off":
        blueLed.off()


class MQTTReaderAWS:
    __slots__ = ('host', 'port', 'topic', 'client')

    def __init__(self, client_id, host, port, topic, key_file, cert_file):
        self.client_id = client_id
        self.host = host
        self.port = port
        self.topic = topic
        self.key_file = key_file
        self.cert_file = cert_file
        self.mqtt_client = None

        self.connect_mqtt()

        self.mqtt_client.set_callback(sub_cb)
        self.mqtt_client.subscribe(topic=self.topic)


    def connect_mqtt(self):

        try:
            with open(self.key_file, "r") as f:
                key = f.read()
            print("Got Key")

            with open(self.cert_file, "r") as f:
                cert = f.read()
            print("Got Cert")

            self.mqtt_client = MQTTClient(
                client_id=self.client_id,
                server=self.host,
                port=self.port,
                keepalive=5000,
                ssl=True,
                ssl_params={"cert":cert, "key":key, "server_side":False})
            self.mqtt_client.connect()
            print('MQTT Connected')

        except Exception as e:
            print('Cannot connect MQTT: ' + str(e))
            raise

    def disconnect(self):
        self.mqtt_client.disconnect()

    def wait_msg(self):
        self.mqtt_client.wait_msg()