from PySide6.QtWidgets import QWidget, QScrollArea, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton
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

        # Create alarm edit
        self.alarm_block_edit = QLineEdit()
        self.alarm_block_edit.setPlaceholderText("Alarm title")

        # Create edit button
        self.edit_button = QPushButton("Edit")
        
        # Add widgets to layout
        self.main_layout.addLayout(self.config_layout)
        self.main_layout.addWidget(self.scroll_area)
        self.config_layout.addWidget(self.alarm_block_edit)
        self.config_layout.addWidget(self.edit_button)

        # Connect signals
        self.alarm_block_edit.returnPressed.connect(self.create_alarm)
        self.edit_button.clicked.connect(self.edit_alarms)

        self.set_theme()
    
    def create_alarm(self):
        # Create alarm block
        alarm_title = self.alarm_block_edit.text().strip()
        if not alarm_title:
            alarm_title = "Alarm"
        alarm_block = QAlarmBlock(alarm_title)
        self.alarm_layout.addWidget(alarm_block)
        self.alarm_block_edit.clear()
    
    def edit_alarms(self):
        # Toggle delete button visibility for all alarm blocks
        for i in range(self.alarm_layout.count()):
            alarm_block = self.alarm_layout.itemAt(i).widget()
            # Toggle visibility
            if alarm_block.delete_button.isVisible():
                alarm_block.delete_button.hide()
            else:
                alarm_block.delete_button.show()

    def set_theme(self):
        theme = "alarm"
        self.setProperty("theme", theme)
        self.window.style_manager.apply_theme(theme, self)