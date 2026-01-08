from PySide6.QtWidgets import QWidget, QLineEdit, QTimeEdit, QHBoxLayout, QVBoxLayout, QPushButton, QAbstractSpinBox
from PySide6.QtCore import Qt, QTime

from .QAlarmTracker import QAlarmTracker

class QAlarmBlock(QWidget):
    def __init__(self, title: str = "Alarm"):
        super().__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.init_vars()
        self.init_ui(title)
    
    def init_vars(self) -> None:
        self.alarm_tracker = QAlarmTracker()

    def init_ui(self, title: str) -> None:
        # Title
        self.title_label = QLineEdit(text=title, alignment=Qt.AlignmentFlag.AlignLeft)
        self.title_label.setObjectName("AlarmTitle")
        self.title_label.setReadOnly(True)

        # Delete Button
        self.delete_button = QPushButton(text="x")
        self.delete_button.setFixedSize(20, 20)
        self.delete_button.setObjectName("DeleteBlockButton")
        self.delete_button.hide()

        # Alarm Edit
        self.alarm_edit = QTimeEdit()
        self.alarm_edit.setDisplayFormat("HH:mm")
        self.alarm_edit.setTime(QTime(7, 0))
        self.alarm_edit.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.alarm_edit.setObjectName("AlarmTime")
        self.alarm_tracker.alarm_edit = self.alarm_edit
        self.alarm_tracker.tracking_time = self.alarm_edit.time()

        # Toggle Button
        self.toggle_button = QPushButton(text="OFF")
        self.toggle_button.setCheckable(True)
        self.toggle_button.setFixedSize(30, 30)
        self.toggle_button.setObjectName("AlarmToggle")

        # Center stack (title above time)
        center_layout = QVBoxLayout(alignment=Qt.AlignCenter)
        center_layout.setSpacing(2)
        center_layout.addWidget(self.title_label)
        center_layout.addWidget(self.alarm_edit)
        
        # Main horizontal layout
        main_layout = QHBoxLayout(self)
        main_layout.setContentsMargins(10, 10, 10, 10)
        main_layout.setSpacing(12)

        main_layout.addWidget(self.delete_button, alignment=Qt.AlignLeft | Qt.AlignVCenter)
        main_layout.addLayout(center_layout)
        main_layout.addWidget(self.toggle_button, alignment=Qt.AlignRight | Qt.AlignVCenter)

        # Connect signals
        self.toggle_button.clicked.connect(self.toggle_alarm)
        self.delete_button.clicked.connect(self.delete_block)

        self.setLayout(main_layout)
        self.setObjectName("AlarmBlock")
    
    def toggle_alarm(self):
        if self.toggle_button.text() == "OFF":
            self.toggle_button.setText("ON")
            self.alarm_tracker.tracking = True
            self.alarm_tracker.start_tracking(self.alarm_edit.time())
        else:
            self.toggle_button.setText("OFF")
            self.alarm_tracker.tracking = False
            self.alarm_tracker.stop_tracking()

    def delete_block(self):
        self.deleteLater()
