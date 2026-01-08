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
        # Create widget components
        self.stopwatch_label: QLabel = QLabel(text="00:00:00", objectName="StopwatchLabel")
        self.stopwatch_button: QPushButton = QPushButton(text="Start", objectName="StopwatchButton")
        self.restart_button: QPushButton = QPushButton(text="Restart", objectName="RestartButton")

        # Create layout
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setAlignment(Qt.AlignCenter)
        self.main_layout.setSpacing(5)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        
        # Add widgets to layout
        self.main_layout.addWidget(self.stopwatch_label)
        self.main_layout.addWidget(self.stopwatch_button)
        self.main_layout.addWidget(self.restart_button)

        # Connect signals
        self.stopwatch_button.clicked.connect(self.toggle_stopwatch)
        self.stopwatch.time_changed.connect(self.update_label)
        self.restart_button.clicked.connect(lambda : self.stopwatch.reset_time())

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