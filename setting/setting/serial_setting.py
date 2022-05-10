from setting.serial_port.serial_window import Ui_Dialog as Form


def open_dialog(self):
    if self.window is None:
        self.window = Form()
    self.window.show()


def serial_setting(self):
    open_dialog(self)