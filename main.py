from PyQt5 import QtWidgets, QtGui, uic
import sys
from Utils.components import component_factory
from Utils.event import file_event, setting_event, help_event, view_event
import qdarktheme
from setting.view import dark_mode, light_mode, zoom_in, zoom_out
from setting.network.ping import ping
class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi("UI/main.ui", self)
        component_factory(self)
        self.window = None
        if (ping('google.com') != True):
            self.statusBar().showMessage("Network is not connected. Go to setting - > network to connect network.")
        else:
            self.statusBar().showMessage("Network is connected.")
        file_event.file_button_event(self)
        setting_event.setting_button_event(self)
        help_event.help_button_event(self)
        view_event.view_button_event(self)
        self.show()
        

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
        else:
            event.ignore()


app = QtWidgets.QApplication(sys.argv)
window = Ui()
window.show()
app.exec_()
