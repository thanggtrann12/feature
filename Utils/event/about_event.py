from setting.about import about_author, about_IAC
def about_button_event(self):
    self.about_IAC.triggered.connect(lambda: about_IAC.IAC())
    self.about_author.triggered.connect(lambda: about_author.author())