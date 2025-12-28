from PySide6.QtWidgets import QWidget, QHBoxLayout, QFrame, QPushButton

# Screens
from widgets.stopwatch_widgets.QStopwatchScreen import QStopwatchScreen
from widgets.countdown_widgets.QCountdownScreen import QCountdownScreen
from widgets.alarm_widgets.QAlarmScreen import QAlarmScreen

class QSwitchBar(QFrame):
    def __init__(self, window):
        super().__init__(window)
        self.init_meta()
        self.init_vars(window)
        self.init_ui()
        self.setFixedHeight(30)
        self.setMouseTracking(True)
    
    def init_meta(self) -> None:
        self.setObjectName("SwitchBar")
        self.setProperty("theme", "stopwatch")
        self.setAutoFillBackground(True)
        self.setFrameShape(QFrame.NoFrame)

    def init_vars(self, window) -> None:
        self.window = window

    def init_ui(self) -> None:
        # Create layouts
        mainLayout = QHBoxLayout(self)
        mainLayout.setContentsMargins(5, 5, 5, 5)
        mainLayout.setSpacing(10)
        
        self.buttonsLayout = QHBoxLayout()
        self.buttonsLayout.setContentsMargins(0, 0, 0, 0)
        mainLayout.addLayout(self.buttonsLayout)

        # Create buttons
        self.stopwatchSwitchButton = QPushButton(text="Stopwatch", objectName="StopwatchSwitchButton")
        self.countdownSwitchButton = QPushButton(text="Countdown", objectName="CountdownSwitchButton")
        self.alarmSwitchButton = QPushButton(text="Alarm", objectName="AlarmSwitchButton")

        # Modify button
        self.stopwatchSwitchButton.setDisabled(True)
        for button in [self.stopwatchSwitchButton, self.countdownSwitchButton, self.alarmSwitchButton]:
            button.setFixedHeight(20)

        # Add buttons to layout
        self.buttonsLayout.addWidget(self.stopwatchSwitchButton)
        self.buttonsLayout.addWidget(self.countdownSwitchButton)
        self.buttonsLayout.addWidget(self.alarmSwitchButton)

        # Connect signals
        self.screen_map = {
            self.stopwatchSwitchButton: QStopwatchScreen,
            self.countdownSwitchButton: QCountdownScreen,
            self.alarmSwitchButton: QAlarmScreen,
        }
        for button in self.screen_map:
            button.clicked.connect(lambda _, b=button: self.switch_screen(b))

        self.set_theme("stopwatch")
    
    def switch_screen(self, button: QPushButton) -> None:
        self.window.screen_manager.switch_to(self.screen_map[button])

        for i in range(self.buttonsLayout.count()):
            widget = self.buttonsLayout.itemAt(i).widget()
            if not widget:
                continue
            
            widget.setDisabled(widget is button)
    
    def set_theme(self, theme: str) -> None:
        # Set theme on this widget
        self.setProperty("theme", theme)

        # Re-polish self
        self.style().unpolish(self)
        self.style().polish(self)
        self.update()

        # Apply theme to children
        for child in self.findChildren(QWidget):
            child.setProperty("theme", theme)
            child.style().unpolish(child)
            child.style().polish(child)
            child.update()