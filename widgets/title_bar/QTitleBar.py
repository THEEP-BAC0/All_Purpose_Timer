from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel, QFrame

from widgets.window.WindowDragger import WindowDragger
from widgets.title_bar.QCloseButton import QCloseButton
from widgets.title_bar.QMinimizeButton import QMinimizeButton

class QTitleBar(QFrame):
    def __init__(self, title: str, window=None):
        super().__init__(window)
        self.init_meta()
        self.init_vars(title, window)
        self.init_ui()
        self.setFixedHeight(25)
        self.setMouseTracking(True)
    
    def init_meta(self) -> None:
        self.setObjectName("TitleBar")
        self.setProperty("theme", "main")
        self.setAutoFillBackground(True)
        self.setFrameShape(QFrame.NoFrame)

    def init_vars(self, title: str, window) -> None:
        self.title = title
        self.window = window
        self.dragger = WindowDragger(self.window, self)

    def init_ui(self):
        # Title label
        self.title_label = QLabel("All Purpose Timer", objectName="Title")
        if self.title: self.title_label.setText(self.title)
        self.title_label.setProperty("theme", "main")

        # Create buttons
        self.btn_close = QCloseButton(self)
        self.btn_min = QMinimizeButton(self)

        # Modify button
        for b in (self.btn_close, self.btn_min): b.setFixedSize(14, 14)
        
        # Create layouts
        main_layout = QHBoxLayout(self)
        main_layout.setContentsMargins(5, 5, 5, 5)
        main_layout.setSpacing(10)

        buttons_layout = QHBoxLayout()
        buttons_layout.setContentsMargins(0, 0, 0, 0)
        title_layout = QHBoxLayout()
        title_layout.setContentsMargins(0, 0, 0, 0)

        main_layout.addLayout(buttons_layout)
        main_layout.addLayout(title_layout)

        # Add widgets to layout
        title_layout.addWidget(self.title_label)
        buttons_layout.addWidget(self.btn_close)
        buttons_layout.addWidget(self.btn_min)

        self.set_theme("main")
    
    def set_theme(self, theme: str):
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

    def mousePressEvent(self, event):
        self.dragger.start_drag(event)

    def mouseMoveEvent(self, event):
        self.dragger.drag(event)

    def mouseReleaseEvent(self, event):
        self.dragger.end_drag(event)