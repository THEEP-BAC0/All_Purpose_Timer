from PySide6.QtCore import QObject, QTimer, QTime
from datetime import datetime


class QAlarmTracker(QObject):
    def __init__(self):
        super().__init__()
        self.tracking_time: QTime | None = None
        self.tracking: bool = False

        # Timer (fires every minute)
        self.timer = QTimer(self)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.check_time)

    def start_tracking(self, time: QTime) -> None:
        self.tracking_time = time
        self.tracking = True

        # Immediate check so alarms set to "now" fire instantly
        self.check_time()

        if not self.timer.isActive():
            self.timer.start()

    def stop_tracking(self) -> None:
        self.tracking = False
        self.timer.stop()

    def check_time(self) -> None:
        if not self.tracking or self.tracking_time is None:
            return
        
        now = datetime.now()

        if (
            self.tracking_time.hour() == now.hour
            and self.tracking_time.minute() == now.minute
        ):
            self.beep_alarm()
            self.stop_tracking()

    def beep_alarm(self) -> None:
        print("Alarm time reached!")