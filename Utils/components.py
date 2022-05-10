from PyQt5 import QtWidgets


def component_factory(self):
    self.file_open = self.findChild(QtWidgets.QAction, "actionOpen")
    self.file_open.setShortcut("Ctrl+O")

    self.file_save = self.findChild(QtWidgets.QAction, "actionSave")
    self.file_save.setShortcut("Ctrl+S")

    self.file_import = self.findChild(QtWidgets.QAction, "actionImport")
    self.file_import.setShortcut("Ctrl+I")

    self.file_export = self.findChild(QtWidgets.QAction, "actionExport_3")
    self.file_export.setShortcut("Ctrl+E")
    
    self.setting_mqtt = self.findChild(QtWidgets.QAction, "actionBrokerInfo")
    self.setting_network = self.findChild(QtWidgets.QAction, "actionNetwork")
    self.setting_serial = self.findChild(QtWidgets.QAction, "actionSerial_2")
    
    self.about_IAC = self.findChild(QtWidgets.QAction, "actionAbout_IAC")
    self.about_author = self.findChild(QtWidgets.QAction, "actionAuthor")

    self.view_dark_mode = self.findChild(QtWidgets.QAction, "actionDark_Mode")
    self.view_light_mode = self.findChild(
        QtWidgets.QAction, "actionLight_Mode_default")
    self.view_zoom_in = self.findChild(QtWidgets.QAction, "actionZoom_In")
    self.view_zoom_out = self.findChild(QtWidgets.QAction, "actionZoom_Out")

    self.data_view = self.findChild(QtWidgets.QAction, "team_container")

    self.quick_guide = self.findChild(QtWidgets.QAction, "actionQuick_Guide")

    self.fanpage = self.findChild(QtWidgets.QAction, "actionFanpage")

    
