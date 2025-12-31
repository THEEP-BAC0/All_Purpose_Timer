from PySide6.QtWidgets import QTimeEdit, QAbstractSpinBox
from PySide6.QtCore import Qt

class QTimeRange(QTimeEdit):
    def __init__(self):
        super().__init__()
        self.setDisplayFormat("hh:mm:ss")
        self.setObjectName("TimeRange")
        self.setFixedSize(200, 100)
        self.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.setAlignment(Qt.AlignCenter)