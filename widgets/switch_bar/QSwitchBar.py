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
        # Create buttons
        self.stopwatch_switch_button = QPushButton(text="Stopwatch", objectName="StopwatchSwitchButton")
        self.countdown_switch_button = QPushButton(text="Countdown", objectName="CountdownSwitchButton")
        self.alarm_switch_button = QPushButton(text="Alarm", objectName="AlarmSwitchButton")

        # Modify button
        self.stopwatch_switch_button.setDisabled(True)
        for button in [self.stopwatch_switch_button, self.countdown_switch_button, self.alarm_switch_button]:
            button.setFixedHeight(20)
        
        # Create layouts
        main_layout = QHBoxLayout(self)
        main_layout.setContentsMargins(5, 5, 5, 5)
        main_layout.setSpacing(10)

        self.buttons_layout = QHBoxLayout()
        self.buttons_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.addLayout(self.buttons_layout)

        # Add buttons to layout
        self.buttons_layout.addWidget(self.stopwatch_switch_button)
        self.buttons_layout.addWidget(self.countdown_switch_button)
        self.buttons_layout.addWidget(self.alarm_switch_button)

        # Connect signals
        self.screen_map = {
            self.stopwatch_switch_button: QStopwatchScreen,
            self.countdown_switch_button: QCountdownScreen,
            self.alarm_switch_button: QAlarmScreen,
        }
        for button in self.screen_map:
            button.clicked.connect(lambda _, b=button: self.switch_screen(b))

        self.set_theme("stopwatch")
    
    def switch_screen(self, button: QPushButton) -> None:
        self.window.screen_manager.switch_to(self.screen_map[button])

        for i in range(self.buttons_layout.count()):
            widget = self.buttons_layout.itemAt(i).widget()
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