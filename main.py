from random import randint
from threading import Thread
from PyQt5 import QtWidgets, QtGui, uic
import sys
from PcToArduino import PcToArduino
from dark_mode import set_dark_mode, set_light_mode
from components import component
from red import Red_Ui_Dialog 
from blue import Blue_Ui_Dialog
from PyQt5.QtCore import *
_serialConnection = None


class Ui(QtWidgets.QMainWindow):
    
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi("UI/main.ui", self)
        component(self)        
        self.RedWindow = Red_Ui_Dialog()
        self.BlueWindow = Blue_Ui_Dialog()
        self.mode  = None
        if self.mode is not None:
          self.mode = set_dark_mode(self)
        self.show_button.clicked.connect(self.open)
        self.stop_button.clicked.connect(self.close)
        timer = QTimer(self)
        timer.timeout.connect(self.threading)
        timer.start(1)

    def threading(self):
        self.RedWindow.change(str(randint(1, 100)))
        
    def open_dialog(self):
        
        self.RedWindow.show()
        self.BlueWindow.show()

    def close(self) :
        self.RedWindow.close()
        self.BlueWindow.close()

    def open(self):
        self.open_dialog()

    def closeEvent(self, event):
        msg = QtWidgets.QMessageBox()
        msg.setText("Are you sure you want to exit?")
        msg.setWindowTitle("Exit")
        msg.setWindowIcon(QtGui.QIcon("./icon/warning.png"))
        msg.setIcon(QtWidgets.QMessageBox.Question)
        msg.setStandardButtons(QtWidgets.QMessageBox.Yes |
                               QtWidgets.QMessageBox.No)
        
        reply = msg.exec()
        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
            
            sys.exit()    
        else:
            event.ignore()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    window.show()
    app.exec_()
