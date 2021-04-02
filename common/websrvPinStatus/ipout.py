import network
print('network config:', network.WLAN(network.STA_IF).ifconfig())
