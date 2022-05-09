import subprocess
def scan_network(self):
    devices = subprocess.check_output(['netsh', 'wlan', 'show', 'networks'])
    devices = devices.decode('ascii')
    devices= devices.replace("\r", "")
    for each in devices.split("\n"):
        if each.startswith("SSID"):
            self.list_of_network.add(each)
        