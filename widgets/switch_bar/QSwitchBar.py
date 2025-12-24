from PySide6.QtWidgets import QWidget, QHBoxLayout, QFrame, QPushButton

# Screens
from widgets.stopwatch_widgets.QStopwatchScreen import QStopwatchScreen
from widgets.countdown_widgets.QCountdownScreen import QCountdownScreen

class QSwitchBar(QFrame):
    def __init__(self, window):
        super().__init__(window)
        self.init_meta()
        self.init_vars(window)
        self.init_ui()
        self.setFixedHeight(30)
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
        mainLayout = QHBoxLayout(self)
        mainLayout.setContentsMargins(5, 5, 5, 5)
        mainLayout.setSpacing(10)
        
        buttonsLayout = QHBoxLayout()
        buttonsLayout.setContentsMargins(0, 0, 0, 0)
        mainLayout.addLayout(buttonsLayout)

        # Create buttons
        self.stopwatchSwitchButton = QPushButton(text="Stopwatch", objectName="StopwatchSwitchButton")
        self.countdownSwitchButton = QPushButton(text="Countdown", objectName="CountdownSwitchButton")

        # Modify button
        self.stopwatchSwitchButton.setDisabled(True)
        for btn in [self.stopwatchSwitchButton, self.countdownSwitchButton]:
            btn.setFixedSize(100, 20)

        # Add buttons to layout
        buttonsLayout.addWidget(self.stopwatchSwitchButton)
        buttonsLayout.addWidget(self.countdownSwitchButton)

        # Connect signals
        self.stopwatchSwitchButton.clicked.connect(self.stopwatch_switch)
        self.countdownSwitchButton.clicked.connect(self.countdown_switch)

        self.set_theme("main")
    
    def stopwatch_switch(self) -> None:
        self.window.screen_manager.switch_to(QStopwatchScreen)
        self.stopwatchSwitchButton.setDisabled(True)
        self.countdownSwitchButton.setDisabled(False)

    def countdown_switch(self) -> None:
        self.window.screen_manager.switch_to(QCountdownScreen)
        self.countdownSwitchButton.setDisabled(True)
        self.stopwatchSwitchButton.setDisabled(False)
    
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