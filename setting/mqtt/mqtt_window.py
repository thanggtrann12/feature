from PyQt5 import QtWidgets, uic
from setting.mqtt.client.broker import set_info, get_info
from setting.mqtt.client.topic_window import Ui_Dialog as Form

class Ui_Dialog(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_Dialog, self).__init__()
        uic.loadUi("UI/mqtt_window.ui", self)
        self.window = None
        self.txt_host = self.findChild(QtWidgets.QLineEdit, "txt_host")
        self.txt_port = self.findChild(QtWidgets.QLineEdit, "txt_port")
        self.txt_username = self.findChild(QtWidgets.QLineEdit, "txt_username")
        self.txt_password = self.findChild(QtWidgets.QLineEdit, "txt_password")
        self.txt_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.retain_checkbox = self.findChild(
            QtWidgets.QCheckBox, "retain_checkbox")
        self.set_button = self.findChild(QtWidgets.QPushButton, "set_button")
        self.get_button = self.findChild(QtWidgets.QPushButton, "get_button")
        self.topic_button = self.findChild(
            QtWidgets.QPushButton, "topic_button")
        self.defaut_button = self.findChild(QtWidgets.QCheckBox, "default_button")
        self.percent = self.findChild(QtWidgets.QProgressBar, "progressBar")
        self.percent.setVisible(False)
        self.set_button.clicked.connect(lambda: set_info(self, self.txt_host.text(), self.txt_port.text(
        ), self.txt_username.text(), self.txt_password.text(), self.retain_checkbox.isChecked()))
        self.get_button.clicked.connect(lambda: get_info(self))
        self.topic_button.clicked.connect(self.open_dialog)


    def close(self):
        self.close()

    


    def open_dialog(self):
        if self.window is None:
            self.window = Form()
        self.window.show()

