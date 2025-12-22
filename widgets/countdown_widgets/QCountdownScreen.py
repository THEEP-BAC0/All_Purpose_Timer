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
        self.stopwatch = QCountdownTimer()

    # Initializes the user interface
    def init_ui(self) -> None:
        # Create layout
        self.layout = QVBoxLayout(self)
        self.layout.setAlignment(Qt.AlignCenter)
        self.layout.setSpacing(5)
        self.layout.setContentsMargins(0, 0, 0, 0)

        # Create widget components
        self.stopwatchLabel: QLabel = QLabel("00:00:00")
        self.stopwatchButton: QPushButton = QPushButton("Start")
        
        # Modify widgets before adding
        self.stopwatchLabel.setObjectName("StopwatchLabel")
        self.stopwatchButton.setObjectName("StopwatchButton")
        
        # Add widgets to layout
        self.layout.addWidget(self.stopwatchLabel)
        self.layout.addWidget(self.stopwatchButton)

        # Connect signals
        self.stopwatchButton.clicked.connect(self.toggle_stopwatch)
        self.stopwatch.time_changed.connect(self.update_label)

        self.set_theme()

    # Toggles the countdown
    def toggle_countdown(self) -> None:
        self.stopwatch.toggle()
        self.stopwatchButton.setText("Stop" if self.stopwatch.running else "Start")

    # Updates stopwatch label
    def update_label(self, text) -> None:
        self.stopwatchLabel.setText(text)
    
    def set_theme(self):
        theme = "stopwatch"
        self.setProperty("theme", theme)
        self.window.style_manager.apply_theme(theme, self)