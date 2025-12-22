from PySide6.QtWidgets import QWidget, QHBoxLayout, QFrame

class QSwitchBar(QFrame):
    def __init__(self, window):
        super().__init__(window)
        self.init_meta()
        self.init_vars(window)
        self.init_ui()
        self.setFixedHeight(25)
        self.setMouseTracking(True)
    
    def init_meta(self) -> None:
        self.setObjectName("SwitchBar")
        self.setProperty("theme", "main")
        self.setAutoFillBackground(True)
        self.setFrameShape(QFrame.NoFrame)

    def init_vars(self, window) -> None:
        self.window = window

    def init_ui(self) -> None:
        # Create layouts
        layout = QHBoxLayout(self)
        layout.setContentsMargins(5, 5, 5, 5)
        layout.setSpacing(10)
        
        buttons_layout = QHBoxLayout()
        buttons_layout.setContentsMargins(0, 0, 0, 0)
        title_layout = QHBoxLayout()
        title_layout.setContentsMargins(0, 0, 0, 0)

        layout.addLayout(buttons_layout)
        layout.addLayout(title_layout)

        # Create buttons
        

        # Modify button
        

        # Add buttons to layout
        

        self.set_theme("main")
    
    def set_theme(self, theme: str) -> None:
        # Set theme on this widget
        self.setProperty("theme", theme)

        # Re-polish self
        self.style().unpolish(self)
        self.style().polish(self)
        self.update()

        # Apply theme to children
        for child in self.findChildren(QWidget):
            child.setProperty("theme", theme)
            child.style().unpolish(child)
            child.style().polish(child)
            child.update()