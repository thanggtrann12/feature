from PyQt5 import QtWidgets
import sys
import qdarktheme
light_mode_flags = False
def get_light_mode(self):
    self.setStyleSheet(qdarktheme.load_stylesheet("light"))
    global light_mode_flags
    light_mode_flags = True