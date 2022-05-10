import os
import time
from Utils.msg_pop_up import msgPopUp
from setting.network.ping import ping


def connect_network(self):
    timeout = 4
    result = os.system(f'''cmd /c"netsh wlan connect name={self.txt_ssid.text()}"''')
    if result == 0:
        while timeout > 0:
            result_ping = ping("google.com")
            if result_ping == True:
                msgPopUp("Connected", "Connected to network successfully.")
                break
            else:
                timeout -= 1
                time.sleep(2)
    else:   
        msgPopUp( "Failed to request to the network!", "Error!")
