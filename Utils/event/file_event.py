from setting.file import file_open, file_save, file_import, file_export

def file_button_event(self):
    self.file_open.triggered.connect(lambda: file_open.open_file("filename"))
    self.file_save.triggered.connect(lambda: file_save.save_file("filename"))
    self.file_import.triggered.connect(lambda: file_import.import_file("filename"))
    self.file_export.triggered.connect(lambda: file_export.export_file("filename"))