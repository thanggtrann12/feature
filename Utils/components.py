from PyQt5 import QtWidgets

def component_factory(self):
    self.file_open = self.findChild(QtWidgets.QAction, "actionOpen")
    self.file_save = self.findChild(QtWidgets.QAction, "actionSave")
    self.file_import = self.findChild(QtWidgets.QAction, "actionImport")
    self.file_export = self.findChild(QtWidgets.QAction, "actionExport_3")

    self.setting_mqtt = self.findChild(QtWidgets.QAction, "actionMqtt")
    self.setting_network = self.findChild(QtWidgets.QAction, "actionNetwork")

    self.help_about = self.findChild(QtWidgets.QAction, "actionAbout_IAC")
    self.help_author = self.findChild(QtWidgets.QAction, "actionAuthor")

    self.view_dark_mode = self.findChild(QtWidgets.QAction, "actionDark_Mode")
    self.view_light_mode = self.findChild(QtWidgets.QAction, "actionLight_Mode_default")
    self.view_zoom_in = self.findChild(QtWidgets.QAction, "actionZoom_In")
    self.view_zoom_out = self.findChild(QtWidgets.QAction, "actionZoom_Out")

    self.data_view = self.findChild(QtWidgets.QAction, "team_container")