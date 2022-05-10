from PyQt5 import QtWidgets, uic
from setting.network.scan_network import scan_network
from setting.network.connect_network import connect_network


class Ui_Dialog(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_Dialog, self).__init__()
        uic.loadUi("UI/network_window.ui", self)
        self.txt_ssid = self.findChild(QtWidgets.QLineEdit, "txt_ssid")
        self.txt_password = self.findChild(QtWidgets.QLineEdit, "txt_password")
        self.progress_bar = self.findChild(
            QtWidgets.QProgressBar, "progressBar")
        self.progress_bar.setVisible(False)
        self.connect_button = self.findChild(
            QtWidgets.QPushButton, "connect_button")
        self.cannel_button = self.findChild(
            QtWidgets.QPushButton, "cancle_button")
        self.list_of_network = self.findChild(
            QtWidgets.QListWidget, "list_networks")
        self.scan_button = self.findChild(QtWidgets.QPushButton, "scan_button")
        self.scan_button.clicked.connect(lambda: scan_network(self))
        self.list_of_network.itemDoubleClicked.connect(self.set_ssid)
        self.connect_button.clicked.connect(lambda: connect_network(self))

    def set_ssid(self):
        ssid_txt = self.list_of_network.currentItem().text()
        index = ssid_txt.index(":")
        self.txt_ssid.setText(ssid_txt[index+1:])