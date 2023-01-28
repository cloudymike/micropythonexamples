# Very simple example of how to setup network
# Best run interactively
# Enter SSID and PASSWORD here or load file once and then
# run the function with the right parameters

import network
import wlanconfig
import machine
import time

def do_connect(hostname='micropythonexamples'):
    nic = network.WLAN(network.STA_IF)
    nic.active(True)
    nic.config(dhcp_hostname=hostname)
    if not nic.isconnected():
        print('connecting to network...')
        while not nic.isconnected():
            nic.connect(wlanconfig.ESSID,wlanconfig.PASSWORD)
            time.sleep_ms(500)

    print('network config:', nic.ifconfig())
    return(nic)

# Remove old connection if exist before reconnecting
def fresh_connect(hostname='micropythonexamples'):
    nic = network.WLAN(network.STA_IF)
    nic.active(True)
    if(nic.isconnected()):
        nic.disconnect()
    print('connecting to network...')
    nic = do_connect(hostname)
    return(nic)
