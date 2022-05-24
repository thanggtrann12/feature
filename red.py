from PyQt5 import QtWidgets, uic
class Red_Ui_Dialog(QtWidgets.QMainWindow):
    def __init__(self):
        super(Red_Ui_Dialog, self).__init__()
        uic.loadUi("UI/red.ui", self)
        self.te = self.findChild(QtWidgets.QLabel, "checkpoint_1")
    
    def change(self, text):
        self.te.setText(text)