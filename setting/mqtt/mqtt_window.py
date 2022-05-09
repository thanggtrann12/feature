from PyQt5 import QtWidgets, uic
from setting.mqtt.client.broker import set_info, get_info


class Ui_Dialog(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_Dialog, self).__init__()
        uic.loadUi("UI/mqtt_window.ui", self)
        self.txt_host = self.findChild(QtWidgets.QLineEdit, "txt_host")
        self.txt_port = self.findChild(QtWidgets.QLineEdit, "txt_port")
        self.txt_username = self.findChild(QtWidgets.QLineEdit, "txt_username")
        self.txt_password = self.findChild(QtWidgets.QLineEdit, "txt_password")
        self.retain_checkbox = self.findChild(
            QtWidgets.QCheckBox, "retain_checkbox")
        self.set_button = self.findChild(QtWidgets.QPushButton, "set_button")
        self.get_button = self.findChild(QtWidgets.QPushButton, "get_button")
        self.cancel_button = self.findChild(
            QtWidgets.QPushButton, "cancle_button")
        self.set_button.clicked.connect(lambda: set_info(self.txt_host.text(), self.txt_port.text(
        ), self.txt_username.text(), self.txt_password.text(), self.retain_checkbox.isChecked()))
        self.get_button.clicked.connect(lambda: get_info())
        # self.cancel_button.clicked.connect(self.close)

    def close(self):
        self.close()
