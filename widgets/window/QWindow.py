# PySide6 Widgets
from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget
from PySide6.QtCore import Qt

# Created Widgets
from widgets.title_bar.QTitleBar import QTitleBar
from widgets.switch_bar.QSwitchBar import QSwitchBar
from .ScreenManager import ScreenManager
from .StyleManager import StyleManager

# Screens
from widgets.stopwatch_widgets.QStopwatchScreen import QStopwatchScreen

class QWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_meta()
        self.init_managers()
        self.init_ui()
    
    def init_meta(self) -> None:
        self.setWindowTitle("All Purpose Timer")
        self.setProperty("theme", "main")
        
        self.width: int = 250
        self.height: int = 375
        self.setFixedSize(self.width, self.height)
        
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        
        with open ("style.qss") as f: self.setStyleSheet(f.read())

    def init_managers(self) -> None:
        self.screen_manager = ScreenManager(self)
        self.style_manager = StyleManager(self)
   
    def init_ui(self) -> None:
        # Create main round container
        self.roundWidget = QWidget(self)
        self.roundWidget.setObjectName("RoundWidget")
        self.roundWidget.setProperty("theme", "main")
        self.roundWidget.resize(self.width, self.height)

        # Layout inside the round widget
        self.roundLayout = QVBoxLayout()
        self.roundLayout.setContentsMargins(0, 0, 0, 0)
        self.roundLayout.setSpacing(0)
        self.roundWidget.setLayout(self.roundLayout)

        # Create title bar inside the round widget
        self.titleBar = QTitleBar("All Purpose Timer", self)
        self.roundLayout.addWidget(self.titleBar)

        # Create switch bar inside the round widget
        self.switchBar = QSwitchBar(self)
        self.roundLayout.addWidget(self.switchBar)

        # Create content area
        self.contentWidget = QWidget(self.roundWidget)
        self.roundLayout.addWidget(self.contentWidget)

        # Create content layout
        self.contentLayout = QVBoxLayout()
        self.contentWidget.setLayout(self.contentLayout)

        # Set roundWidget as the central widget
        self.setCentralWidget(self.roundWidget)
        self.screen_manager.switch_to(QStopwatchScreen)