from PyQt5 import QtWidgets


def component(self):
    
    self.add_button = self.findChild(QtWidgets.QPushButton, "addBtn")
    self.delete_button = self.findChild(QtWidgets.QPushButton, "RmvBtn")
    self.show_button = self.findChild(QtWidgets.QPushButton, "shwBtn")
    self.stop_button = self.findChild(QtWidgets.QPushButton, "stpBtn")
    
