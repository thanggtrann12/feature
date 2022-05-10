import subprocess
import time
from Utils.msg_pop_up import msgPopUp


def scan_network(self):
    network_flag = False
    devices = subprocess.check_output(['netsh', 'wlan', 'show', 'networks'])
    devices = devices.decode('ascii')
    devices = devices.replace("\r", "")
    self.progress_bar.setVisible(True)
    for percent in range(0, len(devices.split("\n"))+1):
        self.progress_bar.setValue(int((percent/len(devices.split("\n")))*100))
        if percent == len(devices.split("\n")):
            self.progress_bar.setVisible(False)
        time.sleep(1)
    for each in devices.split("\n"):
        if each.startswith("SSID"):
            network_flag = True
            self.list_of_network.addItem(each)
        else:
            network_flag = network_flag
    if network_flag == False:
        msgPopUp("No network found!!! Try again", "Failed")
