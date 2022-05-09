from setting.help import help_about, help_author
def help_button_event(self):
    self.help_about.triggered.connect(lambda: help_about.about())
    self.help_author.triggered.connect(lambda: help_author.author())