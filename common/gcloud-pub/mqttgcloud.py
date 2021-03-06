# Copyright 2019 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from third_party import string
import utime
import ssl
from third_party import rsa
from umqtt.simple import MQTTClient
from ubinascii import b2a_base64
from machine import RTC, Pin
import ujson
import config

MESSAGE = b''

def on_message(topic, message):
    global MESSAGE
    MESSAGE = message
    print((topic,message))


def b42_urlsafe_encode(payload):
    return string.translate(b2a_base64(payload)[:-1].decode('utf-8'),{ ord('+'):'-', ord('/'):'_' })

class MQTTgcloud:
    def __init__(self):
        self.jwt = self.create_jwt(config.google_cloud_config['project_id'], config.jwt_config['private_key'], config.jwt_config['algorithm'], config.jwt_config['token_ttl'])
        self.client = self.get_mqtt_client(config.google_cloud_config['project_id'], config.google_cloud_config['cloud_region'], config.google_cloud_config['registry_id'], config.google_cloud_config['device_id'], self.jwt)

    def get_client(self):
        return(self.client)

    # Wrapper
    def publish(self, message):
        topic = '/devices/{}/{}'.format(config.google_cloud_config['device_id'], 'events')
        self.client.publish(topic.encode('utf-8'), message.encode('utf-8'))

    # Wrapper
    def check_msg(self):
        self.client.check_msg()

    def create_jwt(self, project_id, private_key, algorithm, token_ttl):
        print("Creating JWT...")
        private_key = rsa.PrivateKey(*private_key)

        # Epoch_offset is needed because micropython epoch is 2000-1-1 and unix is 1970-1-1. Adding 946684800 (30 years)
        epoch_offset = 946684800
        claims = {
                # The time that the token was issued at
                'iat': utime.time() + epoch_offset,
                # The time the token expires.
                'exp': utime.time() + epoch_offset + token_ttl,
                # The audience field should always be set to the GCP project id.
                'aud': project_id
        }

        #This only supports RS256 at this time.
        header = { "alg": algorithm, "typ": "JWT" }
        content = b42_urlsafe_encode(ujson.dumps(header).encode('utf-8'))
        content = content + '.' + b42_urlsafe_encode(ujson.dumps(claims).encode('utf-8'))
        signature = b42_urlsafe_encode(rsa.sign(content,private_key,'SHA-256'))
        return content+ '.' + signature #signed JWT

    def get_mqtt_client(self, project_id, cloud_region, registry_id, device_id, jwt):
        """Create our MQTT client. The client_id is a unique string that identifies
        this device. For Google Cloud IoT Core, it must be in the format below."""
        client_id = 'projects/{}/locations/{}/registries/{}/devices/{}'.format(project_id, cloud_region, registry_id, device_id)
        print('Sending message with password {}'.format(jwt))
        client = MQTTClient(client_id.encode('utf-8'),server=config.google_cloud_config['mqtt_bridge_hostname'],port=config.google_cloud_config['mqtt_bridge_port'],user=b'ignored',password=jwt.encode('utf-8'),ssl=True)
        client.set_callback(on_message)
        client.connect()
        client.subscribe('/devices/{}/config'.format(device_id), 1)
        client.subscribe('/devices/{}/commands/#'.format(device_id), 1)
        return client

    def last_msg(self):
        return(str(MESSAGE, 'utf-8'))
