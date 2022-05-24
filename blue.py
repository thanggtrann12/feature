from PyQt5 import QtWidgets, uic
class Blue_Ui_Dialog(QtWidgets.QMainWindow):
    def __init__(self):
        super(Blue_Ui_Dialog, self).__init__()
        uic.loadUi("UI/blue.ui", self)