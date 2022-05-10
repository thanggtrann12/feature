from PyQt5 import QtWidgets
import sys
import qdarktheme
from setting.view.light_mode import light_mode_flags
dark_mode_flags = False

def get_dark_mode(self):
    self.setStyleSheet(qdarktheme.load_stylesheet())
    global dark_mode_flags
    dark_mode_flags = True