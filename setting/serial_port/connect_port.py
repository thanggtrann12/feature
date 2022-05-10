from email.policy import default
import serial
from Utils.msg_pop_up import msgPopUp

default_buad_rate_list = [
    100,
    300,
    600,
    1200,
    2400,
    4800,
    9600,
    14400,
    19200,
    38400,
    57600,
    115200,
    230400,
    460800,
    921600
]

default_buad_rate = 9600

def connect_port(self, port_name, baud_rate):
    """Read data from serial port."""
    if port_name != None:
        if baud_rate == "":
            baud_rate = int(default_buad_rate)
            self.buad_rate.setText(str(default_buad_rate))
        if int(baud_rate) not in default_buad_rate_list:
            msgPopUp("Baud rate is not supported. Please choose another one.", "Warning")
        else:
            try:
                serial_port = serial.Serial(port_name, int(baud_rate), timeout=1)
                if serial_port.isOpen():
                    self.statusBar().showMessage("Serial port is connected.")
                    msgPopUp("Serial port is connected.", "Info")
                
            except serial.SerialException as err:
                pass
    else:
        msgPopUp("Port name or baud rate is not defined.", "Error")