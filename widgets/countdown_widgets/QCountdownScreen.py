from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton
from PySide6.QtCore import Qt, QTime
from ..timers.QCountdownTimer import QCountdownTimer

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
        # Create widget components
        self.countdown_range: QTimeRange = QTimeRange()
        self.countdown_button: QPushButton = QPushButton(text="Start", objectName="CountdownButton")
        
        # Create layout
        self.layout = QVBoxLayout(self)
        self.layout.setAlignment(Qt.AlignCenter)
        self.layout.setSpacing(5)
        self.layout.setContentsMargins(0, 0, 0, 0)

        # Add widgets to layout
        self.layout.addWidget(self.countdown_range)
        self.layout.addWidget(self.countdown_button)
        
        # Connect signals
        self.countdown_button.clicked.connect(self.toggle_countdown)
        self.countdown.time_changed.connect(self.update_label)

        self.set_theme()

    # Toggles the countdown
    def toggle_countdown(self) -> None:
        self.countdown.toggle(self.countdown_range.time())
        self.countdown_button.setText("Pause" if self.countdown.running else "Start")

    # Updates countdown label
    def update_label(self, time: QTime) -> None:
        self.countdown_range.setTime(time)
    
    def set_theme(self):
        theme = "countdown"
        self.setProperty("theme", theme)
        self.window.style_manager.apply_theme(theme, self)