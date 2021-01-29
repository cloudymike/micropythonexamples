from simple import MQTTClient
import json
import LED

def sub_cb(topic, msg):
    print((topic, msg))
    if msg == b'on':
        LED.LED.on()
    if msg == b'off':
        LED.LED.off()



class MQTTAWS:
    __slots__ = ('host', 'port', 'topic', 'client')

    def __init__(self, client_id, host, port, pub_topic, sub_topic, key_file, cert_file):
        self.client_id = client_id
        self.host = host
        self.port = port
        self.pub_topic = pub_topic
        self.sub_topic = sub_topic
        self.key_file = key_file
        self.cert_file = cert_file
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
        self.mqtt_client.set_callback(sub_cb)
        self._connect()
        self.mqtt_client.subscribe(topic=self.sub_topic)

    def _connect(self):
        print("Connecting to %s:%s" % (self.host, self.port))
        self.mqtt_client.connect()
        print("Connection successful")

    def pub_msg(self, msg):
        try:
            self.mqtt_client.publish(self.pub_topic, msg, qos=0)
            print("Sent: " + msg)
        except Exception as e:
            print("Exception publish: " + str(e))
            raise

        except Exception as e:
            print('Cannot connect MQTT: ' + str(e))
            raise

    def on_next(self, x):
       data = bytes(json.dumps(x), 'utf-8')
       self.mqtt_client.publish(bytes(self.sub_topic, 'utf-8'), data)

    def disconnect(self):
        self.mqtt_client.disconnect()

    def check_msg(self):
        print("Check messages")
        self.mqtt_client.check_msg()
