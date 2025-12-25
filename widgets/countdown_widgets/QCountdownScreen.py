from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton
from PySide6.QtCore import Qt, QTime
from .QCountdownTimer import QCountdownTimer

from widgets.countdown_widgets.QTimeRange import QTimeRange

class QCountdownScreen(QWidget):
    def __init__(self, window):
        super().__init__()
        self.window = window
        self.init_vars()
        self.init_ui()
    
    # Initialize all needed variables
    def init_vars(self) -> None:
        self.countdown = QCountdownTimer()

    # Initializes the user interface
    def init_ui(self) -> None:
        # Create layout
        self.layout = QVBoxLayout(self)
        self.layout.setAlignment(Qt.AlignCenter)
        self.layout.setSpacing(5)
        self.layout.setContentsMargins(0, 0, 0, 0)

        # Create widget components
        self.countdownRange: QTimeRange = QTimeRange()
        self.countdownButton: QPushButton = QPushButton(text="Start", objectName="CountdownButton")
        
        # Add widgets to layout
        self.layout.addWidget(self.countdownRange)
        self.layout.addWidget(self.countdownButton)

        # Connect signals
        self.countdownButton.clicked.connect(self.toggle_countdown)
        self.countdown.time_changed.connect(self.update_label)

        self.set_theme()

    # Toggles the countdown
    def toggle_countdown(self) -> None:
        self.countdown.toggle(self.countdownRange.time())
        self.countdownButton.setText("Pause" if self.countdown.running else "Start")

    # Updates countdown label
    def update_label(self, time: QTime) -> None:
        self.countdownRange.setTime(time)
    
    def set_theme(self):
        theme = "countdown"
        self.setProperty("theme", theme)
        self.window.style_manager.apply_theme(theme, self)