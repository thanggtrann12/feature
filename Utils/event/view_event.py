from setting.view import dark_mode, light_mode, zoom_in, zoom_out

def view_button_event(self):
    self.view_dark_mode.triggered.connect(lambda: dark_mode.get_dark_mode(self))
    self.view_light_mode.triggered.connect(lambda: light_mode.get_light_mode(self))
    self.view_zoom_in.triggered.connect(lambda: zoom_in.zoom_in(self))
    self.view_zoom_out.triggered.connect(lambda: zoom_out.zoom_out(self))