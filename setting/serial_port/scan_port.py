

def scan_port(self):
    """Scan all serial port and return a list of serial port name."""
    print("Scanning serial port...")
    import serial.tools.list_ports
    self.port_list.clear()
    ports = serial.tools.list_ports.comports()
    for port, desc, _ in sorted(ports):
        portDetail = "{}: {}".format(port, desc)
        self.port_list.addItem(portDetail)