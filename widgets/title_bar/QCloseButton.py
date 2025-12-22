from PySide6.QtWidgets import QPushButton

class QCloseButton(QPushButton):
    def __init__(self, parent = None):
        super().__init__("x")
        self.parent = parent
        self.setObjectName("ExitButton")
        self.setProperty("theme", "main")
        self.clicked.connect(self.parent.window.close)