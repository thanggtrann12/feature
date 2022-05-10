from PyQt5 import QtWidgets, uic
class Ui_Dialog(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_Dialog, self).__init__()
        uic.loadUi("UI/topic_window.ui", self)