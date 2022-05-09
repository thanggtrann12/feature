from PyQt5 import QtCore, QtWidgets
import sys


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Should close")
        QtCore.QTimer.singleShot(0, self.close)


app = QtWidgets.QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec_()
