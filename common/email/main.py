# Very simple example of how to setup network
# Best run interactively
# Enter SSID and PASSWORD here or load file once and then
# run the function with the right parameters

import wlan
import umail

if __name__ == "__main__":
    mynetwork = wlan.do_connect('wlan_test')


smtp = umail.SMTP('smtp.gmail.com', 587, username='my@gmail.com', password='mypassword')
smtp.to('someones@gmail.com')
smtp.send("This is an example.")
smtp.quit()
