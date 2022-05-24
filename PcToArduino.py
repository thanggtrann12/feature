from time import sleep
import serial
import serial.tools.list_ports

class PcToArduino:
    
    def __init__(self, port_name = None, buad_rate = None, timeout = 1):
        self.port_name = port_name
        self.buad_rate = buad_rate
        self.timeout = 5
        if self.port_name is not None:
            self.connection = serial.Serial(self.port_name, self.buad_rate, timeout=self.timeout)

  
    def scanForPort(self):
        if self.port_name == None:
            try:
                print("Scanning serial port...")
                ports = serial.tools.list_ports.comports()
                for port, desc, _ in sorted(ports):
                    portDetail = "{}: {}".format(port, desc)
                    print(portDetail )
            except serial.SerialException as err:
                pass

    def connectPort(self, port_name, buad_rate):
        self.port_name = port_name
        self.buad_rate = buad_rate
        self.connection = serial.Serial(self.port_name, self.buad_rate)
        if self.connection.isOpen():
            print("Connected to {}".format(self.port_name))
            return True
        else:
            print("Failed to connect to {}".format(self.port_name))
        return False

    def closeConnection(self):
        print("closed")

    def readDataFromSerial(self):
        try:
            return self.connection.readline().rstrip().decode()
        except Exception as err:
            pass

    def sendDataToSerial(self, data):
        self.connection.write(data.encode())
        self.connection.flush()
        return self.waitForResponse()
    

    def waitForResponse(self):
        while self.timeout > 0:
            data = self.connection.readline().rstrip().decode()
            if "OK" in data:
                self.timeout = 5
                return True
            sleep(0.3)
            self.timeout -= 1
