import os
from Utils.msg_pop_up import msgPopUp


def connect_network(name, SSID):
    command = "netsh wlan connect name=\""+name + \
        "\" ssid=\""+SSID+"\" interface=Wi-Fi"
    msgPopUp(command, "Connecting...")
    os.system(command)
