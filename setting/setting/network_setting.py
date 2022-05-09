from setting.network.network_window import Ui_Dialog as Form
from PyQt5 import QtWidgets


def open_dialog(self):
    dialog = QtWidgets.QDialog()
    dialog.ui = Form()
    dialog.ui.setupUi(dialog)
    dialog.exec_()
    dialog.show()  
def network_setting(self):
    open_dialog(self)