from PySide6.QtWidgets import QWidget, QScrollArea, QVBoxLayout, QHBoxLayout, QLineEdit
from PySide6.QtCore import Qt

from .QAlarmBlock import QAlarmBlock

class QAlarmScreen(QWidget):
    def __init__(self, window):
        super().__init__()
        self.window = window
        self.init_ui()

    # Initializes the user interface
    def init_ui(self) -> None:
        # Create main layout
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setAlignment(Qt.AlignCenter)
        self.main_layout.setSpacing(5)
        self.main_layout.setContentsMargins(0, 0, 0, 0)

        # Create alarm config layout
        self.config_layout = QHBoxLayout()
        self.config_layout.setSpacing(5)
        self.config_layout.setContentsMargins(0, 0, 0, 0)

        # Create alarm layout (inside scroll area)
        self.alarm_layout = QVBoxLayout()
        self.alarm_layout.setSpacing(5)
        self.alarm_layout.setContentsMargins(5, 5, 5, 5)
        self.alarm_layout.setAlignment(Qt.AlignTop)

        # Create scroll widget
        self.scroll_widget = QWidget()
        self.scroll_widget.setLayout(self.alarm_layout)

        # Create scroll area
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setWidget(self.scroll_widget)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        # Create widget components
        self.alarm_block_edit = QLineEdit()
        self.alarm_block_edit.setPlaceholderText("Alarm title")
        
        # Add widgets to layout
        self.main_layout.addLayout(self.config_layout)
        self.main_layout.addWidget(self.scroll_area)
        self.config_layout.addWidget(self.alarm_block_edit)

        # Connect signals
        self.alarm_block_edit.returnPressed.connect(self.create_alarm)

        self.set_theme()
    
    def create_alarm(self):
        # Create alarm block
        alarm_block = QAlarmBlock(self.alarm_block_edit.text())
        self.alarm_layout.addWidget(alarm_block)
        self.alarm_block_edit.clear()

    def set_theme(self):
        theme = "alarm"
        self.setProperty("theme", theme)
        self.window.style_manager.apply_theme(theme, self)