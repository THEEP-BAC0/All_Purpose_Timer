from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from PySide6.QtCore import Qt
from ..timers.QStopwatch import QStopwatch

class QStopwatchScreen(QWidget):
    def __init__(self, window):
        super().__init__()
        self.window = window
        self.init_vars()
        self.init_ui()
    
    # Initialize all needed variables
    def init_vars(self) -> None:
        self.stopwatch = QStopwatch()

    # Initializes the user interface
    def init_ui(self) -> None:
        # Create layout
        self.layout = QVBoxLayout(self)
        self.layout.setAlignment(Qt.AlignCenter)
        self.layout.setSpacing(5)
        self.layout.setContentsMargins(0, 0, 0, 0)

        # Create widget components
        self.stopwatchLabel: QLabel = QLabel(text="00:00:00", objectName="StopwatchLabel")
        self.stopwatchButton: QPushButton = QPushButton(text="Start", objectName="StopwatchButton")
        self.restartButton: QPushButton = QPushButton(text="Restart", objectName="RestartButton")
        
        # Add widgets to layout
        self.layout.addWidget(self.stopwatchLabel)
        self.layout.addWidget(self.stopwatchButton)
        self.layout.addWidget(self.restartButton)

        # Connect signals
        self.stopwatchButton.clicked.connect(self.toggle_stopwatch)
        self.stopwatch.time_changed.connect(self.update_label)
        self.restartButton.clicked.connect(lambda : self.stopwatch.reset_time())

        self.set_theme()

    # Toggles the stopwatch
    def toggle_stopwatch(self) -> None:
        self.stopwatch.toggle()
        self.stopwatchButton.setText("Stop" if self.stopwatch.running else "Start")

    # Updates stopwatch label
    def update_label(self, text) -> None:
        self.stopwatchLabel.setText(text)
    
    def set_theme(self):
        theme = "stopwatch"
        self.setProperty("theme", theme)
        self.window.style_manager.apply_theme(theme, self)