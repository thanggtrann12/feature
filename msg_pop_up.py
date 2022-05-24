from PyQt5 import QtWidgets


def msgPopUp(msg, title):
    msgBox = QtWidgets.QMessageBox()
    msgBox.setText(msg)
    msgBox.setWindowTitle(title)
    msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
    msgBox.exec_()
