from PyQt5 import QtWidgets
import sys
import qdarktheme

def set_dark_mode(self):
    self.setStyleSheet(qdarktheme.load_stylesheet())
    return "dark"
    
def set_light_mode(self):
    self.setStyleSheet(qdarktheme.load_stylesheet("light"))
    return "light"
