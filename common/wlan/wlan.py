# Very simple example of how to setup network
# Best run interactively
# Enter SSID and PASSWORD here or load file once and then
# run the function with the right parameters

import network
import wlanconfig
from network import WLAN
from network import STA_IF
import machine

def do_connect():
    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.config(dhcp_hostname='micropythonexamples')
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect(wlanconfig.ESSID,wlanconfig.PASSWORD)
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())

def fresh_connect():
    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if(wlan.isconnected()):
        wlan.disconnect()
    print('connecting to network...')
    wlan.connect(wlanconfig.ESSID,wlanconfig.PASSWORD)
    while not wlan.isconnected():
        pass
    print('network config:', wlan.ifconfig())
    ap_if = network.WLAN(network.AP_IF)
    if ap_if.active():
        ap_if.active(False)
        print("Disconnected AP")


def connect_wifi():

    #wlan = WLAN()
    wlan = network.WLAN(network.STA_IF)
    #nets = wlan.scan()
    if(wlan.isconnected()):
        wlan.disconnect()
    wlan.connect(wlanconfig.ESSID,wlanconfig.PASSWORD)
    while not wlan.isconnected():
        machine.idle() # save power while waiting
        print('WLAN connection succeeded!')
        break
    print("connected:", wlan.ifconfig())
