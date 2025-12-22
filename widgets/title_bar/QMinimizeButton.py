from PySide6.QtWidgets import QPushButton

class QMinimizeButton(QPushButton):
    def __init__(self, parent = None):
        super().__init__("-")
        self.parent = parent
        self.setObjectName("MinimizeButton")
        self.setProperty("theme", "main")
        self.clicked.connect(self.parent.window.showMinimized)