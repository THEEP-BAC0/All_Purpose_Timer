class ScreenManager():
    def __init__(self, window):
        self.window = window
        self.current_screen = None

    def switch_to(self, widget_class):
        self.deleteScreen()
        self.current_screen = widget_class(self.window)
        self.window.contentLayout.addWidget(self.current_screen)
    
    # Deletes screen
    def deleteScreen(self):
        if not self.current_screen == None:
            self.window.contentLayout.removeWidget(self.current_screen)
            self.current_screen.deleteLater()