from PyQt5 import QtCore, QtGui, QtWidgets, uic
# from setting.network.scan_network import scan_network
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        uic.loadUi("UI/network_window.ui", Dialog)
        self.connect_button =  Dialog.findChild(QtWidgets.QPushButton, "connect_button")
        self.cannel_button = Dialog.findChild(QtWidgets.QPushButton, "cancle_button")
        self.list_of_network = Dialog.findChild(QtWidgets.QListWidget, "list_networks")
        self.scan_button = Dialog.findChild(QtWidgets.QPushButton, "scan_button")
        self.list_of_network.add("asds")
        # self.scan_button.clicked.connect(lambda: scan_network(self))
        # connect the two functions
        