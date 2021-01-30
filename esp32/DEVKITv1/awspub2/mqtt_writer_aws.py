from simple import MQTTClient
import json
import time

class MQTTWriterAWS:
    __slots__ = ('host', 'port', 'topic', 'client')

    def __init__(self, client_id, host, port, topic, key_file, cert_file):
        self.client_id = client_id
        self.host = host
        self.port = port
        self.topic = topic
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
        self._connect()

    def _connect(self):
        print("Connecting to %s:%s" % (self.host, self.port))
        connected = False
        while not connected:
            try:
                self.mqtt_client.connect()
                connected = True
            except:
                print("Try to connect mqtt again....")
                time.sleep(1)
        print("Connection successful")

    def pub_msg(self, msg):
        try:
            self.mqtt_client.publish(self.topic, msg, qos=0)
            print("Sent: " + msg)
        except Exception as e:
            print("Exception publish: " + str(e))
            raise

        except Exception as e:
            print('Cannot connect MQTT: ' + str(e))
            raise

    def on_next(self, x):
       data = bytes(json.dumps(x), 'utf-8')
       self.mqtt_client.publish(bytes(self.topic, 'utf-8'), data)

    def disconnect(self):
        self.mqtt_client.disconnect()
