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
import machine
import esp32
import utime

from machine import RTC
import ntptime
import ujson
import wlan
import LED


import mqttgcloud

LED.LED.value(1)


def set_time():
    ntptime.settime()
    tm = utime.localtime()
    tm = tm[0:3] + (0,) + tm[3:6] + (0,)
    machine.RTC().datetime(tm)
    print('current time: {}'.format(utime.localtime()))


wlan.do_connect()
#Need to be connected to the internet before setting the local RTC.
set_time()

m = mqttgcloud.MQTTgcloud()
client = m.get_client()

while True:
    message = {
        "hall": esp32.hall_sensor(),
        "temp": esp32.raw_temperature()
    }
    print("Publishing message "+str(ujson.dumps(message)))
    LED.LED.value(1)
    m.publish(ujson.dumps(message))
    LED.LED.value(0)

    m.check_msg() # Check for new messages on subscription
    print('Last message: {}'.format(m.last_msg()))
    utime.sleep(10)  # Delay for 10 seconds.
