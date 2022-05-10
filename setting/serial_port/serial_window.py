from PyQt5 import QtWidgets, uic
from setting.serial_port import connect_port, scan_port
class Ui_Dialog(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_Dialog, self).__init__()
        uic.loadUi("UI/serial_window.ui", self)
        self.scan_button = self.findChild(QtWidgets.QPushButton, "scan_button")
        self.connect_button = self.findChild(QtWidgets.QPushButton, "connect_button")
        self.port_list = self.findChild(QtWidgets.QComboBox, "port_list")
        self.buad_rate = self.findChild(QtWidgets.QLineEdit, "txt_buad_rate")
        self.scan_button.clicked.connect(lambda: scan_port.scan_port(self))
        self.connect_button.clicked.connect(
            lambda: connect_port.connect_port(self, self.port_list.currentText(), self.buad_rate.text()))
       