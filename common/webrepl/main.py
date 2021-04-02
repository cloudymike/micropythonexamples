# webrepl_setup may have to be run first

#import webrepl_setup


import wlan
import webrepl

wlan.do_connect()
password = 'MyPass'
webrepl.start(password=password)
print("Password is {}".format(password))
