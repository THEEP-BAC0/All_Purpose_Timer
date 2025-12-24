from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from PySide6.QtCore import Qt
from .QCountdownTimer import QCountdownTimer

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
        self.countdownLabel: QLabel = QLabel(text="00:00:00", objectName="CountdownLabel")
        self.countdownButton: QPushButton = QPushButton(text="Start", objectName="CountdownButton")
        
        # Modify widgets before adding
        
        # Add widgets to layout
        self.layout.addWidget(self.countdownLabel)
        self.layout.addWidget(self.countdownButton)

        # Connect signals
        self.countdownButton.clicked.connect(self.toggle_countdown)
        self.countdown.time_changed.connect(self.update_label)

        self.set_theme()

    # Toggles the countdown
    def toggle_countdown(self) -> None:
        self.countdown.toggle()
        self.countdownButton.setText("Stop" if self.countdown.running else "Start")

    # Updates countdown label
    def update_label(self, text) -> None:
        self.countdownLabel.setText(text)
    
    def set_theme(self):
        theme = "countdown"
        self.setProperty("theme", theme)
        self.window.style_manager.apply_theme(theme, self)