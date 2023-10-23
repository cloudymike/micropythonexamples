# Very simple example of how to setup network
# Best run interactively
# Enter SSID and PASSWORD here or load file once and then
# run the function with the right parameters

import wlan
import umail

import emailconfig

if __name__ == "__main__":
    mynetwork = wlan.do_connect('wlan_test')


smtp = umail.SMTP('smtp.gmail.com', 587, username=emailconfig.username, password=emailconfig.password)
smtp.to(emailconfig.receiver)
smtp.send("Subject: Test message\n\n This is an example email as would be sent from the ESP32 device. \n Mikael")
smtp.quit()
