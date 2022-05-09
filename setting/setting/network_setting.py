from setting.network.network_window import Ui_Dialog as Form


def open_dialog(self):
    if self.window is None:
        self.window = Form()
    self.window.show()


def network_setting(self):
    open_dialog(self)
